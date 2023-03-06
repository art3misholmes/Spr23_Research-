from rdflib import Graph
import mysql.connector

#TODO: intake model to SPARQL

# Create a Graph
g = Graph()

# Parse in an RDF file hosted on the Internet
g.parse("https://raw.githubusercontent.com/gtfierro/mortar-parquet-support/main/mortar-parquet-client/graphs/bldg1.ttl", format='ttl')

# Puts SPARQL query result into PYTHON variable - given querys 
res = g.query('SELECT * WHERE { ?vav a brick:VAV . ?vav brick:hasPoint ?p . ?p rdf:type ?type }')

# Getting variable names from query 
vars = results.vars

# Create the SQL command 
table_name = 'test_table'
sql_command = f'CREATE TABLE {table_name} ('
for var in vars:
    sql_command += f'{var} TEXT, '
sql_command = sql_command[:-2] + ');'

# Used squlite to create in memory database and run commands 
# Create database in memory
mydb = mysql.connector.connect(
    host="localhost",
    user="kwood1",
    password="1234@"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE test_5_database")

# Run command
mycursor.execute(sql_command)

# Check to see if table was created
mycursor.execute("SELECT * FROM test_table")

#TODO: get right datatypes put in the schema

#TODO: SQL to SPARQL
# get database
# either create table or select frome table
# 