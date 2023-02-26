from rdflib import Graph
def GivenQuerys():
    # Create a Graph
    g = Graph()

    # Parse in an RDF file hosted on the Internet
    g.parse("https://raw.githubusercontent.com/gtfierro/mortar-parquet-support/main/mortar-parquet-client/graphs/bldg1.ttl", format='ttl')

    # Puts SPARQL query result into PYTHON variable - given querys 
    res = g.query('SELECT * WHERE { ?vav a brick:VAV . ?vav brick:hasPoint ?p . ?p rdf:type ?type }')
    res_2 = g.query('SELECT * WHERE { ?equip brick:feeds ?downstream . ?equip brick:isFedBy ?upstream }')

    # Call function SPARQL_to_SQL(results) with passing in res
    SPARQL_to_SQL(res)
    SPARQL_to_SQL(res_2)

# TODO: add more SPARQL comands
def NewQuerys():
    def graphTwo():
        # Create a Graph
        g2 = Graph()

        # Parse in an RDF file hosted on the Internet
        g2.parse("https://raw.githubusercontent.com/gtfierro/mortar-parquet-support/main/mortar-parquet-client/graphs/bldg10.ttl" , format='ttl')

        # Puts SPARQL query result into PYTHON variable

        # query syntax: SELECT * WHERE {?<variable name> a brick:<class type> . ?<same variable name> ...}
        # <a> spesifies the type of resorce 
        # <subject> <predicate> <object> [order for query]
        # subject's property *matches* object

        # using g2 link data lists all air handler units with "feeds" and type info -- retuns all air handler units
        res_3 = g2.query('SELECT * WHERE {?AHU a brick:Air_Handler_Unit . ?AHU brick:feeds ?feeds . ?t rdf:type ?type }')

        # using g2 link data lists all air handler units with "feeds" and "hasPoint"
        # why does it put var for 3rd column in 2nd column?
        res_4 = g2.query('SELECT * WHERE {?AHU a brick:Air_Handler_Unit . ?AHU brick:feeds ?feeds. ?AHU brick:hasPoint ?hasPoint}')

        # using g2 link data lists all floors
        # is this legal? 
        res_5 = g2.query('SELECT ?floor WHERE {?floor a brick:Floor}')

        # using g2 link data to see if we can get only the air handeling units hat have "hasPoint" -- output gives all the data points for "hasPoint"
        res_7 = g2.query('SELECT ?point WHERE {?AHU a brick:Air_Handler_Unit . ?AHU brick:feeds ?feeds. ?AHU brick:hasPoint ?point}')

        # Call function SPARQL_to_SQL(results) with passing in res
        SPARQL_to_SQL(res_3)
        SPARQL_to_SQL(res_4)
        SPARQL_to_SQL(res_5)
        SPARQL_to_SQL(res_7)

    def graphThree():
        # Create a Graph
        g3 = Graph()

        # Parse in an RDF file hosted on the Internet
        g3.parse("https://raw.githubusercontent.com/gtfierro/mortar-parquet-support/main/mortar-parquet-client/graphs/bldg11.ttl" , format='ttl')

        # using g3 link data, list all floors
        res_6 = g3.query('SELECT * WHERE {?floor a brick:Floor}')

        # Call function SPARQL_to_SQL(results) with passing in res
        SPARQL_to_SQL(res_6)

    # Call funtions graphs
    graphTwo()
    graphThree()

# Function I can pass multipul SPARQL commands into
# TODO: get vars in order
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

    # TODO: Display the SQL table

    # Shows data put into the rows of table
    for row in results:
        print(f"row: {row}")
    
# Call functions
GivenQuerys()
NewQuerys()

# TODO: SQL to SPARQL