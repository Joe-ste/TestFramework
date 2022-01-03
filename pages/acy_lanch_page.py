import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class LanchPage(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def click_path(self):
        path = self.wait.until(
            EC.element_to_be_clickable((By.TAG_NAME, 'path')))
        path.click()

    def open_account(self):
        open_account_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="button open-account body-bold"]')))
        open_account_button.click()

    def select_account_type(self, account_type):
        account_type_select = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="entity"]')))
        account_type_select.click()
        account_types = self.driver.find_elements(By.XPATH, "//li[contains(@data-testid,'entity')]")
        for li in account_types:
            if li.text == account_type:
                li.click()

    def select_country(self, country):
        countrys_select = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="country"]')))
        countrys_select.click()
        countrys = self.driver.find_elements(By.XPATH, "//li[contains(@data-testid,'country')]")
        for li in countrys:
            if li.text == country:
                li.click()
        time.sleep(10)

    def select_title(self, title):
        title_select = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="title"]')))
        title_select.click()
        titles = self.driver.find_elements(By.XPATH, "//li[contains(@data-testid,'title')]")
        for li in titles:
            if li.text == title:
                li.click()

    def input_first_name(self, firstname):
        first_name_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="firstname"]')))
        first_name_input.send_keys(firstname)

    def input_middle_name(self, middlename):
        middle_name_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="middlename"]')))
        middle_name_input.send_keys(middlename)

    def input_last_name(self, lastname):
        last_name_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="lastname"]')))
        last_name_input.send_keys(lastname)

    def input_email(self, email):
        email_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="email"]')))
        email_input.send_keys(email)

    def select_and_input_phone(self, local_number, phone_number):
        phone_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="phone"]')))
        phone_input.send_keys(phone_number)
        local_numbers = self.driver.find_elements(By.XPATH, "//li[contains(@data-testid,'undifined')]")
        for li in local_numbers:
            if li.text == local_number:
                li.click()

        time.sleep(5)

    def get_and_input_mobile_authentication(self, code):
        code_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Get Code"]')))
        code_button.click()
        code_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="code"]')))
        code_input.send_keys(code)
        time.sleep(5)

    def click_next(self):
        code_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data_testid="submit"]')))
        code_button.click()
        time.sleep(5)
