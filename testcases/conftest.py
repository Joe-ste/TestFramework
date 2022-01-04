import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get('https://acy.com/en/open-live-account')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    print('close')
    driver.close()
