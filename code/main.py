import os
import time
from datetime import datetime
import logging
from logger import Logger
from processor import *
import argparse
import pandas as pd
import numpy as np
import plotly.express as px

logging = Logger.getLogger(__name__)

def run_process():
    try:

        # PROCESSING DATA
        input_df = pd.read_csv(f'{args.input_folder}/{args.file_name}', index_col='date')
        target_columns = ['generatedCoins', 'paymentCount', 'marketcap(USD)', 'price(USD)']
        input_df = input_df[target_columns]
        # we get the last year only, to generalize this we can just lag the columns of interest
        # an implementation of above is in the processor file
        last_year_data = input_df[-365:]
        converted_data = conversor(df_in=last_year_data,
                                   columns_in=['marketcap(USD)', 'price(USD)'],
                                   columns_out=['marketcap(EUR)', 'price(EUR)'],
                                   conversion_ratio=0.87)
        converted_data.to_csv(f'{args.output_folder}/converted_data.csv')
        summary_input = converted_data[['generatedCoins', 'paymentCount', 'marketcap(EUR)', 'price(EUR)']]
        pivoted_summary_input = pd.melt(summary_input,
                                         var_name='variable',
                                         value_vars=['generatedCoins', 'paymentCount', 'marketcap(EUR)', 'price(EUR)'],
                                         ignore_index=False)
        summary_table = pivoted_summary_input.groupby('variable').agg([min, max, np.mean])
        summary_table.to_csv(f'{args.output_folder}/summary_data.csv')

        # PLOTTING DATA
        fig = px.line(converted_data, x=converted_data.index, y="price(EUR)")
        fig.write_html(f'{args.output_folder}/historical_price.html')

    except Exception as e:
        logging.error("Error while processing or plotting the data: " + str(e))
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_folder', type=str, default=os.getenv('INPUT_FOLDER', '../data/input'))
    parser.add_argument('--output_folder', type=str, default=os.getenv('INPUT_FOLDER', '../data/output'))
    parser.add_argument('--file_name', type=str, default=os.getenv('FILE_NAME', 'btc.csv'))
    parser.add_argument('--mode', type=str, default=os.getenv('MODE', 'all'))
    args, _ = parser.parse_known_args()
    run_process()


