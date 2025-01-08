# ETL Project - Top 10 largest banks in the world.

This project is about compiling the list of the top 10 largest banks in the world ranked by market capitalization in billion USD in GBP, INR, USD, and EUR Currency.

## Extraction
It extracts structured data from wikipedia using web scraping. HTML extraction for web scraping with BeautifulSoup from tables and converting the information into a Pandas DataFrame for future processing.

## Transformation
It accesses a CSV file for exchange rate information and adds three columns to the data frame, each containing the transformed version of Market Cap column to respective currencies

## Loading
It saves the final data frame as a CSV file in a specific path from config.py, it can also save the final data frame to a database table. This project uses a sqlite database.

## Logging
It logs the mentioned message of a given stage of the code execution to a log file.
