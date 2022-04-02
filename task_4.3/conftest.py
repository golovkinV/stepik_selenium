import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language:")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    language = request.config.getoption('language')
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    time.sleep(10)
    yield browser