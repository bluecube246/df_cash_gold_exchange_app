def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "complete": todo["complete"]
    }


def list_serial(todos) -> list:
    return[individual_serial(todo) for todo in todos]


def individual_serial_2(todo) -> dict:
    return {
        "objectId": str(todo["_id"]),
        "itemId": todo["itemId"],
        "itemName": todo["itemName"],
        "averagePrice": todo["averagePrice"],
        "date_time": todo["date_time"],
        "pricePerGold": todo["cost_per_gold"]
    }


def list_serial_2(todos) -> list:
    return[individual_serial_2(todo) for todo in todos]