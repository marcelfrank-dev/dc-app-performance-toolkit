import json
import random
import time

from selenium.webdriver.common.keys import Keys

from selenium_ui.base_page import BasePage
from selenium_ui.jira.pages.selectors import UrlManager, LoginPageLocators, DashboardLocators, PopupLocators, \
    IssueLocators, ProjectLocators, SearchLocators, BoardsListLocators, BoardLocators, LogoutLocators, LastLogViewLocators, SumUpLocators, JwtTestIssueViewLocators, AdminToolboxViewLocators, \
    XChartsResourcesViewLocators, XChartsDataScriptsViewLocators


class PopupManager(BasePage):

    def dismiss_default_popup(self):
        return self.dismiss_popup(PopupLocators.default_popup, PopupLocators.popup_1, PopupLocators.popup_2)


class Login(BasePage):
    page_url = LoginPageLocators.login_url
    page_loaded_selector = LoginPageLocators.system_dashboard

    def is_first_login(self):
        return True if self.get_elements(LoginPageLocators.continue_button) else False

    def first_login_setup(self):
        self.wait_until_visible(LoginPageLocators.continue_button).send_keys(Keys.ESCAPE)
        self.get_element(LoginPageLocators.continue_button).click()
        self.wait_until_visible(LoginPageLocators.avatar_page_next_button).click()
        self.wait_until_visible(LoginPageLocators.explore_current_projects).click()
        self.go_to_url(DashboardLocators.dashboard_url)
        self.wait_until_visible(DashboardLocators.dashboard_window)

    def set_credentials(self, username, password):
        self.get_element(LoginPageLocators.login_field).send_keys(username)
        self.get_element(LoginPageLocators.password_field).send_keys(password)
        self.get_element(LoginPageLocators.login_submit_button).click()


class AdminLogin(BasePage):
    page_url = LoginPageLocators.admin_login_url
    page_loaded_selector = LoginPageLocators.system_settings

    def is_first_login(self):
        return True if self.get_elements(LoginPageLocators.continue_button) else False

    def set_credentials(self, username, password):
        self.get_element(LoginPageLocators.login_field).send_keys(username)
        self.get_element(LoginPageLocators.password_field).send_keys(password)
        self.get_element(LoginPageLocators.login_submit_button).click()


class SecureLogin(BasePage):
    page_loaded_selector = LoginPageLocators.secure_login

    def set_credentials(self):
        self.get_element(LoginPageLocators.secure_password_field).send_keys("admin")
        self.get_element(LoginPageLocators.login_submit_button).click()


class Logout(BasePage):
    page_url = LogoutLocators.logout_url

    def click_logout(self):
        self.get_element(LogoutLocators.logout_submit_button).click()

    def wait_for_page_loaded(self):
        self.wait_until_present(LogoutLocators.login_button_link)


class Dashboard(BasePage):
    page_url = DashboardLocators.dashboard_url

    def wait_dashboard_presented(self):
        self.wait_until_present(DashboardLocators.dashboard_window)


class Issue(BasePage):
    page_loaded_selector = IssueLocators.issue_title

    def __init__(self, driver, issue_key=None, issue_id=None):
        BasePage.__init__(self, driver)
        url_manager_modal = UrlManager(issue_key=issue_key)
        url_manager_edit_page = UrlManager(issue_id=issue_id)
        self.page_url = url_manager_modal.issue_url()
        self.page_url_edit_issue = url_manager_edit_page.edit_issue_url()
        self.page_url_edit_comment = url_manager_edit_page.edit_comments_url()

    def wait_for_issue_title(self):
        self.wait_until_visible(IssueLocators.issue_title)

    def go_to_edit_issue(self):
        self.go_to_url(self.page_url_edit_issue)
        self.wait_until_visible(IssueLocators.edit_issue_page)

    def go_to_edit_comment(self):
        self.go_to_url(self.page_url_edit_comment)
        self.wait_until_visible(IssueLocators.edit_comment_add_comment_button)

    def fill_summary_edit(self):
        text_summary = f"Edit summary form selenium - {self.generate_random_string(10)}"
        self.get_element(IssueLocators.issue_summary_field).send_keys(text_summary)

    def __fill_rich_editor_textfield(self, text, selector):
        self.wait_until_available_to_switch(selector)
        self.get_element(IssueLocators.tinymce_description_field).send_keys(text)
        self.return_to_parent_frame()

    def __fill_textfield(self, text, selector):
        self.get_element(selector).send_keys(text)

    def edit_issue_submit(self):
        self.get_element(IssueLocators.edit_issue_submit).click()

    def fill_description_edit(self, rte):
        text_description = f"Edit description form selenium - {self.generate_random_string(100)}"
        if rte:
            self.__fill_rich_editor_textfield(text_description, selector=IssueLocators.issue_description_field_RTE)
        else:
            self.__fill_textfield(text_description, selector=IssueLocators.issue_description_field)

    def open_create_issue_modal(self):
        self.wait_until_clickable(IssueLocators.create_issue_button).click()
        self.wait_until_visible(IssueLocators.issue_modal)

    def fill_description_create(self, rte):
        text_description = f'Description: {self.generate_random_string(100)}'
        if rte:
            self.__fill_rich_editor_textfield(text_description, selector=IssueLocators.issue_description_field_RTE)
        else:
            self.__fill_textfield(text_description, selector=IssueLocators.issue_description_field)

    def fill_summary_create(self):
        summary = f"Issue created date {time.time()}"
        self.wait_until_clickable(IssueLocators.issue_summary_field).send_keys(summary)

    def assign_to_me(self):
        assign_to_me_links = self.get_elements(IssueLocators.issue_assign_to_me_link)
        for link in assign_to_me_links:
            link.click()

    def set_resolution(self):
        resolution_field = self.get_elements(IssueLocators.issue_resolution_field)
        if resolution_field:
            drop_down_length = len(self.select(resolution_field[0]).options)
            random_resolution_id = random.randint(1, drop_down_length - 1)
            self.select(resolution_field[0]).select_by_index(random_resolution_id)

    def set_issue_type(self):
        def __filer_epic(element):
            return "epic" not in element.get_attribute("class").lower()

        issue_types = {}
        data_suggestions = json.loads(self.get_element(IssueLocators.issue_types_options)
                                      .get_attribute('data-suggestions'))
        for data in data_suggestions:
            # 'Please select' is label in items list where all issue types are presented (not for current project)
            if 'Please select' not in str(data):
                items = data['items']
                for label in items:
                    if label['label'] not in issue_types:
                        issue_types[label['label']] = label['selected']
        if 'Epic' in issue_types:
            if issue_types['Epic']:
                # Do in case of 'Epic' issue type is selected
                self.action_chains().move_to_element(self.get_element(IssueLocators.issue_type_field))
                self.get_element(IssueLocators.issue_type_field).click()
                issue_dropdown_elements = self.get_elements(IssueLocators.issue_type_dropdown_elements)
                if issue_dropdown_elements:
                    filtered_issue_elements = list(filter(__filer_epic, issue_dropdown_elements))
                    rnd_issue_type_el = random.choice(filtered_issue_elements)
                    self.action_chains().move_to_element(rnd_issue_type_el).click(rnd_issue_type_el).perform()
                self.wait_until_invisible(IssueLocators.issue_ready_to_save_spinner)

    def submit_issue(self):
        self.wait_until_clickable(IssueLocators.issue_submit_button).click()
        self.wait_until_invisible(IssueLocators.issue_modal)

    def fill_comment_edit(self, rte):
        text = 'Comment from selenium'
        if rte:
            self.__fill_rich_editor_textfield(text, selector=IssueLocators.edit_comment_text_field_RTE)
        else:
            self.__fill_textfield(text, selector=IssueLocators.edit_comment_text_field)

    def edit_comment_submit(self):
        self.get_element(IssueLocators.edit_comment_add_comment_button).click()
        self.wait_until_visible(IssueLocators.issue_title)


class Project(BasePage):
    page_loaded_selector = ProjectLocators.project_summary_property_column

    def __init__(self, driver, project_key):
        BasePage.__init__(self, driver)
        url_manager = UrlManager(project_key=project_key)
        self.page_url = url_manager.project_summary_url()


class ProjectsList(BasePage):

    def __init__(self, driver, projects_list_pages):
        BasePage.__init__(self, driver)
        self.projects_list_page = random.randint(1, projects_list_pages)
        url_manager = UrlManager(projects_list_page=self.projects_list_page)
        self.page_url = url_manager.projects_list_page_url()

    def wait_for_page_loaded(self):
        self.wait_until_any_ec_presented(
            selector_names=[ProjectLocators.projects_list, ProjectLocators.projects_not_found])


class BoardsList(BasePage):
    page_url = BoardsListLocators.boards_list_url
    page_loaded_selector = BoardsListLocators.boards_list


class JwtTestIssueView(BasePage):
    page_url = JwtTestIssueViewLocators.jwt_test_issue_view_url
    page_loaded_selector = JwtTestIssueViewLocators.summary

    def click_transition(self):
        self.wait_until_visible(JwtTestIssueViewLocators.transition_button, 10)
        self.get_element(JwtTestIssueViewLocators.transition_button).click()
        self.wait_until_visible(JwtTestIssueViewLocators.issue_updated_flag, 10)
        self.get_element(JwtTestIssueViewLocators.issue_updated_flag_close_button).click()
        self.wait_until_invisible(JwtTestIssueViewLocators.issue_updated_flag)

    def check_calc_field_value(self):
        self.wait_until_visible(JwtTestIssueViewLocators.calc_field_value, 10)
        assert "1" in self.get_element(JwtTestIssueViewLocators.calc_field_value).text

    def change_priority(self):
        self.get_element(JwtTestIssueViewLocators.priority_button).click()
        self.wait_until_visible(JwtTestIssueViewLocators.first_priority_option, 10)
        self.get_element(JwtTestIssueViewLocators.first_priority_option).click()
        self.wait_until_visible(JwtTestIssueViewLocators.submit_priority_button, 10)
        self.get_element(JwtTestIssueViewLocators.submit_priority_button).click()
        self.wait_until_visible(JwtTestIssueViewLocators.priority_select_loading, 10)
        self.wait_until_invisible(JwtTestIssueViewLocators.priority_select_loading)

    def check_automation_rule_changes(self):
        self.wait_until_visible(JwtTestIssueViewLocators.assignee, 10)
        assert "Unassigned" in self.get_element(JwtTestIssueViewLocators.assignee).text.strip()
        self.check_summary_value("Changed by Automation rule")

    def assign_to_me(self):
        self.wait_until_visible(JwtTestIssueViewLocators.assign_to_me_button, 10)
        self.get_element(JwtTestIssueViewLocators.assign_to_me_button).click()
        self.wait_until_visible(JwtTestIssueViewLocators.issue_updated_flag, 10)
        self.get_element(JwtTestIssueViewLocators.issue_updated_flag_close_button).click()
        self.wait_until_invisible(JwtTestIssueViewLocators.issue_updated_flag)

    def check_condition(self, visible):
        if visible:
            self.wait_until_visible(JwtTestIssueViewLocators.transition_button)
        else:
            self.wait_until_invisible(JwtTestIssueViewLocators.transition_button)

    def check_validator(self, passed):
        if passed:
            self.wait_until_invisible(JwtTestIssueViewLocators.transition_screen_error)
        else:
            self.wait_until_visible(JwtTestIssueViewLocators.transition_screen_error)

    def close_transition_screen(self):
        self.get_element(JwtTestIssueViewLocators.transition_screen_cancel_button).click()

    def execute_transition_without_change(self):
        self.wait_until_visible(JwtTestIssueViewLocators.transition_button, 10)
        self.get_element(JwtTestIssueViewLocators.transition_button).click()
        self.wait_until_visible(JwtTestIssueViewLocators.transition_screen_submit_button, 10)
        self.get_element(JwtTestIssueViewLocators.transition_screen_submit_button).click()

    def execute_transition_with_change(self):
        self.wait_until_visible(JwtTestIssueViewLocators.transition_button, 10)
        self.get_element(JwtTestIssueViewLocators.transition_button).click()
        self.wait_until_visible(JwtTestIssueViewLocators.transition_summary, 10)
        self.get_element(JwtTestIssueViewLocators.transition_summary).send_keys("JWT-Summary")
        self.get_element(JwtTestIssueViewLocators.transition_screen_submit_button).click()
        self.wait_until_visible(JwtTestIssueViewLocators.issue_updated_flag, 10)
        self.get_element(JwtTestIssueViewLocators.issue_updated_flag_close_button).click()
        self.wait_until_invisible(JwtTestIssueViewLocators.issue_updated_flag)

    def check_summary_value(self, text):
        self.wait_until_visible(JwtTestIssueViewLocators.summary, 10)
        assert text in self.get_element(JwtTestIssueViewLocators.summary).text


class AdminToolboxIssueTypeView(BasePage):
    page_url = AdminToolboxViewLocators.admin_toolbox_issue_types_view_url
    page_loaded_selector = AdminToolboxViewLocators.filter_bar

    def check_id_column_visibility(self, visible):
        if visible:
            self.wait_until_visible(AdminToolboxViewLocators.filter_id_column, 10)
        else:
            self.wait_until_invisible(AdminToolboxViewLocators.filter_id_column)

    def activate_show_hide_id_column(self):
        self.get_element(AdminToolboxViewLocators.filter_settings_button).click()
        self.wait_until_visible(AdminToolboxViewLocators.filter_settings_show_hide_button, 10)
        if not self.get_element(AdminToolboxViewLocators.filter_settings_show_hide_checkbox).is_selected():
            self.get_element(AdminToolboxViewLocators.filter_settings_show_hide_button).click()
        self.get_element(AdminToolboxViewLocators.filter_settings_button).click()

    def deactivate_show_hide_id_column(self):
        self.wait_until_visible(AdminToolboxViewLocators.filter_settings_button, 10)
        self.get_element(AdminToolboxViewLocators.filter_settings_button).click()
        self.wait_until_visible(AdminToolboxViewLocators.filter_settings_show_hide_button, 10)
        if self.get_element(AdminToolboxViewLocators.filter_settings_show_hide_checkbox).is_selected():
            self.get_element(AdminToolboxViewLocators.filter_settings_show_hide_button).click()
        self.get_element(AdminToolboxViewLocators.filter_settings_button).click()

    def check_smart_view_visibility(self, visible):
        if visible:
            self.wait_until_visible(AdminToolboxViewLocators.filter_smart_view_related_schemes_button, 10)
        else:
            self.wait_until_invisible(AdminToolboxViewLocators.filter_smart_view_related_schemes_button)

    def activate_smart_view(self):
        self.wait_until_visible(AdminToolboxViewLocators.filter_settings_button, 10)
        self.get_element(AdminToolboxViewLocators.filter_settings_button).click()
        self.wait_until_visible(AdminToolboxViewLocators.filter_settings_smart_view_button, 10)
        if not self.get_element(AdminToolboxViewLocators.filter_settings_smart_view_checkbox).is_selected():
            self.get_element(AdminToolboxViewLocators.filter_settings_smart_view_button).click()
        self.get_element(AdminToolboxViewLocators.filter_settings_button).click()

    def deactivate_smart_view(self):
        self.wait_until_visible(AdminToolboxViewLocators.filter_settings_button, 10)
        self.get_element(AdminToolboxViewLocators.filter_settings_button).click()
        self.wait_until_visible(AdminToolboxViewLocators.filter_settings_smart_view_button, 10)
        if self.get_element(AdminToolboxViewLocators.filter_settings_smart_view_checkbox).is_selected():
            self.get_element(AdminToolboxViewLocators.filter_settings_smart_view_button).click()
        self.get_element(AdminToolboxViewLocators.filter_settings_button).click()

    def set_name_filter(self):
        self.get_element(AdminToolboxViewLocators.filter_name_select).click()
        self.wait_until_visible(AdminToolboxViewLocators.filter_name_dropdown_container, 10)
        self.get_element(AdminToolboxViewLocators.filter_name_bug_option).click()
        self.get_element(AdminToolboxViewLocators.filter_name_select).click()

    def click_reset_filter_button(self):
        self.get_element(AdminToolboxViewLocators.filter_reset_all_button).click()

    def check_activated_name_filter_result(self):
        self.wait_until_invisible(AdminToolboxViewLocators.filter_name_second_visible_table_row)

    def check_deactivated_name_filter_result(self):
        self.wait_until_visible(AdminToolboxViewLocators.filter_name_second_visible_table_row, 10)


class LastLogView(BasePage):
    page_url = LastLogViewLocators.last_log_view_url
    page_loaded_selector = LastLogViewLocators.log

    def remove_log(self):
        self.execute_js("$(\"#logContent\").html('')")

    def check_log_exists(self):
        assert 0 < len(self.get_element(LastLogViewLocators.log_content).text)

    def apply_filter(self):
        self.get_element(LastLogViewLocators.apply_filter_button).click()

    def check_log_visibility(self):
        self.wait_until_visible(LastLogViewLocators.log, 10)

    def reload(self):
        self.get_element(LastLogViewLocators.reload_button).click()


class XChartsResourcesView(BasePage):
    page_url = XChartsResourcesViewLocators.xcharts_resources_view_url
    page_loaded_selector = XChartsResourcesViewLocators.create_resources_button

    def click_create_resources_button(self):
        self.wait_until_visible(XChartsResourcesViewLocators.create_resources_button, 10)
        self.get_element(XChartsResourcesViewLocators.create_resources_button).click()

    def set_resource_name(self, name):
        self.wait_until_visible(XChartsResourcesViewLocators.resource_name_input_field, 10)
        self.get_element(XChartsResourcesViewLocators.resource_name_input_field).send_keys(name)

    def set_resource_description(self, description):
        self.wait_until_visible(XChartsResourcesViewLocators.resource_description_input_field, 10)
        self.get_element(XChartsResourcesViewLocators.resource_description_input_field).send_keys(description)

    def change_resource_type(self):
        self.wait_until_visible(XChartsResourcesViewLocators.resource_type_input_field, 10)
        self.get_element(XChartsResourcesViewLocators.resource_type_input_field).click()
        self.get_element(XChartsResourcesViewLocators.resource_type_input_field).send_keys(Keys.ENTER)

    def set_resource_data(self, data):
        self.wait_until_present(XChartsResourcesViewLocators.resource_data_input, 10)
        self.execute_js("document.getElementById(\"data\").setAttribute(\"style\",\"\")")
        self.get_element(XChartsResourcesViewLocators.resource_data_input).send_keys(data)

    def change_to_data_tab(self):
        self.wait_until_visible(XChartsResourcesViewLocators.resource_data_tab_button, 10)
        self.get_element(XChartsResourcesViewLocators.resource_data_tab_button).click()

    def click_save_resource_button(self):
        self.wait_until_visible(XChartsResourcesViewLocators.resource_save_button, 10)
        self.get_element(XChartsResourcesViewLocators.resource_save_button).click()

    def check_resource_data(self, name, description, res_type):
        self.wait_until_visible(XChartsResourcesViewLocators.table_resource_name, 10)
        assert name in self.get_element(XChartsResourcesViewLocators.table_resource_name).text
        self.wait_until_visible(XChartsResourcesViewLocators.table_resource_description, 10)
        assert description in self.get_element(XChartsResourcesViewLocators.table_resource_description).text
        self.wait_until_visible(XChartsResourcesViewLocators.table_resource_type, 10)
        assert res_type in self.get_element(XChartsResourcesViewLocators.table_resource_type).text

    def delete_first_resource(self):
        self.get_element(XChartsResourcesViewLocators.table_resource_delete_button).click()
        self.wait_until_visible(XChartsResourcesViewLocators.table_resource_delete_confirm_button, 10)
        self.get_element(XChartsResourcesViewLocators.table_resource_delete_confirm_button).click()

    def check_empty_resource_table(self):
        self.wait_until_visible(XChartsResourcesViewLocators.table_resource, 10)
        self.wait_until_invisible(XChartsResourcesViewLocators.table_resource_rows)


class XChartsDataScriptsView(BasePage):
    page_url = XChartsDataScriptsViewLocators.xcharts_data_scripts_view_url
    page_loaded_selector = XChartsDataScriptsViewLocators.create_script_button

    def set_script_name(self, name):
        self.wait_until_visible(XChartsDataScriptsViewLocators.script_name_input_field, 10)
        self.get_element(XChartsDataScriptsViewLocators.script_name_input_field).send_keys(name)

    def set_script_description(self, description):
        self.wait_until_visible(XChartsDataScriptsViewLocators.script_description_input_field, 10)
        self.get_element(XChartsDataScriptsViewLocators.script_description_input_field).send_keys(description)

    def set_example(self):
        self.wait_until_visible(XChartsDataScriptsViewLocators.script_example_input_field, 10)
        self.get_element(XChartsDataScriptsViewLocators.script_example_input_field).click()
        self.wait_until_visible(XChartsDataScriptsViewLocators.script_example_first_option, 10)
        self.get_element(XChartsDataScriptsViewLocators.script_example_input_field).send_keys(Keys.ENTER)

    def click_create_script_button(self):
        self.wait_until_visible(XChartsDataScriptsViewLocators.create_script_button, 10)
        self.get_element(XChartsDataScriptsViewLocators.create_script_button).click()

    def add_script(self):
        self.wait_until_visible(XChartsDataScriptsViewLocators.script_add_button, 10)
        self.get_element(XChartsDataScriptsViewLocators.script_add_button).click()

    def set_jql_parameter(self):
        self.wait_until_visible(XChartsDataScriptsViewLocators.script_jql_parameter_input, 10)
        self.get_element(XChartsDataScriptsViewLocators.script_jql_parameter_input).send_keys("porject = \"VLLR\"")

    def save_and_close_script(self):
        self.wait_until_visible(XChartsDataScriptsViewLocators.script_save_and_close_button, 10)
        self.get_element(XChartsDataScriptsViewLocators.script_save_and_close_button).click()

    def run_preview(self):
        self.wait_until_visible(XChartsDataScriptsViewLocators.script_preview_button, 10)
        self.wait_until_invisible(XChartsDataScriptsViewLocators.script_preview_iframe)
        self.get_element(XChartsDataScriptsViewLocators.script_preview_button).click()
        self.wait_until_visible(XChartsDataScriptsViewLocators.script_preview_iframe, 10)

    def check_script_data(self, name, description, layout):
        self.wait_until_visible(XChartsDataScriptsViewLocators.table_script_name, 10)
        assert name in self.get_element(XChartsDataScriptsViewLocators.table_script_name).text
        self.wait_until_visible(XChartsDataScriptsViewLocators.table_script_description, 10)
        assert description in self.get_element(XChartsDataScriptsViewLocators.table_script_description).text
        self.wait_until_visible(XChartsDataScriptsViewLocators.table_script_layout, 10)
        assert layout in self.get_element(XChartsDataScriptsViewLocators.table_script_layout).text

    def delete_first_script(self):
        self.get_element(XChartsDataScriptsViewLocators.table_script_delete_button).click()
        self.wait_until_visible(XChartsDataScriptsViewLocators.table_script_delete_submit_button, 10)
        self.get_element(XChartsDataScriptsViewLocators.table_script_delete_submit_button).click()

    def check_empty_resource_table(self):
        self.wait_until_visible(XChartsDataScriptsViewLocators.table_script, 10)
        self.wait_until_invisible(XChartsDataScriptsViewLocators.table_script_rows)


class SumUpCalcRulesView(BasePage):
    page_url = SumUpLocators.calc_rules_url
    page_loaded_selector = SumUpLocators.add_new_rule_button

    def add_new_rule(self):
        self.get_element(SumUpLocators.add_new_rule_button).click()
        self.wait_until_visible(SumUpLocators.new_rule_field_select, 10)
        self.get_element(SumUpLocators.new_rule_field_select).send_keys("Watchers")
        self.wait_until_visible(SumUpLocators.watchers_field_select_option, 10)
        self.get_element(SumUpLocators.new_rule_field_select).send_keys(Keys.ENTER)
        self.wait_until_visible(SumUpLocators.rule_name_field, 10)
        self.get_element(SumUpLocators.rule_name_field).send_keys("SumUp watchers field")
        self.get_element(SumUpLocators.submit_button).click()
        self.wait_until_visible(SumUpLocators.first_rule, 10)

    def delete_rule(self):
        self.get_element(SumUpLocators.delete_first_rule_button).click()
        self.wait_until_visible(SumUpLocators.submit_button, 10)
        self.get_element(SumUpLocators.submit_button).click()
        # wait 2 seconds to be sure that the rule is deleted
        time.sleep(2)
        self.go_to()
        self.element_exists(SumUpLocators.no_rule_message)


class SumUpCalculationView(BasePage):
    page_url = SumUpLocators.issues_calc_view_url
    page_loaded_selector = SumUpLocators.switch_layout_button

    def switch_view_layout(self):
        self.get_element(SumUpLocators.switch_layout_button).click()
        self.wait_until_visible(SumUpLocators.list_view_layout_option, 10)
        self.get_element(SumUpLocators.list_view_layout_option).click()

    def add_watchers_field(self):
        self.get_element(SumUpLocators.columns_button).click()
        self.wait_until_visible(SumUpLocators.columns_search_bar, 10)
        self.get_element(SumUpLocators.columns_search_bar).send_keys("Watchers")
        self.wait_until_visible(SumUpLocators.watchers_checkbox_label, 10)
        checkbox_label = self.get_element(SumUpLocators.watchers_checkbox_label)
        checkbox = self.get_element(SumUpLocators.watchers_checkbox)
        if not checkbox.is_selected():
            checkbox_label.click()
        self.get_element(SumUpLocators.columns_submit_button).click()
        self.wait_until_visible(SumUpLocators.watchers_column_header, 10)

    def calculate(self):
        self.get_element(SumUpLocators.calculate_toggle).click()
        self.wait_until_visible(SumUpLocators.page_sum_row, 10)
        self.wait_until_visible(SumUpLocators.total_sum_row, 10)
        self.get_element(SumUpLocators.calculate_toggle).click()
        self.wait_until_invisible(SumUpLocators.page_sum_row)
        self.wait_until_invisible(SumUpLocators.total_sum_row)

    def remove_watchers_field(self):
        self.get_element(SumUpLocators.columns_button).click()
        self.wait_until_visible(SumUpLocators.columns_search_bar, 10)
        self.get_element(SumUpLocators.columns_search_bar).send_keys("Watchers")
        self.wait_until_visible(SumUpLocators.watchers_checkbox_label, 10)
        checkbox_label = self.get_element(SumUpLocators.watchers_checkbox_label)
        checkbox = self.get_element(SumUpLocators.watchers_checkbox)
        if checkbox.is_selected():
            checkbox_label.click()
        self.get_element(SumUpLocators.columns_submit_button).click()


class SumUpGlobalSettingsView(BasePage):
    page_url = SumUpLocators.global_settings_url
    page_loaded_selector = SumUpLocators.supported_apps_table

    def deactivate_apps(self):
        self.wait_until_visible(SumUpLocators.active_jira_core_toggle, 10)
        self.get_element(SumUpLocators.active_jira_core_toggle).click()
        self.wait_until_visible(SumUpLocators.open_flag, 10)
        self.get_element(SumUpLocators.flag_close_button).click()
        self.wait_until_invisible(SumUpLocators.open_flag)
        self.wait_until_visible(SumUpLocators.inactive_jira_core_toggle, 10)
        self.wait_until_visible(SumUpLocators.active_jira_software_toggle, 10)
        self.get_element(SumUpLocators.active_jira_software_toggle).click()
        self.wait_until_visible(SumUpLocators.open_flag, 10)
        self.get_element(SumUpLocators.flag_close_button).click()
        self.wait_until_invisible(SumUpLocators.open_flag)
        self.wait_until_visible(SumUpLocators.inactive_jira_software_toggle, 10)

    def activate_apps(self):
        self.wait_until_visible(SumUpLocators.inactive_jira_core_toggle, 10)
        self.get_element(SumUpLocators.inactive_jira_core_toggle).click()
        self.wait_until_visible(SumUpLocators.open_flag, 10)
        self.get_element(SumUpLocators.flag_close_button).click()
        self.wait_until_invisible(SumUpLocators.open_flag)
        self.wait_until_visible(SumUpLocators.active_jira_core_toggle, 10)
        self.wait_until_visible(SumUpLocators.inactive_jira_software_toggle, 10)
        self.get_element(SumUpLocators.inactive_jira_software_toggle).click()
        self.wait_until_visible(SumUpLocators.open_flag, 10)
        self.get_element(SumUpLocators.flag_close_button).click()
        self.wait_until_invisible(SumUpLocators.open_flag)
        self.wait_until_visible(SumUpLocators.active_jira_software_toggle, 10)


class Search(BasePage):

    def __init__(self, driver, jql):
        BasePage.__init__(self, driver)
        url_manager = UrlManager(jql=jql)
        self.page_url = url_manager.jql_search_url()

    def wait_for_page_loaded(self):
        self.wait_until_any_ec_presented(selector_names=[SearchLocators.search_issue_table,
                                                         SearchLocators.search_issue_content,
                                                         SearchLocators.search_no_issue_found])


class Board(BasePage):
    page_loaded_selector = BoardLocators.board_columns

    def __init__(self, driver, board_id):
        BasePage.__init__(self, driver)
        url_manager = UrlManager(board_id=board_id)
        self.page_url = url_manager.scrum_board_url()
        self.backlog_url = url_manager.scrum_board_backlog_url()

    def go_to_backlog(self):
        self.go_to_url(self.backlog_url)

    def wait_for_scrum_board_backlog(self):
        self.wait_until_present(BoardLocators.scrum_board_backlog_content)
