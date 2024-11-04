import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS
from selenium_ui.jira import modules
from selenium_ui.jira.pages.pages import SumUpCalcRulesView, SumUpCalculationView, SumUpGlobalSettingsView

from selenium_ui.jira.pages.pages import PopupManager


# ----------------------- SUM UP ------------------------

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

    def test_10_selenium_browse_calculation_rules_view_action(webdriver, datasets):
        modules.browse_calc_rules_view(webdriver)

    test_10_selenium_browse_calculation_rules_view_action(webdriver, datasets)

    def test_20_selenium_add_new_rule_action(webdriver, datasets):
        calc_rules_view_page = SumUpCalcRulesView(webdriver)
        calc_rules_view_page.add_new_rule()

    test_20_selenium_add_new_rule_action(webdriver, datasets)

    def test_30_selenium_calculate_watcher_field_action(webdriver, datasets):
        modules.browse_calc_issues_view(webdriver)
        calc_issues_view_page = SumUpCalculationView(webdriver)
        calc_issues_view_page.switch_view_layout()
        calc_issues_view_page.add_watchers_field()
        calc_issues_view_page.go_to()
        calc_issues_view_page.calculate()
        calc_issues_view_page.go_to()
        calc_issues_view_page.remove_watchers_field()

    test_30_selenium_calculate_watcher_field_action(webdriver, datasets)

    def test_40_selenium_delete_new_rule_action(webdriver, datasets):
        calc_rules_view_page = SumUpCalcRulesView(webdriver)
        calc_rules_view_page.go_to()
        calc_rules_view_page.wait_for_page_loaded()
        calc_rules_view_page.delete_rule()

    test_40_selenium_delete_new_rule_action(webdriver, datasets)

    def test_50_selenium_browse_global_settings_view_action(webdriver, datasets):
        modules.browse_global_settings_view(webdriver)

    test_50_selenium_browse_global_settings_view_action(webdriver, datasets)

    def test_60_selenium_deactivate_apps_action(webdriver, datasets):
        global_settings_view_page = SumUpGlobalSettingsView(webdriver)
        global_settings_view_page.deactivate_apps()

    test_60_selenium_deactivate_apps_action(webdriver, datasets)

    def test_70_selenium_activate_apps_action(webdriver, datasets):
        global_settings_view_page = SumUpGlobalSettingsView(webdriver)
        global_settings_view_page.activate_apps()

    test_70_selenium_activate_apps_action(webdriver, datasets)
