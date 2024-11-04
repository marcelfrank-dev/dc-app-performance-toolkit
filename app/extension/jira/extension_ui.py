import time

from selenium_ui.base_page import BasePage
from selenium_ui.jira import modules
from selenium_ui.jira.pages.pages import JwtTestIssueView


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

    # ----------------------- JWT ------------------------
    def test_10_selenium_browse_jwt_test_issue_action(webdriver, datasets):
        modules.browse_jwt_test_issue(webdriver)

    test_10_selenium_browse_jwt_test_issue_action(webdriver, datasets)

    def test_11_selenium_check_calc_field_value_action(webdriver, datasets):
        jwt_test_issue_view_page = JwtTestIssueView(webdriver)
        jwt_test_issue_view_page.go_to()
        jwt_test_issue_view_page.check_calc_field_value()

    test_11_selenium_check_calc_field_value_action(webdriver, datasets)

    def test_12_selenium_check_automation_rule_action(webdriver, datasets):
        jwt_test_issue_view_page = JwtTestIssueView(webdriver)
        jwt_test_issue_view_page.go_to()
        jwt_test_issue_view_page.change_priority()
        # wait 4 seconds to be sure that the automation rule is executed
        time.sleep(4)
        jwt_test_issue_view_page.go_to()
        jwt_test_issue_view_page.check_automation_rule_changes()

    test_12_selenium_check_automation_rule_action(webdriver, datasets)

    def test_13_selenium_check_condition_hide_button_action(webdriver, datasets):
        jwt_test_issue_view_page = JwtTestIssueView(webdriver)
        jwt_test_issue_view_page.go_to()
        jwt_test_issue_view_page.check_condition(0)

    test_13_selenium_check_condition_hide_button_action(webdriver, datasets)

    def test_14_selenium_check_condition_show_button_action(webdriver, datasets):
        jwt_test_issue_view_page = JwtTestIssueView(webdriver)
        jwt_test_issue_view_page.go_to()
        jwt_test_issue_view_page.assign_to_me()
        jwt_test_issue_view_page.check_condition(1)

    test_14_selenium_check_condition_show_button_action(webdriver, datasets)

    def test_15_selenium_check_validation_fail_action(webdriver, datasets):
        jwt_test_issue_view_page = JwtTestIssueView(webdriver)
        jwt_test_issue_view_page.go_to()
        jwt_test_issue_view_page.execute_transition_without_change()
        jwt_test_issue_view_page.check_validator(0)
        jwt_test_issue_view_page.close_transition_screen()
        jwt_test_issue_view_page.go_to()

    test_15_selenium_check_validation_fail_action(webdriver, datasets)

    def test_16_selenium_check_validation_pass_action(webdriver, datasets):
        jwt_test_issue_view_page = JwtTestIssueView(webdriver)
        jwt_test_issue_view_page.go_to()
        jwt_test_issue_view_page.execute_transition_with_change()
        jwt_test_issue_view_page.check_validator(1)
        jwt_test_issue_view_page.check_summary_value("JWT-Summary")

    test_16_selenium_check_validation_pass_action(webdriver, datasets)
