from extension.jira import extension_ui  # noqa F401
from selenium_ui.jira import modules
from selenium_ui.jira.pages.pages import SumUpCalcRulesView, SumUpCalculationView, SumUpGlobalSettingsView


# this action should be the first one
def test_0_selenium_a_login(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.login(jira_webdriver, jira_datasets)


def test_1_selenium_browse_projects_list(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.browse_projects_list(jira_webdriver, jira_datasets)


def test_1_selenium_browse_boards_list(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.browse_boards_list(jira_webdriver, jira_datasets)


def test_1_selenium_create_issue(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.create_issue(jira_webdriver, jira_datasets)


def test_1_selenium_edit_issue(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.edit_issue(jira_webdriver, jira_datasets)


def test_1_selenium_save_comment(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.save_comment(jira_webdriver, jira_datasets)


def test_1_selenium_search_jql(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.search_jql(jira_webdriver, jira_datasets)


def test_1_selenium_view_backlog_for_scrum_board(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.view_backlog_for_scrum_board(jira_webdriver, jira_datasets)


def test_1_selenium_view_scrum_board(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.view_scrum_board(jira_webdriver, jira_datasets)


def test_1_selenium_view_kanban_board(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.view_kanban_board(jira_webdriver, jira_datasets)


def test_1_selenium_view_dashboard(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.view_dashboard(jira_webdriver, jira_datasets)


def test_1_selenium_view_issue(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.view_issue(jira_webdriver, jira_datasets)


def test_1_selenium_view_project_summary(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.view_project_summary(jira_webdriver, jira_datasets)


"""
Add custom actions anywhere between login and log out action. Move this to a different line as needed.
Write your custom selenium scripts in `app/extension/jira/extension_ui.py`.
Refer to `app/selenium_ui/jira/modules.py` for examples.
"""


# def test_1_selenium_custom_action(jira_webdriver, jira_datasets, jira_screen_shots):
#     extension_ui.app_specific_action(jira_webdriver, jira_datasets)


# ----------------------- ADMIN MODE ------------------------
def test_1_selenium_a_login(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.adminLogin(jira_webdriver)


# ----------------------- SUM UP ------------------------
def test_10_selenium_browse_calculation_rules_view_action(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.browse_calc_rules_view(jira_webdriver)


def test_20_selenium_add_new_rule_action(jira_webdriver, jira_datasets, jira_screen_shots):
    calc_rules_view_page = SumUpCalcRulesView(jira_webdriver)
    calc_rules_view_page.add_new_rule()


def test_30_selenium_calculate_watcher_field_action(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.browse_calc_issues_view(jira_webdriver)
    calc_issues_view_page = SumUpCalculationView(jira_webdriver)
    calc_issues_view_page.switch_view_layout()
    calc_issues_view_page.add_watchers_field()
    calc_issues_view_page.go_to()
    calc_issues_view_page.calculate()
    calc_issues_view_page.go_to()
    calc_issues_view_page.remove_watchers_field()


def test_40_selenium_delete_new_rule_action(jira_webdriver, jira_datasets, jira_screen_shots):
    calc_rules_view_page = SumUpCalcRulesView(jira_webdriver)
    calc_rules_view_page.go_to()
    calc_rules_view_page.wait_for_page_loaded()
    calc_rules_view_page.delete_rule()


def test_50_selenium_browse_global_settings_view_action(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.browse_global_settings_view(jira_webdriver)


def test_60_selenium_deactivate_apps_action(jira_webdriver, jira_datasets, jira_screen_shots):
    global_settings_view_page = SumUpGlobalSettingsView(jira_webdriver)
    global_settings_view_page.deactivate_apps()


def test_70_selenium_activate_apps_action(jira_webdriver, jira_datasets, jira_screen_shots):
    global_settings_view_page = SumUpGlobalSettingsView(jira_webdriver)
    global_settings_view_page.activate_apps()


# this action should be the last one
def test_999_selenium_z_log_out(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.log_out(jira_webdriver, jira_datasets)
