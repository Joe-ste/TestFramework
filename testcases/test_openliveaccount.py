import pytest
from utilities.utils import Utils
from pages.acy_launch_page import LaunchPage
from ddt import ddt, data, unpack

@pytest.mark.usefixtures('setup')
class TestOpenAccount:

    @pytest.mark.parametrize('account_type,country,title,firstname,middlename,lastname,email,phone,areacode,code',
                             Utils.read_data_from_excel("C:\\TestFramework\\testdata\\testdata.xlsx", "personal_detail"))
    def test_personal_detail(self, account_type, country, title, firstname,
                             middlename, lastname, email, phone, areacode, code):

        # open https://acy.com/en/open-live-account
        page = LaunchPage(self.driver)
        # click X
        page.click_path()
        # select account type
        page.select_account_type(account_type)
        # select account type
        page.select_country(country)
        # select title
        page.select_title(title)
        # input first name
        page.input_first_name(firstname)
        # input middle name
        page.input_middle_name(middlename)
        # scroll the page
        #page.page_scroll()
        # input last name
        page.input_last_name(lastname)
        # input email
        page.input_email(email)
        # input phone number
        page.input_phone_number(phone)
        # select area code
        page.select_area_code(areacode)
        # click get code button
        page.click_get_code()
        # input mobile_authentication
        page.input_mobile_authentication(code)
        # click next button
        page.click_next()