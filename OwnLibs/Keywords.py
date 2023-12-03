import selenium
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def lib_explicit_wait(driver, locator, key_wait_time=10):
    wait = WebDriverWait(driver, key_wait_time)
    return wait.until(expected_conditions.visibility_of_element_located(locator))

def lib_click(driver, locator, wait=True, key_wait_time=10):
    if wait:
        lib_explicit_wait(driver, locator, key_wait_time)
    driver.find_element(*locator).click()

def lib_input_text(driver, locator, text, wait=True, key_wait_time=10):
    if wait:
        lib_explicit_wait(driver, locator, key_wait_time)
    driver.find_element(*locator).click()
    driver.find_element(*locator).send_keys(text)
