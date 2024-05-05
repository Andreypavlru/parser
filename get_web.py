import requests
from bs4 import BeautifulSoup


link = "https://vdrifte.ru/results/rdsgp2023/"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')
result_table_js = soup.find('table', {"class" : "rating"})

def get_result_table():
    return result_table_js

