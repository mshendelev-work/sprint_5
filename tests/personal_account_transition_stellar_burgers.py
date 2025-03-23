from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site/')

# Ожидание отображения кнопки «Войти в аккаунт»
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, './/button'
                                                                                      '[text()="Войти в аккаунт"]')))

# Нажатие кнопки «Войти в аккаунт»
driver.find_element(By.XPATH, './/button[text()="Войти в аккаунт"]').click()

# Ожидание отображения формы «Вход»
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, './/h2'
                                                                                  '[text()="Вход"]')))

# Ввод email
driver.find_element(By.XPATH, './/fieldset[@class="Auth_fieldset__1QzWN mb-6"][1]//input'
                        '[@class="text input__textfield text_type_main-default"]').send_keys('shendelev_19@gmail.com')

# Ввод пароля
driver.find_element(By.XPATH, './/fieldset[@class="Auth_fieldset__1QzWN mb-6"][2]//input'
                        '[@class="text input__textfield text_type_main-default"]').send_keys('yandex_practicum')

# Нажатие кнопки «Войти»
driver.find_element(By.XPATH, './/button[text()="Войти"]').click()

# Ожидание отображения кнопки «Личный Кабинет»
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, './/p'
                                                                                      '[text()="Личный Кабинет"]')))

# Нажатие кнопки «Личный Кабинет»
driver.find_element(By.XPATH, './/p[text()="Личный Кабинет"]').click()

# Ожидание отображения кнопки «Профиль»
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, './/a'
                                                                                      '[text()="Профиль"]')))

# Проверка, что пользователь находится на странице «Личный Кабинет»
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

# Нажатие кнопки «Stellar Burgers»
driver.find_element(By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]').click()

# Ожидание отображения кнопки «Оформить заказ»
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, './/button'
                                                                                      '[text()="Оформить заказ"]')))

# Проверка, что пользователь находится на странице «Конструктор»
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

# Закрытие браузера
driver.quit()
