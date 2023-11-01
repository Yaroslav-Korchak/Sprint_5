from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait

class TestAccountCredentials:
    name = "Yaroslav"
    email = "yaroslav_korchak_sun_555@yandex.ru"
    password = "123456"

    def test_go_to_account_unregistered(self, browser):
        # запускаем главную страницу
        browser.get("https://stellarburgers.nomoreparties.site")
        # Клик по кнопке "Личный кабинет"
        browser.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/login"))
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_go_to_account_registered(self, browser):
        # запускаем главную страницу
        browser.get("https://stellarburgers.nomoreparties.site")
        # нажатие по кнопке "Личный кабинет"
        browser.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/login"))
        # ввод учётных данных в соответствующие поля
        browser.find_element(*TestLocators.EMAIL).send_keys(TestAccountCredentials.email)
        browser.find_element(*TestLocators.PASSWORD).send_keys(TestAccountCredentials.password)
        # нажатие на кнопку 'Войти'
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        # Переход в личный кабинет
        browser.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/account/profile"))
        # открылся личный кабинет с заполненными полями
        browser.find_element(*TestLocators.ACCOUNT_LIST)
        assert browser.find_element(*TestLocators.LOGIN_FIELD).get_attribute("value") == "yaroslav_korchak_sun_555@yandex.ru"