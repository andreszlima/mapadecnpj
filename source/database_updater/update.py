import csv
import psycopg2
import os

def clean_value(value):
    if value == '' or value == 'nan':
        return None
    return value

def insert_csv_data_to_table(csv_file_path, table_name, conn):
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Open the CSV file for reading
    with open(csv_file_path, 'r', encoding='latin-1') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Construct the SQL INSERT query with ON CONFLICT clause
        insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(next(csvreader)))}) ON CONFLICT DO NOTHING"
        
        # Convert csvreader to a list of tuples for insertion
        rows = [tuple(clean_value(cell) for cell in row) for row in csvreader]
        
        # Execute the insert query with the rows
        cur.executemany(insert_query, rows)

    # Liberar memória
    csvfile.close()

    if table_name == "paises":
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO paises (codigo, descricao)
                SELECT generate_series(1, 1000), ''
                ON CONFLICT (codigo) DO NOTHING;
            """)

    if table_name == "qualificacoes_de_socios":
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO qualificacoes_de_socios (codigo, descricao)
                SELECT generate_series(1, 1000), ''
                ON CONFLICT (codigo) DO NOTHING;
            """)

    # Commit the changes and close the cursor
    conn.commit()
    cur.close()

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="mapadecnpj_dev",
    user="andreszlima",
    password="a12345"
)

## Cnaes ----------------------------------------------------------------------

# Path to your CSV file
csv_file_path = os.path.join(script_dir, "csv", "parsed_Cnaes.csv")
# Specify the table name
table_name = "cnaes"
# Call the function to insert data
#insert_csv_data_to_table(csv_file_path, table_name, conn)
print("Cnaes inseridos")


## Simples -------------------------------------------------------------------

# Path to your CSV file
csv_file_path = os.path.join(script_dir, "csv", "parsed_Simples.csv")
# Specify the table name
table_name = "simples"
# Call the function to insert data
#insert_csv_data_to_table(csv_file_path, table_name, conn)
print("Simples Nacional inserido")

## Natureza Jurídica ---------------------------------------------------------

# Path to your CSV file
csv_file_path = os.path.join(script_dir, "csv", "parsed_Naturezas.csv")
# Specify the table name
table_name = "naturezas_juridicas"
# Call the function to insert data
#insert_csv_data_to_table(csv_file_path, table_name, conn)
print("Naturezas Jurídicas inseridas")

## Qualificações de sócios ---------------------------------------------------

# Path to your CSV file
csv_file_path = os.path.join(script_dir, "csv", "parsed_Qualificacoes.csv")
# Specify the table name
table_name = "qualificacoes_de_socios"
# Call the function to insert data
#insert_csv_data_to_table(csv_file_path, table_name, conn)
print("Qualificações de sócios inseridas")

## Países -------------------------------------------------------------------

# Path to your CSV file
csv_file_path = os.path.join(script_dir, "csv", "parsed_Paises.csv")
# Specify the table name
table_name = "paises"
# Call the function to insert data
#insert_csv_data_to_table(csv_file_path, table_name, conn)
print("Países inseridos")

## Municípios ---------------------------------------------------------------

# Path to your CSV file
csv_file_path = os.path.join(script_dir, "csv", "parsed_Municipios.csv")
# Specify the table name
table_name = "municipios"
# Call the function to insert data
#insert_csv_data_to_table(csv_file_path, table_name, conn)
print("Municípios inseridos")

## Motivos ---------------------------------------------------------------

# Path to your CSV file
csv_file_path = os.path.join(script_dir, "csv", "parsed_Motivos.csv")
# Specify the table name
table_name = "motivos"
# Call the function to insert data
#insert_csv_data_to_table(csv_file_path, table_name, conn)
print("Motivos inseridos")

## Empresas -----------------------------------------------------------------

# Loop through files in the directory
csv_directory = os.path.join(script_dir, "csv")
for file_name in os.listdir(csv_directory):
    if "Empresas" in file_name:
        csv_file_path = os.path.join(csv_directory, file_name)
        # Specify the table name
        table_name = "empresas"
        # Call the function to insert data
        #insert_csv_data_to_table(csv_file_path, table_name, conn)
        print(file_name + " inserido")

## Estabelecimentos -----------------------------------------------------------

# Loop through files in the directory
csv_directory = os.path.join(script_dir, "csv")
for file_name in os.listdir(csv_directory):
    if "Estabelecimentos" in file_name:
        csv_file_path = os.path.join(csv_directory, file_name)
        # Specify the table name
        table_name = "estabelecimentos"
        # Call the function to insert data
        insert_csv_data_to_table(csv_file_path, table_name, conn)
        print(file_name + " inserido")


# Close the connection
conn.close()
print("Conexão fechada")