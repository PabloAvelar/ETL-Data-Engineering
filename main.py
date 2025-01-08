import sqlite3
from config import url, csv_path, csv_output_path, db_name, table_name, log_file, extraction_attr
from etl.extract import extract
from etl.transform import transform
from etl.load import load_to_csv, load_to_db, run_query
from etl.utils import log_progress


def etl_process():
    log_progress('Preliminaries complete. Initiating ETL process', log_file)

    data = extract(url, extraction_attr)
    log_progress('Data extraction complete. Initiating Transformation process', log_file)

    transformed_data = transform(data, csv_path)
    log_progress('Data transformation complete. Initiating Loading process', log_file)
    print(transformed_data)

    load_to_csv(transformed_data, csv_output_path)
    log_progress('Data saved to CSV file', log_file)

    conn = sqlite3.connect(db_name)
    log_progress('SQL Connection initiated', log_file)

    load_to_db(transformed_data, conn, table_name)
    log_progress('Data loaded to Database as a table, Executing queries', log_file)

    # Print the contents of the entire table
    query_statement = f'SELECT * FROM {table_name}'
    run_query(query_statement, conn)

    # Print the average market capitalization of all the banks in Billion USD.
    query_statement = f'SELECT AVG(MC_GBP_Billion) FROM {table_name}'
    run_query(query_statement, conn)

    # Print only the names of the top 5 banks
    query_statement = f'SELECT Name from {table_name} LIMIT 5'
    run_query(query_statement, conn)
    log_progress('Process Complete', log_file)

    conn.close()
    log_progress('Server Connection closed', log_file)


if __name__ == '__main__':
    etl_process()
