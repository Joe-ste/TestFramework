import pytest
from pages.acy_lanch_page import LanchPage

@pytest.mark.usefixtures('setup')
class TestOpenAccount:

    def test_personal_detail(self):

        # open https://acy.com/en/open-live-account
        page = LanchPage(self.driver, self.wait)
        # click path
        #page.click_path()
        # select account type
        page.select_account_type('Personal')
        # select account type
        page.select_country('China')
        # select title
        page.select_title('Mr')
        # input first name
        page.input_first_name('k')
        # input middle name
        page.input_middle_name('k')
        # scroll the page
        page.page_scroll()
        # input last name
        page.input_last_name('k')
        # input email
        page.input_email('k@k.com')
        # input and select phone number
        page.select_and_input_phone('Taiwan +886', '0910519034')
        # input mobile_authentication
        page.get_and_input_mobile_authentication('0')
        # click next
        page.click_next()