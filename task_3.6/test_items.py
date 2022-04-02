from selenium.webdriver.common.by import By
import time


def test_page_contains_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form button")
    assert 'page does not contains add to cart button'