from config.database import df_db
from api.constants import average_auction_dict

results = []
for item, collection in average_auction_dict.items():
    result = df_db[collection].find().sort({"$natural": 1}).limit(1)
    print([res for res in result][0])
    results.append(result)
