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

# ----------------------- LAST LOG ------------------------
def test_1_selenium_browse_last_log_view_action(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.browse_last_log_view_log(jira_webdriver)


def test_1_selenium_last_log_apply_filter_action(jira_webdriver, jira_datasets, jira_screen_shots):
    last_log_view_page = LastLogView(jira_webdriver)
    last_log_view_page.apply_filter()
    last_log_view_page.wait_for_loading()
    last_log_view_page.check_log_visibility()


def test_1_selenium_last_log_reload_action(jira_webdriver, jira_datasets, jira_screen_shots):
    last_log_view_page = LastLogView(jira_webdriver)
    last_log_view_page.reload()
    last_log_view_page.wait_for_loading()
    last_log_view_page.wait_for_loading()
    last_log_view_page.check_log_visibility()


# this action should be the last one
def test_2_selenium_z_log_out(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.log_out(jira_webdriver, jira_datasets)
