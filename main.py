import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEy = 'EE3T3UYSW8HCXPRE'
STOCK_ENDPOINT = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={API_KEy}'
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
response = requests.get(STOCK_ENDPOINT)
tesla_data = response.json()['Time Series (Daily)']
clean_data = []
print(clean_data)
for i in tesla_data:
    dat = i
    Open = float(tesla_data[i]['1. open'])
    new_item = {
        'date': i,
        'open_value': Open,

    }
    clean_data.append(new_item)
for i in range(1, len(clean_data) - 1):
    difference = abs(clean_data[i]['open_value'] - clean_data[i - 1]['open_value'])
    if difference > 20:
        print(('there was a big diffrence at {}'.format(clean_data[i]['date'])))
