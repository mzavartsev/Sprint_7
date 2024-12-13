import pytest
from methods.couriers_methods import *


@pytest.fixture()
def return_correct_creds_for_new_courier():
    courier_data = return_login_password()
    return courier_data

@pytest.fixture()
def create_courier(return_correct_creds_for_new_courier):
    new_courier = CourierMethods(return_correct_creds_for_new_courier)
    new_courier.post_create_courier()
    return new_courier

@pytest.fixture()
def create_and_delete_courier(return_correct_creds_for_new_courier):
    new_courier = CourierMethods(return_correct_creds_for_new_courier)
    new_courier.post_create_courier()
    courier_id = CourierMethods(return_correct_creds_for_new_courier).post_login_courier()
    yield new_courier
    CourierMethods(return_correct_creds_for_new_courier).delete_courier(courier_id[1]["id"])
