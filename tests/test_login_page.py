from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import time

#
class TestAccountCredentials:
    name = "Yaroslav"
    email = "yaroslav_korchak_sun_555@yandex.ru"
    password = "123456"


    def test_login_through_personal_account_button(self, browser):
        # запускаем главную страницу
        browser.get("https://stellarburgers.nomoreparties.site")

        # нажатие на кнопку 'Личный кабинет'
        browser.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        # ввод учётных данных в соответствующие поля
        browser.find_element(*TestLocators.EMAIL).send_keys(TestAccountCredentials.email)
        browser.find_element(*TestLocators.PASSWORD).send_keys(TestAccountCredentials.password)
        # нажатие на кнопку 'Войти'
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        # ни один из других методов ожидания не срабатывает, поэтому оставил здесь time.sleep
        time.sleep(2)
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_by_button_through_enter_account_button(self, browser):
        # запускаем главную страницу
        browser.get("https://stellarburgers.nomoreparties.site")
        # Клик по кнопке «Войти в аккаунт»
        browser.find_element(*TestLocators.ENTER_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/login"))
        # ввод учётных данных в соответствующие поля
        browser.find_element(*TestLocators.EMAIL).send_keys(TestAccountCredentials.email)
        browser.find_element(*TestLocators.PASSWORD).send_keys(TestAccountCredentials.password)
        # нажатие на кнопку 'Войти'
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_through_registration_form(self, browser):
        # Открыть страницу регистрации
        browser.get("https://stellarburgers.nomoreparties.site/register")
        # Нажать на кнопку "Войти"
        browser.find_element(*TestLocators.ENTER_LINK_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/login"))
        # ввод учётных данных в соответствующие поля
        browser.find_element(*TestLocators.EMAIL).send_keys(TestAccountCredentials.email)
        browser.find_element(*TestLocators.PASSWORD).send_keys(TestAccountCredentials.password)
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_through_password_recovery_form(self, browser):
        # запускаем главную страницу
        browser.get("https://stellarburgers.nomoreparties.site")
        # нажатие на кнопку 'Личный кабинет'
        browser.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        # переход на страницу 'Восстановить пароль'
        browser.find_element(*TestLocators.FORGOT_PASSWORD).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/forgot-password"))
        # нажать на кнопку 'Войти'
        browser.find_element(*TestLocators.ENTER_LINK_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/login"))
        # ввод учётных данных в соответствующие поля
        browser.find_element(*TestLocators.EMAIL).send_keys(TestAccountCredentials.email)
        browser.find_element(*TestLocators.PASSWORD).send_keys(TestAccountCredentials.password)
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"

