import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield browser
    print("\nquit browser..")
    time.sleep(10)
    browser.quit()
