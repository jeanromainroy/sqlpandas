# SQLpandas

Creates a wrapper around a Pandas Dataframe to run SQL query.

## Requirements

- python >=3.6

- libs : click, pandas


## Installation

To install

    python3 setup.py install


## Usage

In a script,

    import pandas as pd
    from sqlpandas import SQLpandas

    # load csv using pandas
    df = pd.read_csv('./path/to/my/csv')

    # feed to sql pandas
    sql_df = SQLpandas(df)

    # you can now run sql queries (table take the 't' name)
    sql_df.query('SELECT count(*) FROM t')


Using the CLI,

    python3 -m sqlpandas run --filepath='/path/to/my/csv' --query='SELECT count(*) FROM t'

