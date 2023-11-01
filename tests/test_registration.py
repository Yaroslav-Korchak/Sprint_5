from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators




class TestRegistration:

    def test_registration_with_correct_data_successful(self, browser, generate_login, generate_password):

        # открываем страницу регистрации
        browser.get("https://stellarburgers.nomoreparties.site/register")

        # заполняем поля валидными значениями
        browser.find_element(*TestLocators.NAME).send_keys("Маша")
        browser.find_element(*TestLocators.EMAIL).send_keys(generate_login + '@yandex.ru')
        browser.find_element(*TestLocators.PASSWORD).send_keys(generate_password)

        # нажать на кнопку "Зарегистрироваться"pytest -v
        browser.find_element(*TestLocators.REGISTR_BUTTON).click()

        # открылась страница логина
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/login"))
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_registration_without_name_failed(self, browser, generate_login, generate_password):


        # открываем страницу регистрации
        browser.get("https://stellarburgers.nomoreparties.site/register")

        # заполняем email и пароль
        browser.find_element(*TestLocators.EMAIL).send_keys(generate_login + '@yandex.ru')
        browser.find_element(*TestLocators.PASSWORD).send_keys(generate_password)

        # нажать на кнопку "Зарегистрироваться"
        browser.find_element(*TestLocators.REGISTR_BUTTON).click()

        # страница та же, поля email и пароль заполнены, поле имя - пустое
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/register"
        assert browser.find_element(*TestLocators.NAME).get_attribute("value") == ""
        assert browser.find_element(*TestLocators.EMAIL).get_attribute("value") == generate_login + "@yandex.ru"
        assert browser.find_element(*TestLocators.PASSWORD).get_attribute("value") == generate_password

    def test_registration_with_short_password_failed(self, browser, generate_login, generate_password):


        # открываем страницу регистрации
        browser.get("https://stellarburgers.nomoreparties.site/register")

        # заполняем поля кроме пароля валидными значениями
        browser.find_element(*TestLocators.NAME).send_keys("Маша")
        browser.find_element(*TestLocators.EMAIL).send_keys(generate_login + '@yandex.ru')
        generate_password = generate_password[:-3]
        browser.find_element(*TestLocators.PASSWORD).send_keys(generate_password)

        # нажать на кнопку "Зарегистрироваться"
        browser.find_element(*TestLocators.REGISTR_BUTTON).click()
        # ожидание появления сообщения об ошибке
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PASSWORD_ERROR))
        assert browser.find_element(*TestLocators.PASSWORD_ERROR).text == 'Некорректный пароль'


    def test_registration_with_bad_email_failed(self, browser, generate_login, generate_password):


        # открываем страницу регистрации
        browser.get("https://stellarburgers.nomoreparties.site/register")

        # заполняем поля кроме пароля валидными значениями
        browser.find_element(*TestLocators.NAME).send_keys("Маша")
        browser.find_element(*TestLocators.EMAIL).send_keys(generate_login)
        browser.find_element(*TestLocators.PASSWORD).send_keys(generate_password)

        # нажать на кнопку "Зарегистрироваться"
        browser.find_element(*TestLocators.REGISTR_BUTTON).click()
        # ожидание появления сообщения об ошибке
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.EMAIL_ERROR))
        assert browser.find_element(*TestLocators.EMAIL_ERROR).text == 'Такой пользователь уже существует'
