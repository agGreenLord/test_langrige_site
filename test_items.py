from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_buy_button(browser, request):
    browser.get(f'http://selenium1py.pythonanywhere.com/{request.config.getoption("language")}/catalogue/coders-at-work_207/')
    assert WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))), "Кнопка не отображается"
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    button.click()
    time.sleep(5)
    assert WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.alertinner'))), 'Кнопка не прожалась '

