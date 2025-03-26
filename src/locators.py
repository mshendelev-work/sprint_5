from selenium.webdriver.common.by import By


class Locators:
    BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE = \
        By.XPATH, './/p[text()="Личный Кабинет"]' # Кнопка «Личный кабинет» на главной странице
    BUTTON_REGISTRATION_ON_LOGIN_PAGE = \
        By.XPATH, './/a[text()="Зарегистрироваться"]' # Кнопка регистрации на странице авторизации
    INPUT_NAME_ON_REGISTRATION_PAGE = By.XPATH, '''.//fieldset[@class="Auth_fieldset__1QzWN mb-6"][1]//input
        [@class="text input__textfield text_type_main-default"]''' # Поле «Имя» на странице регистрации
    INPUT_EMAIL_ON_REGISTRATION_PAGE = By.XPATH, '''.//fieldset[@class="Auth_fieldset__1QzWN mb-6"][2]//input
        [@class="text input__textfield text_type_main-default"]''' # Поле «Email» на странице регистрации
    INPUT_PASSWORD_ON_REGISTRATION_PAGE = By.XPATH, '''.//fieldset[@class="Auth_fieldset__1QzWN mb-6"][3]//input
        [@class="text input__textfield text_type_main-default"]''' # Поле «Пароль» на странице регистрации
    BUTTON_REGISTRATION_ON_REGISTRATION_PAGE = \
        By.XPATH, './/button[text()="Зарегистрироваться"]' # Кнопка «Зарегистрироваться» на странице регистрации
    BUTTON_LOGIN_ON_LOGIN_PAGE = \
        By.XPATH, './/button[text()="Войти"]' # Кнопка «Войти» на странице авторизации
    PLACEHOLDER_INCORRECT_PASSWORD = \
        By.XPATH, './/p[text()="Некорректный пароль"]' # Плейсхолдер "Некорректный пароль" на странице регистрации
    BUTTON_LOGIN_ON_HOME_PAGE = \
        By.XPATH, './/button[text()="Войти в аккаунт"]' # Кнопка «Войти в аккаунт» на главной странице
    TEXT_ENTER_ON_LOGIN_PAGE = By.XPATH, './/h2[text()="Вход"]' # Надпись «Вход» на странице авторизации
    BUTTON_ORDER_ON_HOME_PAGE = \
        By.XPATH, './/button[text()="Оформить заказ"]' # Кнопка «Оформить заказ» на главной странице
    BUTTON_LOGIN_ON_REGISTRATION_PAGE = By.XPATH, './/a[text()="Войти"]' # Кнопка «Войти» на странице регистрации
    BUTTON_LOGIN_ON_RECOVERY_PASSWORD_PAGE = \
        By.XPATH, './/a[text()="Войти"]' # Кнопка «Войти» на странице восстановления пароля
    BUTTON_PROFILE_ON_PERSONAL_ACCOUNT_PAGE = \
        By.XPATH, './/a[text()="Профиль"]' # Кнопка «Профиль» на странице личного кабинета
    BUTTON_EXIT_ON_PERSONAL_ACCOUNT_PAGE = \
        By.XPATH, './/button[text()="Выход"]' # Кнопка «Выход» на странице личного кабинета
    BUTTON_CONSTRUCTOR_ON_HEADER = \
        By.XPATH, './/p[text()="Конструктор"]' # Кнопка «Конструктор» в хедере
    BUTTON_STELLAR_BURGERS_ON_HEADER = \
        By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]'  # Кнопка «Stellar Burgers» в хедере
    NAME_TABLE_ASSEMBLE_BURGERS_ON_CONSTRUCTION_PAGE = \
        By.XPATH, './/h1[text()="Соберите бургер"]' # Название таблицы «Соберите бургер» на странице «Конструктор»
    BUTTON_STUFFING_ON_CONSTRUCTION_PAGE = \
        By.XPATH, './/span[text()="Начинки"]' # Кнопка «Начинки» на странице «Конструктор» (она же главная страница)
    NAME_CATEGORY_STUFFING_ON_CONSTRUCTION_PAGE = \
        By.XPATH, './/h2[text()="Начинки"]' # Наименование категории «Начинки» на странице «Конструктор»
    BUTTON_SAUCES_ON_CONSTRUCTION_PAGE = \
        By.XPATH, './/span[text()="Соусы"]' # Кнопка «Соусы» на странице «Конструктор» (она же главная страница)
    NAME_CATEGORY_SAUCES_ON_CONSTRUCTION_PAGE = \
        By.XPATH, './/h2[text()="Соусы"]' # Наименование категории «Соусы» на странице «Конструктор»
    BUTTON_BUNS_ON_CONSTRUCTION_PAGE = \
        By.XPATH, './/span[text()="Булки"]' # Кнопка «Булки» на странице «Конструктор» (она же главная страница)
    NAME_BUNS_SAUCES_ON_CONSTRUCTION_PAGE = \
        By.XPATH, './/h2[text()="Булки"]' # Наименование категории «Булки» на странице «Конструктор»