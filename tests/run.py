import unittest

import pandas as pd
from sqlpandas import SQLpandas as sqlpd

# path to sample data
path = './tests/data.csv'

class TestClass(unittest.TestCase):

    def test_basic(self):

        # load in dataframe
        df = pd.read_csv(path)

        # create a db
        sql_df = sqlpd(df)

        # print columns
        print(sql_df.columns())

        # query
        print(sql_df.query('SELECT * FROM t').head(5))

        # query
        print(sql_df.query('SELECT * FROM t WHERE latitude <= 33 LIMIT 10').head(5))

if __name__ == '__main__':
    unittest.main()
