url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
csv_path = './data/exchange_rate.csv'
csv_output_path = './data/Largest_banks_data.csv'

db_name = './database/Banks.db'
table_name = 'Largest_banks'
log_file = './logs/code_log.txt'
extraction_attr = ['Name', 'MC_USD_Billion']
final_attr = ['Name', 'MC_USD_Billion', 'MC_GBP_Billion', 'MC_EUR_Billion', 'MC_INR_Billion']
