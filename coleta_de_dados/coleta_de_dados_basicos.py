import requests
from bs4 import BeautifulSoup
import pandas


response = requests.get("https://br.financas.yahoo.com/quote/%5EBVSP/history/")

print("requests: ")
print(response.text[:600])

soup = BeautifulSoup(response.text,"html.parser")
print("soup: ")
print(soup.prettify()[:1000])

print("pandas: ")
url_dados = pandas.read_html("https://br.financas.yahoo.com/quote/%5EBVSP/history/")
print(url_dados[0].head(10))