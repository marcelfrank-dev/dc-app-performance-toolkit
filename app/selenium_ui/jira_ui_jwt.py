import time

from extension.jira import extension_ui  # noqa F401
from selenium_ui.jira import modules
from selenium_ui.jira.pages.pages import JwtTestIssueView


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


# ----------------------- JWT ------------------------
def test_1_selenium_browse_jwt_test_issue_action(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.browse_jwt_test_issue(jira_webdriver)


def test_1_selenium_check_calc_field_value_action(jira_webdriver, jira_datasets, jira_screen_shots):
    jwt_test_issue_view_page = JwtTestIssueView(jira_webdriver)
    jwt_test_issue_view_page.check_calc_field_value()


def test_1_selenium_check_automation_rule_action(jira_webdriver, jira_datasets, jira_screen_shots):
    jwt_test_issue_view_page = JwtTestIssueView(jira_webdriver)
    jwt_test_issue_view_page.change_priority()
    # wait 2 seconds to be sure that the automation rule is executed
    time.sleep(2)
    jwt_test_issue_view_page.go_to()
    jwt_test_issue_view_page.check_automation_rule_changes()


def test_1_selenium_check_condition_hide_button_action(jira_webdriver, jira_datasets, jira_screen_shots):
    jwt_test_issue_view_page = JwtTestIssueView(jira_webdriver)
    jwt_test_issue_view_page.check_condition(0)


def test_1_selenium_check_condition_show_button_action(jira_webdriver, jira_datasets, jira_screen_shots):
    jwt_test_issue_view_page = JwtTestIssueView(jira_webdriver)
    jwt_test_issue_view_page.assign_to_me()
    jwt_test_issue_view_page.check_condition(1)


def test_1_selenium_check_validation_fail_action(jira_webdriver, jira_datasets, jira_screen_shots):
    jwt_test_issue_view_page = JwtTestIssueView(jira_webdriver)
    jwt_test_issue_view_page.execute_transition_without_change()
    jwt_test_issue_view_page.check_validator(0)
    jwt_test_issue_view_page.close_transition_screen()
    jwt_test_issue_view_page.go_to()


def test_1_selenium_check_validation_pass_action(jira_webdriver, jira_datasets, jira_screen_shots):
    jwt_test_issue_view_page = JwtTestIssueView(jira_webdriver)
    jwt_test_issue_view_page.execute_transition_with_change()
    jwt_test_issue_view_page.check_validator(1)
    jwt_test_issue_view_page.check_summary_value("JWT-Summary")


# this action should be the last one
def test_2_selenium_z_log_out(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.log_out(jira_webdriver, jira_datasets)
