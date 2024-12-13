from methods.order_methods import *
import allure


class TestGetOrder:

    @allure.title("Возвращается объект")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_successful_return_object(self):
        new_order = OrdersMethods()
        new_order_info = new_order.post_create_order()
        order_info = new_order.get_get_order_info(new_order_info[2]["track"])
        assert "order" in order_info[2]

    @allure.title("Отображается сообщение об ошибке после запроса без id")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_error_message_after_request_without_track_id(self):
        new_order = requests.get(f"https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=")
        assert "Недостаточно данных для поиска" in new_order.json()["message"]

    @allure.title("Отображается сообщение об ошибке после запроса c некорректным id")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_error_message_after_request_with_not_correct_track_id(self):
        new_order = requests.get(f"https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=9999999")
        assert "Заказ не найден" in new_order.json()["message"]