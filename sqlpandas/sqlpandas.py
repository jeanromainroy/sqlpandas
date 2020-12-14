import os
import uuid
import sqlite3
import pandas as pd

class SQLpandas:

    def __init__(self, df):

        # path to temp db
        self.db_path = f'.{uuid.uuid4()}.db'

        # make sure it doesn't already exist
        self.clear()

        # grab connection
        self.conn = sqlite3.connect(self.db_path)

        # grab columns
        self.cols = list(df.columns)

        # convert values to list
        values_list = [tuple(d) for d in df.values.tolist()]

        # column tuple
        columns_str = ', '.join(self.cols)

        # unknown tuple
        unknown_str = ', '.join(['?']*len(self.cols))

        # init a cursor
        cur = self.conn.cursor()

        # create table
        cur.execute(f'CREATE TABLE t ({columns_str});')
        self.conn.commit()

        # insert values
        insert_query = f"INSERT INTO t ({columns_str}) VALUES ({unknown_str});"
        cur.executemany(insert_query, values_list)
        self.conn.commit()


    def __del__(self):
        """
            Destructor
        """
        self.close()
        self.clear()


    def clear(self):
        """
            Removes the temporary database from the disk
        """
        if os.path.exists(self.db_path):
            os.remove(self.db_path)


    def close(self):
        """
            Closes the connection to the database
        """
        self.conn.close()


    def columns(self):
        """
            Returns the columns
        """
        return self.cols


    def query(self, query):
        """
            Runs a SQL query and returns results as pandas dataframe. Table will take the 't' name
        """
        return pd.read_sql(query, self.conn)
