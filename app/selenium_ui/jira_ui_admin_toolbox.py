from extension.jira import extension_ui  # noqa F401
from selenium_ui.conftest import print_timing
from selenium_ui.jira import modules
from selenium_ui.jira.pages.pages import AdminToolboxIssueTypeView, JwtTestIssueView, SumUpCalcRulesView, SumUpCalculationView, SumUpGlobalSettingsView, LastLogView


# this action should be the first one
# ----------------------- ADMIN MODE ------------------------
def test_0_selenium_a_login(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.adminLogin(jira_webdriver)


"""
Add custom actions anywhere between login and log out action. Move this to a different line as needed.
Write your custom selenium scripts in `app/extension/jira/extension_ui.py`.
Refer to `app/selenium_ui/jira/modules.py` for examples.
"""
# def test_1_selenium_custom_action(jira_webdriver, jira_datasets, jira_screen_shots):
#     extension_ui.app_specific_action(jira_webdriver, jira_datasets)


# ----------------------- ADMIN TOOLBOX ------------------------
def test_1_selenium_browse_issue_types_view_action(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.browse_admin_toolbox_issue_types_view(jira_webdriver)


def test_1_selenium_check_show_hide_id_column_action(jira_webdriver, jira_datasets, jira_screen_shots):
    admin_toolbox_issue_type_view_page = AdminToolboxIssueTypeView(jira_webdriver)
    admin_toolbox_issue_type_view_page.check_id_column_visibility(1)
    admin_toolbox_issue_type_view_page.deactivate_show_hide_id_column()
    admin_toolbox_issue_type_view_page.check_id_column_visibility(0)
    admin_toolbox_issue_type_view_page.activate_show_hide_id_column()
    admin_toolbox_issue_type_view_page.check_id_column_visibility(1)


def test_1_selenium_check_smart_view_action(jira_webdriver, jira_datasets, jira_screen_shots):
    admin_toolbox_issue_type_view_page = AdminToolboxIssueTypeView(jira_webdriver)
    admin_toolbox_issue_type_view_page.check_smart_view_visibility(0)
    admin_toolbox_issue_type_view_page.activate_smart_view()
    admin_toolbox_issue_type_view_page.check_smart_view_visibility(1)
    admin_toolbox_issue_type_view_page.deactivate_smart_view()
    admin_toolbox_issue_type_view_page.check_smart_view_visibility(0)


def test_1_selenium_filter_by_name_action(jira_webdriver, jira_datasets, jira_screen_shots):
    admin_toolbox_issue_type_view_page = AdminToolboxIssueTypeView(jira_webdriver)
    admin_toolbox_issue_type_view_page.check_deactivated_name_filter_result()
    admin_toolbox_issue_type_view_page.set_name_filter()
    admin_toolbox_issue_type_view_page.check_activated_name_filter_result()


def test_1_selenium_clear_filter_action(jira_webdriver, jira_datasets, jira_screen_shots):
    admin_toolbox_issue_type_view_page = AdminToolboxIssueTypeView(jira_webdriver)
    admin_toolbox_issue_type_view_page.click_reset_filter_button()
    admin_toolbox_issue_type_view_page.check_deactivated_name_filter_result()


# this action should be the last one
def test_2_selenium_z_log_out(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.log_out(jira_webdriver, jira_datasets)
