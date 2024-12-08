import allure
from methods.order_methods import *
import pytest


@allure.feature("Order")
class TestOrder:

    @pytest.mark.parametrize("color", [(["BLACK"]),
                                            (["GREY"]),
                                            (["BLACK","GREY"]),
                                            ([])]
                             )
    @allure.title("Создание заказа с указанием различных значенией в 'color'")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_create_order(self, color):
        new_order = OrdersMethods(color).post_create_order()
        assert 201 == new_order[0]

    @allure.title("Возвращается track key после успешного создания заказа")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_check_track_key_after_create_order(self):
        new_order = OrdersMethods().post_create_order()
        assert "track" in new_order[1]

    @allure.title("Возвращается список с заказами")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_get_list_of_orders(self):
        get_list = OrdersMethods().get_get_order_info()
        assert 200 == get_list[0]