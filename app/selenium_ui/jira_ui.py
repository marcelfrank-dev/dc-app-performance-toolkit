from extension.jira import extension_ui  # noqa F401
from selenium_ui.conftest import print_timing
from selenium_ui.jira import modules
from selenium_ui.jira.pages.pages import AdminToolboxIssueTypeView, JwtTestIssueView, SumUpCalcRulesView, SumUpCalculationView, SumUpGlobalSettingsView, LastLogView


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


# ----------------------- SUM UP ------------------------
def test_1_selenium_browse_calculation_rules_view_action(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.browse_calc_rules_view(jira_webdriver)


def test_1_selenium_add_new_rule_action(jira_webdriver, jira_datasets, jira_screen_shots):
    calc_rules_view_page = SumUpCalcRulesView(jira_webdriver)
    calc_rules_view_page.add_new_rule()


def test_1_selenium_calculate_watcher_field_action(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.browse_calc_issues_view(jira_webdriver)
    calc_issues_view_page = SumUpCalculationView(jira_webdriver)
    calc_issues_view_page.switch_view_layout()
    calc_issues_view_page.add_watchers_field()
    calc_issues_view_page.go_to()
    calc_issues_view_page.calculate()
    calc_issues_view_page.go_to()
    calc_issues_view_page.remove_watchers_field()


def test_1_selenium_delete_new_rule_action(jira_webdriver, jira_datasets, jira_screen_shots):
    calc_rules_view_page = SumUpCalcRulesView(jira_webdriver)
    calc_rules_view_page.go_to()
    calc_rules_view_page.wait_for_page_loaded()
    calc_rules_view_page.delete_rule()


def test_1_selenium_browse_global_settings_view_action(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.browse_global_settings_view(jira_webdriver)


def test_1_selenium_deactivate_apps_action(jira_webdriver, jira_datasets, jira_screen_shots):
    global_settings_view_page = SumUpGlobalSettingsView(jira_webdriver)
    global_settings_view_page.deactivate_apps()


def test_1_selenium_activate_apps_action(jira_webdriver, jira_datasets, jira_screen_shots):
    global_settings_view_page = SumUpGlobalSettingsView(jira_webdriver)
    global_settings_view_page.activate_apps()


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


# ----------------------- JWT ------------------------
def test_1_selenium_browse_jwt_test_issue_action(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.browse_jwt_test_issue(jira_webdriver)


def test_1_selenium_check_calc_field_value_action(jira_webdriver, jira_datasets, jira_screen_shots):
    jwt_test_issue_view_page = JwtTestIssueView(jira_webdriver)
    jwt_test_issue_view_page.check_calc_field_value()


def test_1_selenium_check_automation_rule_action(jira_webdriver, jira_datasets, jira_screen_shots):
    jwt_test_issue_view_page = JwtTestIssueView(jira_webdriver)
    jwt_test_issue_view_page.change_priority()
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
