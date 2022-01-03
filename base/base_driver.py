import time
class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)