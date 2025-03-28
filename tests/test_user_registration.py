from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.constants import Constants
from src.locators import Locators


class TestRegistrations:
    def test_registration_correct_data(self, driver):
        # Ожидание отображения кнопки «Личный кабинет»
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE))
        # Переход к странице авторизации
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE).click()
        # Ожидание отображения кнопки Регистрации на странице авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_REGISTRATION_ON_LOGIN_PAGE))
        # Переход к странице регистрации
        driver.find_element(*Locators.BUTTON_REGISTRATION_ON_LOGIN_PAGE).click()
        # Ввод данных в поле «Имя» на странице регистрации
        driver.find_element(*Locators.INPUT_NAME_ON_REGISTRATION_PAGE).send_keys(Constants.CORRECT_USER_DATA.get(
            'name'))
        # Ввод данных в поле «Email» на странице регистрации
        driver.find_element(*Locators.INPUT_EMAIL_ON_REGISTRATION_PAGE).send_keys(Constants.CORRECT_USER_DATA.get(
            'email'))
        # Ввод данных в поле «Пароль» на странице регистрации
        driver.find_element(*Locators.INPUT_PASSWORD_ON_REGISTRATION_PAGE).send_keys(Constants.CORRECT_USER_DATA.get(
            'password'))
        # Нажатие кнопки «Зарегистрироваться» на странице регистрации
        driver.find_element(*Locators.BUTTON_REGISTRATION_ON_REGISTRATION_PAGE).click()
        # Ожидание отображения страницы для авторизации
        login_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_LOGIN_ON_LOGIN_PAGE))
        # Проверка, что кнопка «Войти» отображается на странице авторизации
        assert login_button.is_displayed() is True, 'Button is not displayed'
        assert login_button.is_enabled() is True, 'Button is not enabled'

    def test_registration_incorrect_password(self, driver):
        # Ожидание отображения кнопки «Личный кабинет» на главной странице
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE))
        # Переход к странице авторизации
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE).click()
        # Ожидание отображения кнопки Регистрации на странице авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_REGISTRATION_ON_LOGIN_PAGE))
        # Переход к странице регистрации
        driver.find_element(*Locators.BUTTON_REGISTRATION_ON_LOGIN_PAGE).click()
        # Ввод данных в поле «Имя» на странице регистрации
        driver.find_element(*Locators.INPUT_NAME_ON_REGISTRATION_PAGE).send_keys(
            Constants.INCORRECT_USER_PASSWORD.get('name'))
        # Ввод данных в поле «Email» на странице регистрации
        driver.find_element(*Locators.INPUT_EMAIL_ON_REGISTRATION_PAGE).send_keys(
            Constants.INCORRECT_USER_PASSWORD.get('email'))
        # Ввод данных в поле «Пароль» на странице регистрации
        driver.find_element(*Locators.INPUT_PASSWORD_ON_REGISTRATION_PAGE).send_keys(
            Constants.INCORRECT_USER_PASSWORD.get('password'))
        # Нажатие кнопки «Зарегистрироваться»
        driver.find_element(*Locators.BUTTON_REGISTRATION_ON_REGISTRATION_PAGE).click()
        # Ожидание плейсхолдера указывающего на некорректный пароль на странице регистрации
        placeholder = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.PLACEHOLDER_INCORRECT_PASSWORD))
        # Проверка, что плейсхолдер "Некорректный пароль" отображается на странице регистрации
        assert placeholder.is_displayed() is True, 'Placeholder is not displayed'
        assert placeholder.is_enabled() is True, 'Placeholder is not enabled'
