from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.constants import Constants
from src.locators import Locators


class TestUserLogin:
    def test_login_from_home_page(self, driver):
        # Ожидание отображения кнопки «Войти в аккаунт» на главной странице
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.BUTTON_LOGIN_ON_HOME_PAGE))
        # Нажатие кнопки «Войти в аккаунт» на главной странице
        driver.find_element(*Locators.BUTTON_LOGIN_ON_HOME_PAGE).click()
        # Ожидание отображения текста «Вход» на странице авторизации
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.TEXT_ENTER_ON_LOGIN_PAGE))
        # Ввод email на странице авторизации
        driver.find_element(*Locators.INPUT_NAME_ON_REGISTRATION_PAGE).send_keys(Constants.BASIC_USER_DATA.get(
            'email'))
        # Ввод пароля на странице авторизации
        driver.find_element(*Locators.INPUT_EMAIL_ON_REGISTRATION_PAGE).send_keys(Constants.BASIC_USER_DATA.get(
            'password'))
        # Нажатие кнопки «Войти» на странице авторизации
        driver.find_element(*Locators.BUTTON_LOGIN_ON_LOGIN_PAGE).click()
        # Ожидание отображения кнопки «Оформить заказ» на главной странице
        order_button = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.BUTTON_ORDER_ON_HOME_PAGE))
        # Проверка, что кнопка «Оформить заказ» отображается на главной странице
        assert order_button.is_displayed() is True, 'Button is not displayed'
        assert order_button.is_enabled() is True, 'Button is not enabled'

    def test_login_in_button_my_account(self, driver):
        # Ожидание отображения кнопки «Личный Кабинет» на главной странице
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE))
        # Нажатие кнопки «Личный Кабинет» на главной странице
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE).click()
        # Ожидание отображения текста «Вход» на странице авторизации
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.TEXT_ENTER_ON_LOGIN_PAGE))
        # Ввод email на странице авторизации
        driver.find_element(*Locators.INPUT_NAME_ON_REGISTRATION_PAGE).send_keys(Constants.BASIC_USER_DATA.get(
            'email'))
        # Ввод пароля на странице авторизации
        driver.find_element(*Locators.INPUT_EMAIL_ON_REGISTRATION_PAGE).send_keys(Constants.BASIC_USER_DATA.get(
            'password'))
        # Нажатие кнопки «Войти» на странице авторизации
        driver.find_element(*Locators.BUTTON_LOGIN_ON_LOGIN_PAGE).click()
        # Ожидание отображения кнопки «Оформить заказ» на главной странице
        order_button = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.BUTTON_ORDER_ON_HOME_PAGE))
        # Проверка, что кнопка «Оформить заказ» отображается на главной странице
        assert order_button.is_displayed() is True, 'Button is not displayed'
        assert order_button.is_enabled() is True, 'Button is not enabled'

    def test_login_from_registration_page(self, driver):
        # Открытие страницы регистрации
        driver.get(Constants.REGISTRATION_URL)
        # Ожидание отображения кнопки «Войти» на странице регистрации
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.BUTTON_LOGIN_ON_REGISTRATION_PAGE))
        # Нажатие кнопки «Войти» на странице регистрации
        driver.find_element(*Locators.BUTTON_LOGIN_ON_REGISTRATION_PAGE).click()
        # Ожидание отображения текста «Вход» на странице авторизации
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.TEXT_ENTER_ON_LOGIN_PAGE))
        # Ввод email на странице авторизации
        driver.find_element(*Locators.INPUT_NAME_ON_REGISTRATION_PAGE).send_keys(Constants.BASIC_USER_DATA.get(
            'email'))
        # Ввод пароля на странице авторизации
        driver.find_element(*Locators.INPUT_EMAIL_ON_REGISTRATION_PAGE).send_keys(Constants.BASIC_USER_DATA.get(
            'password'))
        # Нажатие кнопки «Войти» на странице авторизации
        driver.find_element(*Locators.BUTTON_LOGIN_ON_LOGIN_PAGE).click()
        # Ожидание отображения кнопки «Оформить заказ» на главной странице
        order_button = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.BUTTON_ORDER_ON_HOME_PAGE))
        # Проверка, что кнопка «Оформить заказ» отображается на главной странице
        assert order_button.is_displayed() is True, 'Button is not displayed'
        assert order_button.is_enabled() is True, 'Button is not enabled'

    def test_login_from_recovery_password_page(self, driver):
        # Открытие страницы восстановления пароля
        driver.get(Constants.RECOVERY_PASSWORD_URL)
        # Ожидание отображения кнопки «Войти» на странице восстановления пароля
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.BUTTON_LOGIN_ON_RECOVERY_PASSWORD_PAGE))
        # Нажатие кнопки «Войти» на странице восстановления пароля
        driver.find_element(*Locators.BUTTON_LOGIN_ON_RECOVERY_PASSWORD_PAGE).click()
        # Ожидание отображения текста «Вход» на странице авторизации
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.TEXT_ENTER_ON_LOGIN_PAGE))
        # Ввод email на странице авторизации
        driver.find_element(*Locators.INPUT_NAME_ON_REGISTRATION_PAGE).send_keys(Constants.BASIC_USER_DATA.get(
            'email'))
        # Ввод пароля на странице авторизации
        driver.find_element(*Locators.INPUT_EMAIL_ON_REGISTRATION_PAGE).send_keys(Constants.BASIC_USER_DATA.get(
            'password'))
        # Нажатие кнопки «Войти» на странице авторизации
        driver.find_element(*Locators.BUTTON_LOGIN_ON_LOGIN_PAGE).click()
        # Ожидание отображения кнопки «Оформить заказ» на главной странице
        order_button = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.BUTTON_ORDER_ON_HOME_PAGE))
        # Проверка, что кнопка «Оформить заказ» отображается на главной странице
        assert order_button.is_displayed() is True, 'Button is not displayed'
        assert order_button.is_enabled() is True, 'Button is not enabled'
