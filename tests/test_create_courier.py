from methods.couriers_methods import *


@allure.feature("CreateCourier")
class TestsCreateCourier:

    @allure.title("Создание курьера")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_create_courier(self, return_correct_creds_for_new_courier):
        new_courier = CourierMethods(return_correct_creds_for_new_courier).post_create_courier()
        courier_id = CourierMethods(return_correct_creds_for_new_courier).post_login_courier()
        CourierMethods(return_correct_creds_for_new_courier).delete_courier(courier_id[1]["id"])
        with allure.step("Проверка статус кода после создания курьера"):
            assert new_courier[0] == 201

    @allure.title("Создание курьера с указанием уже использованных кредов")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_create_courier_with_already_used_creds(self, return_correct_creds_for_new_courier):
        CourierMethods(return_correct_creds_for_new_courier).post_create_courier()
        new_courier = CourierMethods(return_correct_creds_for_new_courier).post_create_courier()
        courier_id = CourierMethods(return_correct_creds_for_new_courier).post_login_courier()
        CourierMethods(return_correct_creds_for_new_courier).delete_courier(courier_id[1]["id"])
        with allure.step("Проверка, отображения корректного сообщения об ошибке"):
            assert "Этот логин уже используется. Попробуйте другой." in new_courier[1]

    @allure.title("Сообщение об успехе, после создания курьера")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_return_correct_successful_message(self, return_correct_creds_for_new_courier):
        new_courier = CourierMethods(return_correct_creds_for_new_courier).post_create_courier()
        courier_id = CourierMethods(return_correct_creds_for_new_courier).post_login_courier()
        CourierMethods(return_correct_creds_for_new_courier).delete_courier(courier_id[1]["id"])
        with allure.step("Проверка отображения сообщение об успехе после создания курьера вернулось "):
            assert new_courier[1] == '{"ok":true}'

    @allure.title("Создание курьера без передачи обязательного поля")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_create_courier_without_required_field(self, return_correct_creds_for_new_courier):
        del return_correct_creds_for_new_courier["password"]
        new_courier = CourierMethods(return_correct_creds_for_new_courier).post_create_courier()
        with allure.step("Проверка 400 статус кода после некорректного создания курьера"):
            assert new_courier[0] == 400

    @allure.title("409 статус код при создании курьера с указанием уже использованных кредов")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_return_correct_error_status_code(self):
        new_courier = requests.post(f"{BASE_URL}{CREATE_COURIER}", data=creds_of_an_already_created_courier)
        with allure.step("Проверка 409 статус кода после некорректного создания курьера"):
            assert new_courier.status_code == 409

    @allure.title("Создание курьера с указанием уже использовавшегося логина")
    @allure.link(BASE_URL, name="https://qa-scooter.praktikum-services.ru")
    def test_create_courier_with_already_used_login(self, return_correct_creds_for_new_courier):
        CourierMethods(return_correct_creds_for_new_courier).post_create_courier()
        return_correct_creds_for_new_courier["password"] = "12ada2eda23d2"
        return_correct_creds_for_new_courier["firstName"] = "223ada2eda23d2"
        new_courier = CourierMethods(return_correct_creds_for_new_courier).post_create_courier()
        with allure.step("Проверка 409 статус кода после некорректного создания курьера"):
            assert new_courier[0] == 409