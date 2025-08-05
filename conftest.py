from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--language", action='store', default='en',
                     help="Choose language: en, ru, es, fr, etc" )
    
@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption("language")

    option = Options()
    option.add_experimental_option('prefs',{'intl.accept_language': user_language} )

    browser = webdriver.Chrome(options=option)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
