from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait


class TestAccountCredentials:
    name = "Yaroslav"
    email = "yaroslav_korchak_sun_555@yandex.ru"
    password = "123456"

    def test_open_constructor_from_personal_account_by_click_constructor(self, browser):
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

        # Переход в конструктор по клику на вкладку «Конструктор»
        browser.find_element(*TestLocators.CONSTRUCTOR_COLUMN).click()
        WebDriverWait(browser, 3).until_not(expected_conditions.url_contains("/account/profile"))
        # открылась страница с конструктором
        assert browser.find_element(*TestLocators.CHOOSE_BREAD).text == "Перетяните булочку сюда (верх)"
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_open_constructor_from_personal_account_by_click_logo(self, browser):
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
        # Переход в конструктор по клику на логотип бургеров
        browser.find_element(*TestLocators.LOGO).click()
        WebDriverWait(browser, 3).until_not(expected_conditions.url_contains("/account/profile"))
        # открылась страница с конструктором
        assert browser.find_element(*TestLocators.CHOOSE_BREAD).text == "Перетяните булочку сюда (верх)"
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"