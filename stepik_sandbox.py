from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import math
import os
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    browser.get(link)

    wait = WebDriverWait(browser, 12)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # browser.execute_script("window.scrollTo(0,100)")
    browser.find_element(By.ID, "book").click()

    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    # browser.switch_to.alert.accept()

    el_x = browser.find_element(By.ID, "input_value")
    x = el_x.text
    y = calc(x)
    #
    browser.find_element(By.ID, "answer").send_keys(y)
    # browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    #
    # browser.find_element(By.NAME, "lastname").send_keys("Lol")
    #
    # browser.find_element(By.NAME, "email").send_keys("lol@yandex.ru")
    #
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # test_path = os.path.join(current_dir, "test.txt")
    # print(test_path)
    # browser.find_element(By.ID, "file").send_keys(test_path)

    browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
