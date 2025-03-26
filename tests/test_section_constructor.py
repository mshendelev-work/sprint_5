from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.constants import Constants
from src.locators import Locators


class TestSectionConstructor:
    def test_transition_on_section_constructor(self, driver):
        # Ожидание отображения таблицы «Соберите бургер»
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.NAME_TABLE_ASSEMBLE_BURGERS_ON_CONSTRUCTION_PAGE))
        # Нажатие кнопки «Начинки» на странице «Конструктор» (она же главная страница)
        driver.find_element(*Locators.BUTTON_STUFFING_ON_CONSTRUCTION_PAGE).click()
        # Ожидание отображения категории «Начинки» на странице «Конструктор» (она же главная страница)
        category_stuffing = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.NAME_CATEGORY_STUFFING_ON_CONSTRUCTION_PAGE))
        assert category_stuffing.is_displayed() is True, 'Stuffing is not displayed'
        assert category_stuffing.is_enabled() is True, 'Stuffing is not enabled'
        # Нажатие кнопки «Соусы» на странице «Конструктор» (она же главная страница)
        driver.find_element(*Locators.BUTTON_SAUCES_ON_CONSTRUCTION_PAGE).click()
        # Ожидание отображения категории «Соусы» на странице «Конструктор» (она же главная страница)
        category_sauces = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.NAME_CATEGORY_SAUCES_ON_CONSTRUCTION_PAGE))
        assert category_sauces.is_displayed() is True, 'Sauces is not displayed'
        assert category_sauces.is_enabled() is True, 'Sauces is not enabled'
        # Нажатие кнопки «Булки» на странице «Конструктор» (она же главная страница)
        driver.find_element(*Locators.BUTTON_BUNS_ON_CONSTRUCTION_PAGE).click()
        # Ожидание отображения категории «Булки» на странице «Конструктор» (она же главная страница)
        category_buns = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.NAME_BUNS_SAUCES_ON_CONSTRUCTION_PAGE))
        assert category_buns.is_displayed() is True, 'Buns is not displayed'
        assert category_buns.is_enabled() is True, 'Buns is not enabled'
