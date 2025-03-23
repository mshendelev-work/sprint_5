from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site/')

# Ожидание отображения таблицы «Соберите бургер»
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, './/h1'
                                                                                      '[text()="Соберите бургер"]')))

# Нажатие кнопки «Начинки»
driver.find_element(By.XPATH, './/span[text()="Начинки"]').click()

# Ожидание отображения категории «Начинки»
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, './/h2'
                                                                                      '[text()="Начинки"]')))

# Нажатие кнопки «Соусы»
driver.find_element(By.XPATH, './/span[text()="Соусы"]').click()

# Ожидание отображения категории «Соусы»
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, './/h2'
                                                                                      '[text()="Соусы"]')))

# Нажатие кнопки «Булки»
driver.find_element(By.XPATH, './/span[text()="Булки"]').click()

# Ожидание отображения категории «Булки»
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, './/h2'
                                                                                      '[text()="Булки"]')))

# Закрытие браузера
driver.quit()
