from selenium_ui.base_page import BasePage
from selenium_ui.jira import modules

from selenium_ui.jira.pages.pages import AdminToolboxIssueTypeView


# ----------------------- XCHARTS ------------------------

def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out action
    #
    # @print_timing("selenium_app_specific_user_login")
    # def measure():
    #     def app_specific_user_login(username='admin', password='admin'):
    #         login_page = Login(webdriver)
    #         login_page.delete_all_cookies()
    #         login_page.go_to()
    #         login_page.set_credentials(username=username, password=password)
    #         if login_page.is_first_login():
    #             login_page.first_login_setup()
    #         if login_page.is_first_login_second_page():
    #             login_page.first_login_second_page_setup()
    #         login_page.wait_for_page_loaded()
    #     app_specific_user_login(username='admin', password='admin')
    # measure()

    # ----------------------- ADMIN MODE ------------------------
    def test_1_selenium_a_login(webdriver, datasets):
        modules.adminLogin(webdriver)

    test_1_selenium_a_login(webdriver, datasets)

    def test_10_selenium_open_default_chart(webdriver, datasets):
        modules.xcharts_open_default_chart(webdriver)

    test_10_selenium_open_default_chart(webdriver, datasets)


