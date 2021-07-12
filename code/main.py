import os
import time
import datetime
from logger import Logger
from processor import *
import numpy as np

TEMP_FOLDER = os.getenv('TEMP_FOLDER', '/tmp/')
logger = Logger.getLogger(__name__)

def run_process(mode):
    try:
        input_df = pd.read_csv(f'{args.input_folder}/{args.file_name}')
    except Exception as e:
        raise e

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_folder', type=str, default=os.getenv('INPUT_FOLDER', '../data/input'))
    parser.add_argument('--output_folder', type=str, default=os.getenv('INPUT_FOLDER', '../data/output'))
    parser.add_argument('--file_name', type=str, default=os.getenv('FILE_NAME', 'btc.csv'))
    parser.add_argument('--mode', type=str, default=os.getenv('MODE', 'all'))
    args, _ = parser.parse_known_args()
    run_process(args.mode)


