from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver:

    def __init__(self, driver):
        self.driver = driver


    def page_scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_for_being_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element_to_click = wait.until(
            EC.element_to_be_clickable((locator_type, locator))
        )
        return element_to_click

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(
            EC.presence_of_all_elements_located((locator_type, locator))
        )
        return list_of_elements