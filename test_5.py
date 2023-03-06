from rdflib import Graph
import sqlite3
import pandas as pd

#TODO: intake model to SPARQL -- why did I put this again?

# Create a Graph
g = Graph()

# Parse in an RDF file hosted on the Internet
g.parse("https://raw.githubusercontent.com/gtfierro/mortar-parquet-support/main/mortar-parquet-client/graphs/bldg1.ttl", format='ttl')

# Puts SPARQL query result into PYTHON variable - given querys 
res = g.query('SELECT * WHERE { ?vav a brick:VAV . ?vav brick:hasPoint ?p . ?p rdf:type ?type }')

# Getting variable names from query 
vars = res.vars

# Create the SQL command to create table
table_name = 'test_table_5'
sql_command = f'CREATE TABLE {table_name} ('
for var in vars:
    sql_command += f'{var} TEXT, '
sql_command = sql_command[:-2] + ');'

#TODO: get right datatypes put in the schema -- how to use SPARQL to get datatype?

# Used squlite to create in memory database and run commands 
# Create database in memory
connection_obj = sqlite3.connect(':memory:')

# Run command
connection_obj.execute(sql_command)

# insert rows into table 
cur = connection_obj.cursor()
for row in res:
    valStrs = ""
    for var in vars:
        valStrs = valStrs + "'" + row[var].toPython() + "',"
    valStrs = valStrs[:-1]
    cur.execute("INSERT INTO " + table_name + " VALUES (" + valStrs + ")")

# Check to see if table was created
print(pd.read_sql_query("SELECT * FROM " + table_name, connection_obj))

#TODO: SQL to SPARQL
# get database
# either create table or select frome table
# ask if find or alter SPARQL database
