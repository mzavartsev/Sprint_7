import allure
from data import *
from randomizer import *


class CourierMethods:
    def __init__(self, courier_data):
        self.courier_data = courier_data
        self.login_courier = None

    def post_create_courier(self):
        with allure.step("Создание курьера"):
            self.create_courier = requests.post(f"{BASE_URL}{CREATE_COURIER}", data=self.courier_data)
            return self.create_courier.status_code, self.create_courier.text, self.create_courier.json()

    def post_login_courier(self):
        with allure.step("Авторизация курьера"):
            login_pass = self.courier_data.copy()
            del login_pass["firstName"]
            self.login_courier = requests.post(f"{BASE_URL}{LOGIN_COURIER}", data=login_pass)
            return self.login_courier.status_code, self.login_courier.json()

    def delete_courier(self, id):
        self.delete_courier = requests.delete(f"{BASE_URL}{DELETE_COURIER.replace(":id", str(id))}")
        return self.delete_courier.status_code, self.delete_courier.text, self.delete_courier.json()



