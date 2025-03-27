import pytest
from selenium import webdriver
from src.constants import Constants


# Запуск и закрытие драйвера
@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get(Constants.HOME_URL)
    yield chrome
    chrome.quit()
