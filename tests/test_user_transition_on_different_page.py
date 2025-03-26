from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.constants import Constants
from src.locators import Locators


class TestUserTransitionPage:
    def test_personal_account_transition_constructor(self, driver):
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
        # Нажатие кнопки «Конструктор» в хедере
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR_ON_HEADER).click()
        # Ожидание отображения кнопки «Оформить заказ» на главной странице
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.BUTTON_ORDER_ON_HOME_PAGE))
        # Проверка, что пользователь находится на странице «Конструктор» (она же главная страница)
        assert driver.current_url == Constants.HOME_URL, 'User is not on HOME_URL'

    def test_personal_account_transition_in_button_stellar_burgers(self, driver):
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
        # Нажатие кнопки «Stellar Burgers» в хедере
        driver.find_element(*Locators.BUTTON_STELLAR_BURGERS_ON_HEADER).click()
        # Ожидание отображения кнопки «Оформить заказ» на главной странице
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.BUTTON_ORDER_ON_HOME_PAGE))
        # Проверка, что пользователь находится на странице «Конструктор» (она же главная страница)
        assert driver.current_url == Constants.HOME_URL, 'User is not on HOME_URL'

    def test_personal_account_transition_for_home_page(self, driver):
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