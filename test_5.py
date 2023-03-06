from rdflib import Graph
import sqlite3

#TODO: intake model to SPARQL

# Create a Graph
g = Graph()

# Parse in an RDF file hosted on the Internet
g.parse("https://raw.githubusercontent.com/gtfierro/mortar-parquet-support/main/mortar-parquet-client/graphs/bldg1.ttl", format='ttl')

# Puts SPARQL query result into PYTHON variable - given querys 
res = g.query('SELECT * WHERE { ?vav a brick:VAV . ?vav brick:hasPoint ?p . ?p rdf:type ?type }')

# Getting variable names from query 
vars = res.vars

# Create the SQL command 
table_name = 'test_table'
sql_command = f'CREATE TABLE {table_name} ('
for var in vars:
    sql_command += f'{var} TEXT, '
sql_command = sql_command[:-2] + ');'

#TODO: insert rows into table

# Used squlite to create in memory database and run commands 
# Create database in memory
connection_obj = sqlite3.connect(':memory:')

# Run command
connection_obj.execute(sql_command)

# Check to see if table was created
cur = connection_obj.cursor()
cur.execute("SELECT * FROM test_table")
print(cur.fetchone())

#TODO: get right datatypes put in the schema

#TODO: SQL to SPARQL
# get database
# either create table or select frome table
# 