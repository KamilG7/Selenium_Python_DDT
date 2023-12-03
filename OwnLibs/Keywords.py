import selenium
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


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


def lib_is_displayed(driver, locator, wait=True, key_wait_time=10):
    if wait:
        lib_explicit_wait(driver, locator, key_wait_time)
    driver.find_element(*locator).is_displayed()


def lib_get_text(driver, locator, wait=True, key_wait_time=10):
    if wait:
        lib_explicit_wait(driver, locator, key_wait_time)
    msg = driver.find_element(*locator).text
    return msg
