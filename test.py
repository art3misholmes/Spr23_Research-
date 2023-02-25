from rdflib import Graph

# Create a Graph
g = Graph()

# Parse in an RDF file hosted on the Internet
g.parse("https://raw.githubusercontent.com/gtfierro/mortar-parquet-support/main/mortar-parquet-client/graphs/bldg1.ttl", format='ttl')

# Puts SPARQL query result into PYTHON variable
res = g.query('SELECT * WHERE { ?vav a brick:VAV . ?vav brick:hasPoint ?p . ?p rdf:type ?type }')

# Getting variable names from query 
vars = res.vars

# Create the SQL command 
table_name = 'test_table'
sql_command = f'CREATE TABLE {table_name} ('
for var in vars:
    sql_command += f'{var} TEXT, '
sql_command = sql_command[:-2] + ');'
print(sql_command)

