from logger import Logger
import pandas as pd
pd.options.mode.chained_assignment = None  # false positive of copy warning

logging = Logger.getLogger(__name__)


def lag_processor(df_in, target_columns, lag=365, drop_nans=True) -> pd.DataFrame:
    """
    This function creates the lag values (previous values according to the index of the pd.Series)
    for the columns mentioned in the target_columns and the steps specified in the lags argument

    Parameters
    ----------
    df_in : pd.DataFrame
        Input dataframe
    target_columns : list
        A list containing the target columns that will be lagged
    lag: int
        An integer containing the look back for calculating the previous data
    drop_nans: bool
        A boolean specifying if we drop the nans of the dataset or not

    Returns
    -------
    pd.DataFrame
        A dataframe containing the lagged values of the target columns
    """
    try:
        dict_out = {}
        for col_name in target_columns:
            dict_out[col_name] = df_in[col_name]
            # create lagged Series
            dict_out['%s_lag%d' % (col_name, lag)] = df_in[col_name].shift(lag)
        df_out = pd.DataFrame(dict_out, index=df_in.index)
        if drop_nans:
            df_out = df_out.dropna()
        else:
            df_out = df_out
        logging.info(f'Successfully lagged {target_columns}')
    except Exception as e:
        raise e
    return df_out


# def summary_output(df_in):
#    return

def conversor(df_in, columns_in, columns_out, conversion_ratio) -> pd.DataFrame:
    """
    This function converts the value of the columns within the columns_in list according to
    a conversion ratio between EUROs and USD

    Parameters
    ----------
    df_in : pd.DataFrame
        Input dataframe
    columns_in : list
        A list containing the columns that will be converted to EURO
    columns_out : list
        A list containing the name of the output columns after the conversion
    conversion_ratio : float
        An integer with the value of the conversion ratio

    Returns
    -------
    pd.DataFrame
        A dataframe containing the converted columns in EURO
    """
    try:
        df_in[columns_out] = df_in[columns_in] * conversion_ratio
        # logging.info(f'Successfully converted {columns_in} to EURO')
    except Exception as e:
        raise e
    return df_in
