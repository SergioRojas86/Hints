import pandas as pd
import pyodbc

def odbc_exec(sqcmd):
    cnxn = pyodbc.connect('')
    cnxn.autocommit = True
    cursor = cnxn.cursor()
    cursor.execute(sqcmd)
