from methods.couriers_methods import *


@allure.feature("LoginCourier")
class TestsLoginCourier:

    @allure.title("Авторизация курьера")
    @allure.description("Авторизация курьера")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_login_courier(self, create_and_delete_courier):
        login_data = create_and_delete_courier.post_login_courier()
        assert 200 == login_data[0]

    @allure.title("404 статус код при указании не корректных пароля или логина")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_error_message_not_correct_login_or_password(self, create_and_delete_courier):
        true_login = create_and_delete_courier.courier_data["login"]
        create_and_delete_courier.courier_data["login"] = "213213123qwawd"
        info_with_not_true_login = create_and_delete_courier.post_login_courier()
        create_and_delete_courier.courier_data["login"] = true_login
        create_and_delete_courier.courier_data["password"] = "213213123qwawd"
        info_with_not_true_password = create_and_delete_courier.post_login_courier()
        assert [404, 404] == [info_with_not_true_login[0], info_with_not_true_password[0]]

    @allure.title("400 статус код при авторизации без указания пароля или логина")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_error_message_for_login_without_login_or_password_field(self, create_and_delete_courier):
        true_creds = create_and_delete_courier.courier_data
        create_and_delete_courier.courier_data["password"] = ""
        info_without_password_field = create_and_delete_courier.post_login_courier()
        create_and_delete_courier.courier_data = true_creds
        create_and_delete_courier.courier_data["login"] = ""
        info_without_login_field = create_and_delete_courier.post_create_courier()
        assert [400, 400] == [info_without_password_field[0], info_without_login_field[0]]

    @allure.title("404 статус код при авторизации с указанием незарегестрированных кредов")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_login_without_registration(self, return_correct_creds_for_new_courier):
        courier = CourierMethods(return_correct_creds_for_new_courier).post_login_courier()
        assert 404 == courier[0]

    @allure.title("Возвращается id после успешной авторизации")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_return_id_after_successful_login(self, create_and_delete_courier):
        login_data = create_and_delete_courier.post_login_courier()
        assert "id" in login_data[1]
