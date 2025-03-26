from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.constants import Constants
from src.locators import Locators


class TestUserLogout:
    def test_logout_from_personal_account_page(self, driver):
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
        # Ожидание отображения кнопки «Личный Кабинет» на главной странице
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE))
        # Нажатие кнопки «Личный Кабинет» на главной странице
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE).click()
        # Ожидание отображения кнопки «Профиль» на странице личного кабинета
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.BUTTON_PROFILE_ON_PERSONAL_ACCOUNT_PAGE))
        # Проверка, что пользователь находится на странице личного кабинета
        assert driver.current_url == Constants.PERSONAL_ACCOUNT_PAGE
        # Нажатие кнопки «Выход» на странице личного кабинета
        driver.find_element(*Locators.BUTTON_EXIT_ON_PERSONAL_ACCOUNT_PAGE).click()
        # Ожидание отображения кнопки «Войти» на странице авторизации
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.BUTTON_LOGIN_ON_LOGIN_PAGE))
        # Проверка, что пользователь находится на странице авторизации
        assert driver.current_url == Constants.LOGIN_URL, 'User is not on LOGIN_URL'
