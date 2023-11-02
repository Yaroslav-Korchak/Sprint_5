from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import helpers
import data


class TestRegistration:

    def test_registration_with_correct_data_successful(self, browser):

        # открываем страницу регистрации
        browser.get("https://stellarburgers.nomoreparties.site/register")
        browser.find_element(*TestLocators.NAME).send_keys(data.name)
        browser.find_element(*TestLocators.EMAIL).send_keys(helpers.generate_login() + '@yandex.ru')
        browser.find_element(*TestLocators.PASSWORD).send_keys(helpers.generate_password())
        browser.find_element(*TestLocators.REGISTR_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/login"))
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_registration_without_name_failed(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/register")
        email = helpers.generate_login() + '@yandex.ru'
        password = helpers.generate_password()
        browser.find_element(*TestLocators.EMAIL).send_keys(email)
        browser.find_element(*TestLocators.PASSWORD).send_keys(password)
        browser.find_element(*TestLocators.REGISTR_BUTTON).click()
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/register"
        assert browser.find_element(*TestLocators.NAME).get_attribute("value") == ""
        assert browser.find_element(*TestLocators.EMAIL).get_attribute("value") == email
        assert browser.find_element(*TestLocators.PASSWORD).get_attribute("value") == password

    def test_registration_with_short_password_failed(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/register")
        browser.find_element(*TestLocators.NAME).send_keys("Маша")
        browser.find_element(*TestLocators.EMAIL).send_keys(helpers.generate_login() + '@yandex.ru')
        password = helpers.generate_password()[:-3]
        browser.find_element(*TestLocators.PASSWORD).send_keys(password)
        browser.find_element(*TestLocators.REGISTR_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PASSWORD_ERROR))
        assert browser.find_element(*TestLocators.PASSWORD_ERROR).text == 'Некорректный пароль'

    def test_registration_with_bad_email_failed(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/register")
        # заполняем поля кроме пароля валидными значениями
        browser.find_element(*TestLocators.NAME).send_keys("Маша")
        browser.find_element(*TestLocators.EMAIL).send_keys(helpers.generate_login())
        browser.find_element(*TestLocators.PASSWORD).send_keys(helpers.generate_password())
        browser.find_element(*TestLocators.REGISTR_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.EMAIL_ERROR))
        assert browser.find_element(*TestLocators.EMAIL_ERROR).text == 'Такой пользователь уже существует'
