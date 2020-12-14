import sys
import os
import click
import pandas as pd
from .sqlpandas import SQLpandas


@click.group()
def cli():
    pass


@click.command()
@click.option('--filepath', type=str, help='Path to .csv file')
@click.option('--sep', type=str, default=',', help="Separator (default ',')")
@click.option('--query', type=str, help="SQL Query")
def run(filepath, sep, query):
    """
        Runs a SQL query on a CSV file. Table will take the 't' name
    """

    # validate inputs
    if not os.path.exists(filepath):
        raise Exception('Invalid file path')

    if filepath[-3:] != 'csv':
        raise Exception('Invalid file type')

    if not isinstance(query, str) or len(query) == 0:
        raise Exception('Invalid query')

    # load csv using pandas
    df = pd.read_csv(filepath, sep=sep)

    # load with SQLpandas
    sqldf = SQLpandas(df)

    # run query
    res = sqldf.query(query)

    print(res)


# add commands
cli.add_command(run)


if __name__ == "__main__":
    cli()
