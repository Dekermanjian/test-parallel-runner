"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.8
"""
import polars as pl

def sum_data(data: pl.DataFrame, group: str) -> pl.DataFrame:
    """simple sum function"""
    return data.filter(pl.col('group')==group).select(pl.col('value').sum())