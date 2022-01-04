
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    PATH = 'path'
    ACOUNT_TYPE = '//div[@data-testid="entity"]'
    COUNTRY = '//div[@data-testid="country"]'
    TITLE = '//div[@data-testid="title"]'
    FIRST_NAME = '//input[@data-testid="firstname"]'
    MIDDLE_NAME = '//input[@data-testid="middlename"]'
    LAST_NAME = '//input[@data-testid="lastname"]'
    EMAIL = '//input[@data-testid="email"]'
    AREA_CODE = '//div[@class="MuiBox-root jss118 jss50 undefined"]'
    PHONE = '//input[@data-testid="phone"]'
    MOBILE_AUTHENTICATION = '//input[@data-testid="code"]'
    GET_CODE_BUTTON = '//button[text()="Get Code"]'
    NEXT_BUTTON = '//button[@data-testid="submit"]'
    CLOSE_BUTTON = '//button[text()="Close"]'
    ALL_ACCOUNT_TYPES = '//li[contains(@data-testid,"entity")]'
    ALL_COUNTRYS = '//li[contains(@data-testid,"country")]'
    ALL_TITLES = '//li[contains(@data-testid,"title")]'
    ALL_AREA_CODE = '//li[contains(@data-testid,"undefined")]'

    # get elements
    def getPath(self):
        return self.wait_for_being_clickable(By.TAG_NAME, self.PATH)

    def getAcountType(self):
        return self.wait_for_being_clickable(By.XPATH, self.ACOUNT_TYPE)

    def getCountry(self):
        return self.wait_for_being_clickable(By.XPATH, self.COUNTRY)

    def getTitle(self):
        return self.wait_for_being_clickable(By.XPATH, self.TITLE)

    def getFirstName(self):
        return self.wait_for_being_clickable(By.XPATH, self.FIRST_NAME)

    def getMiddleName(self):
        return self.wait_for_being_clickable(By.XPATH, self.MIDDLE_NAME)

    def getLastName(self):
        return self.wait_for_being_clickable(By.XPATH, self.LAST_NAME)

    def getEmail(self):
        return self.wait_for_being_clickable(By.XPATH, self.EMAIL)

    def getAreaCode(self):
        return self.wait_for_being_clickable(By.XPATH, self.AREA_CODE)

    def getPhone(self):
        return self.wait_for_being_clickable(By.XPATH, self.PHONE)

    def getMobileAuthentication(self):
        return self.wait_for_being_clickable(By.XPATH, self.MOBILE_AUTHENTICATION)

    def getAllAcount(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ALL_ACCOUNT_TYPES)

    def getAllCountry(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ALL_COUNTRYS)

    def getAllTitle(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ALL_TITLES)

    def getAllAreaCode(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ALL_AREA_CODE)

    def getGetCodeButton(self):
        return self.wait_for_being_clickable(By.XPATH, self.GET_CODE_BUTTON)

    def getNextButton(self):
        return self.wait_for_being_clickable(By.XPATH, self.NEXT_BUTTON)

    def getCloseButton(self):
        return self.wait_for_being_clickable(By.XPATH, self.CLOSE_BUTTON)

    # action
    def click_path(self):
        self.getPath().click()

    def select_account_type(self, account_type):
        self.getAcountType().click()
        all_account_types = self.getAllAcount()
        for li in all_account_types:
            if li.text == account_type:
                li.click()
                break

    def select_country(self, country):
        self.getCountry().click()
        all_countrys = self.getAllCountry()
        for li in all_countrys:
            if li.text == country:
                li.click()
                break

    def select_title(self, title):
        self.getTitle().click()
        all_titles = self.getAllTitle()
        for li in all_titles:
            if li.text == title:
                li.click()
                break

    def input_first_name(self, firstname):
        self.getFirstName().send_keys(firstname)

    def input_middle_name(self, middlename):
        self.getMiddleName().send_keys(middlename)

    def input_last_name(self, lastname):
        self.getLastName().send_keys(lastname)

    def input_email(self, email):
        self.getEmail().send_keys(email)

    def select_area_code(self, area_code):
        self.getAreaCode().click()
        all_area_code = self.getAllAreaCode()
        for li in all_area_code:
            if li.text == area_code:
                li.click()
                break

    def input_phone_number(self, phone_number):
        self.getPhone().send_keys(phone_number)

    def click_get_code(self):
        self.getGetCodeButton().click()
        self.getCloseButton().click()

    def input_mobile_authentication(self, code):
        self.getMobileAuthentication().send_keys(code)

    def click_next(self):
        self.getNextButton().click()

    #def input_personal_detail(self, **kwargs):

