from rdflib import Graph

# Create a Graph
g = Graph()

# Parse in an RDF file hosted on the Internet
g.parse("https://raw.githubusercontent.com/gtfierro/mortar-parquet-support/main/mortar-parquet-client/graphs/bldg1.ttl", format='ttl')

# Puts SPARQL query result into PYTHON variable
res = g.query('SELECT * WHERE { ?vav a brick:VAV . ?vav brick:hasPoint ?p . ?p rdf:type ?type }')
res_2 = g.query('SELECT * WHERE { ?equip brick:feeds ?downstream . ?equip brick:isFedBy ?upstream }')

# TODO: add more SPARQL comands
# Create a Graph
g2 = Graph()

# Parse in an RDF file hosted on the Internet
g2.parse("https://raw.githubusercontent.com/gtfierro/mortar-parquet-support/main/mortar-parquet-client/graphs/bldg10.ttl" , format='ttl')

# Puts SPARQL query result into PYTHON variable
res_3 = g2.query('SELECT * WHERE { }')


# Function I can pass multipl SPARQL comands into
def SPARQL_to_SQL(results):
    # Getting variable names from query 
    vars = results.vars

    # Create the SQL command 
    table_name = 'test_table'
    sql_command = f'CREATE TABLE {table_name} ('
    for var in vars:
        sql_command += f'{var} TEXT, '
    sql_command = sql_command[:-2] + ');'
    print(sql_command)

# Call function SPARQL_to_SQL(results) with passing in res
SPARQL_to_SQL(res)
SPARQL_to_SQL(res_2)
SPARQL_to_SQL(res_3)

# TODO: Display the SQL table

# TODO: SQL to SPARQL