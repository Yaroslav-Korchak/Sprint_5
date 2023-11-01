import pytest
from selenium import webdriver
import random
import string



@pytest.fixture(scope='function')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def generate_login():
    characters = string.ascii_lowercase
    login = ''.join(random.choice(characters) for _ in range(8))
    return login

@pytest.fixture(scope='function')
def generate_password():
    characters = string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(8))
    return password





