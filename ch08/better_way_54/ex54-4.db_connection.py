# db_connection.py
import sys

class Win32Database(object):
    # ...

class PosixDatabase(object):
    # ...

if sys.platform.startswitch('win32'):
    Database = Win32Database
else:
    Database = PosixDatabase
