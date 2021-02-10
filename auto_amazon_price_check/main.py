import smtplib
import ssl

import requests
from bs4 import BeautifulSoup

headers = {
    "Accept-Language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.150 Safari/537.36 "
}
url = "https://www.amazon.com/-/he/dp/B07D9FB15R/ref=sr_1_2?dchild=1&keywords=garmin+fenix&qid=1612957155&sr=8-2"
response = requests.get(url=url, headers=headers)
sp = BeautifulSoup(response.text, "html.parser")
temp = str(sp.select("#priceblock_ourprice"))
index_of_dollar = temp.index("$")
print(index_of_dollar)
price = float(temp[index_of_dollar - 7:index_of_dollar])
print(price)
from_mail = "matca2954@gmail.com"
from_password = "ma291188"
to_mail = "matca2952@gmail.com"
target_price = 400.00
if price <= target_price:
    msg = f"Subject:price is low!!!\n\nThe price of the Fenix 5 is lower then {target_price}. the price is now {price}"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", context=context) as server:
        server.login(from_mail, from_password)
        server.sendmail(from_addr=from_mail, to_addrs="matca2952@gmail.com", msg=msg)
