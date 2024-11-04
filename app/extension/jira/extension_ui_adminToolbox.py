from selenium_ui.base_page import BasePage
from selenium_ui.jira import modules

from selenium_ui.jira.pages.pages import AdminToolboxIssueTypeView


# ----------------------- ADMIN TOOLBOX ------------------------

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

    def test_9_selenium_browse_issue_types_view_action(webdriver, jira_datasets):
        modules.browse_admin_toolbox_issue_types_view(webdriver)

    test_9_selenium_browse_issue_types_view_action(webdriver, datasets)

    def test_10_selenium_check_show_hide_id_column_action(webdriver, jira_datasets):
        admin_toolbox_issue_type_view_page = AdminToolboxIssueTypeView(webdriver)
        admin_toolbox_issue_type_view_page.check_id_column_visibility(1)
        admin_toolbox_issue_type_view_page.deactivate_show_hide_id_column()
        admin_toolbox_issue_type_view_page.check_id_column_visibility(0)
        admin_toolbox_issue_type_view_page.activate_show_hide_id_column()
        admin_toolbox_issue_type_view_page.check_id_column_visibility(1)

    test_10_selenium_check_show_hide_id_column_action(webdriver, datasets)

    def test_20_selenium_check_smart_view_action(webdriver, jira_datasets):
        admin_toolbox_issue_type_view_page = AdminToolboxIssueTypeView(webdriver)
        admin_toolbox_issue_type_view_page.check_smart_view_visibility(0)
        admin_toolbox_issue_type_view_page.activate_smart_view()
        admin_toolbox_issue_type_view_page.check_smart_view_visibility(1)
        admin_toolbox_issue_type_view_page.deactivate_smart_view()
        admin_toolbox_issue_type_view_page.check_smart_view_visibility(0)

    test_20_selenium_check_smart_view_action(webdriver, datasets)

    def test_30_selenium_filter_by_name_action(webdriver, jira_datasets):
        admin_toolbox_issue_type_view_page = AdminToolboxIssueTypeView(webdriver)
        admin_toolbox_issue_type_view_page.check_deactivated_name_filter_result()
        admin_toolbox_issue_type_view_page.set_name_filter()
        admin_toolbox_issue_type_view_page.check_activated_name_filter_result()

    test_30_selenium_filter_by_name_action(webdriver, datasets)

    def test_40_selenium_clear_filter_action(webdriver, jira_datasets):
        admin_toolbox_issue_type_view_page = AdminToolboxIssueTypeView(webdriver)
        admin_toolbox_issue_type_view_page.click_reset_filter_button()
        admin_toolbox_issue_type_view_page.check_deactivated_name_filter_result()

    test_40_selenium_clear_filter_action(webdriver, datasets)
