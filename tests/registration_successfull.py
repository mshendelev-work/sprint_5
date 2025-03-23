from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site/')

# Ожидание отображения кнопки «Личный кабинет»
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, './/p'
                                                                                      '[text()="Личный Кабинет"]')))

# Переход к форме для входа
driver.find_element(By.XPATH, './/p[text()="Личный Кабинет"]').click()

# Ожидание отображения кнопки «Зарегистрироваться»
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, './/a'
                                                                                  '[text()="Зарегистрироваться"]')))

# Переход к форме регистрации (шаг 2)
driver.find_element(By.XPATH, './/a[text()="Зарегистрироваться"]').click()

# Ввод данных для регистрации
driver.find_element(By.XPATH, './/fieldset[@class="Auth_fieldset__1QzWN mb-6"][1]//input'
                                    '[@class="text input__textfield text_type_main-default"]').send_keys('Илон')


def test_register_user_email(get_random_email, driver):
    email_field = driver.find_element(
        By.XPATH,
        './/fieldset[@class="Auth_fieldset__1QzWN mb-6"][2]//input[@class="text input__textfield text_type_main-default"]'
    )
    email_field.send_keys(get_random_email)


def test_register_user_password(get_random_password, driver):
    password_field = driver.find_element(
        By.XPATH,
        './/fieldset[@class="Auth_fieldset__1QzWN mb-6"][3]//input[@class="text input__textfield text_type_main-default"]'
    )
    password_field.send_keys(get_random_password)


# Нажатие кнопки «Зарегистрироваться»
driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()

# Ожидание отображения формы для входа
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, './/button'
                                                                                  '[text()="Войти"]')))

# Проверка, что в url добавился /login
assert '/login' in driver.current_url

# Закрытие браузера
driver.quit()
