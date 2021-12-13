# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:54:33 2021

@author: hasnaw

"""
def GetConnectionString():
    driver="{ODBC Driver 17 for SQL Server}"
    server="server-data.database.windows.net" #
    database="DATA" 
    username=
    password=
    connectionString="DRIVER=" + driver + ";SERVER=" + server + "; DATABASE=" + database + "; UID=" + username + "; PWD=" + password 
    
    return connectionString
      

""" 
    driver="{ODBC Driver 17 for SQL Server}"
    server="NAWHASW10\MSSQLSERVER1"
    database="DATA"
    username=
    password=
    connectionString="DRIVER=" + driver + ";SERVER=" + server + "; DATABASE=" + database + "; UID=" + username + "; PWD=" + password 
   """