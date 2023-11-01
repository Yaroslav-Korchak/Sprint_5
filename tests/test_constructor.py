from locators import TestLocators

def test_constructor_select_sause(browser):

    # запускаем главную страницу
    browser.get("https://stellarburgers.nomoreparties.site")
    # кликнуть на соусы
    browser.find_element(*TestLocators.SAUCES_BUTTON).click()
    is_active = browser.find_element(*TestLocators.SAUCES_BUTTON).get_attribute('class')
    assert 'current' in is_active

def test_constructor_select_bread(browser):

    # запускаем главную страницу
    browser.get("https://stellarburgers.nomoreparties.site")
    # кликнуть на соус
    browser.find_element(*TestLocators.SAUCES_BUTTON).click()
    # кликнуть на булки
    browser.find_element(*TestLocators.BREAD_BUTTON).click()
    is_active = browser.find_element(*TestLocators.BREAD_BUTTON).get_attribute('class')
    assert 'current' in is_active

def test_constructor_select_fillings(browser):
    # запускаем главную страницу
    browser.get("https://stellarburgers.nomoreparties.site")
    # кликнуть на начинки
    browser.find_element(*TestLocators.FILLINGS_BUTTON).click()
    is_active = browser.find_element(*TestLocators.FILLINGS_BUTTON).get_attribute('class')
    assert 'current' in is_active
