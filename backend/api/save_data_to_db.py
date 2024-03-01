from dotenv import load_dotenv, find_dotenv
from dnf_api import get_average_item_price
from config.database import df_db
from constants import average_auction_dict
import schedule
import time
load_dotenv(find_dotenv())


def save_to_mongo_db(item, collection):
    document = get_average_item_price(item)
    inserted_id = df_db[collection].insert_one(document).inserted_id
    print(str(inserted_id) + " has been inserted.")


def save_all_to_mongo_db():
    for _item, _collection in average_auction_dict.items():
        save_to_mongo_db(_item, _collection)
    print("saved")


if __name__ == '__main__':
    save_all_to_mongo_db()

    # schedule.every(10).minutes.do(save_all_to_mongo_db)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

