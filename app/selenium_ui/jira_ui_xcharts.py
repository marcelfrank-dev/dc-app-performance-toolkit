from extension.jira import extension_ui  # noqa F401
from selenium_ui.jira import modules

from selenium_ui.jira.pages.pages import XChartsResourcesView, XChartsDataScriptsView, PopupManager


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


# ----------------------- xCharts ------------------------
def test_1_selenium_add_java_script_resource_action(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.xcharts_add_js_ressource(jira_webdriver)



def test_1_selenium_add_css_script_resource_action(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.xcharts_add_css_ressource(jira_webdriver)

def test_1_selenium_add_data_script_action(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.xcharts_add_data_script(jira_webdriver)
    xcharts_data_script_page = XChartsDataScriptsView(jira_webdriver)
    xcharts_data_script_page.go_to()
    xcharts_data_script_page.wait_for_page_loaded()
    PopupManager(jira_webdriver).dismiss_default_popup()
    xcharts_data_script_page.click_create_script_button()
    xcharts_data_script_page.set_script_name("Data Script name")
    xcharts_data_script_page.set_script_description("Data Script description")
    xcharts_data_script_page.set_example()
    xcharts_data_script_page.add_script()
    xcharts_data_script_page.set_jql_parameter()
    xcharts_data_script_page.run_preview()
    xcharts_data_script_page.save_and_close_script()
    xcharts_data_script_page.check_script_data("Data Script name", "Data Script description", "Default Layout")
    xcharts_data_script_page.delete_first_script()
    xcharts_data_script_page.check_empty_resource_table()


# this action should be the last one
def test_2_selenium_z_log_out(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.log_out(jira_webdriver, jira_datasets)
