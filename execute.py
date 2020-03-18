from src.db import mssql

# Test if the connection works. If returns True then backup is possible
#mssql.test()

# Backup the database
mssql.backup('database')
