import requests
from datetime import datetime
from constants import auction_original_price_dict
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
api_key = os.environ.get("DF_API")

url = "https://api.neople.co.kr/df/auction?itemName={}&limit=2&apikey={}"


def get_average_item_price(item_name):
    response = requests.get(url.format(item_name, api_key)).json()
    response_one = response['rows'][0]

    current_dt = datetime.today().replace(microsecond=0)

    document = {
        "itemId": response_one["itemId"],
        "itemName": response_one['itemName'],
        "averagePrice": response_one['averagePrice'],
        "date_time": current_dt,
        "cost_per_gold": auction_original_price_dict[item_name] * 1000000 / response_one['averagePrice']
    }

    return document


if __name__ == '__main__':
    print(get_average_item_price("선계 : 조화의 수호자 패키지"))


