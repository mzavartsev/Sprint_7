import requests
import json
from data import *


class OrdersMethods:
    def __init__(self, color=[]):
        self.order_data = {
                "firstName": "Naruto",
                "lastName": "Uchiha",
                "address": "Konoha, 142 apt.",
                "metroStation": 4,
                "phone": "+7 800 355 35 35",
                "rentTime": 5,
                "deliveryDate": "2020-06-06",
                "comment": "Saske, come back to Konoha",
                "color": color
            }

    def post_create_order(self):
        json_data = json.dumps(self.order_data)
        self.create_order = requests.post(f"{BASE_URL}{CREATE_ORDER}", data=json_data)
        return self.create_order.status_code, self.create_order.text, self.create_order.json()

    def get_get_order_info(self, track=""):
        if track == "":
            self.get_info_about_order = requests.get(f"{BASE_URL}{GET_LIST_OF_ORDERS}")
        else:
            self.get_info_about_order = requests.get(f"{BASE_URL}{GET_ORDER}{track}")
        return self.get_info_about_order.status_code, self.get_info_about_order.text, self.get_info_about_order.json()
