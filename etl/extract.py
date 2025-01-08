import pandas as pd
from bs4 import BeautifulSoup
import requests


def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''

    page_html = requests.get(url).text
    soup = BeautifulSoup(page_html, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)

    table = soup.find_all('tbody')[0]
    rows = table.find_all('tr')

    for row in rows:
        col = row.find_all('td')
        if len(col) == 0:
            continue

        bank_name = col[1].text[:-1]
        bank_cap = float(col[2].text[:-1])

        data = {
            table_attribs[0]: bank_name,
            table_attribs[1]: [bank_cap]
        }
        df1 = pd.DataFrame(data)
        df = pd.concat([df, df1], ignore_index=True)

    return df
