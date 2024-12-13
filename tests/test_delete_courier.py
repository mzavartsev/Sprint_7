from methods.couriers_methods import *


class TestDeleteCourier:

    @allure.title("Отображается корректное сообщение об ошибке")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_error_message_after_unsuccessful_request(self):
        delete_courier = requests.delete(f"{BASE_URL}/api/v1/courier/9999999")
        assert delete_courier.status_code == 404

    @allure.title("Отображается корректное сообщение успеха")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_return_correct_successful_message(self, create_courier):
        new_courier = create_courier.post_login_courier()
        id = new_courier[1]["id"]
        delete_courier = create_courier.delete_courier(id)
        assert delete_courier[1] == '{"ok":true}'

    @allure.title("Отображается корректное сообщение об ошибке")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_return_error_message_after_delete_without_required_field(self):
        delete_courier = requests.delete(f"{BASE_URL}/api/v1/courier/")
        assert delete_courier.status_code == 404

