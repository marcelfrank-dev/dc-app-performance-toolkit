from selenium.webdriver.common.by import By
from util.conf import JIRA_SETTINGS


class PopupLocators:
    default_popup = '.aui-message .icon-close'
    popup_1 = 'form.tip-footer>.helptip-close'
    popup_2 = '.aui-inline-dialog-contents .cancel'


class UrlManager:

    def __init__(self, issue_key=None, issue_id=None, project_key=None, jql=None, projects_list_page=None,
                 board_id=None):
        self.host = JIRA_SETTINGS.server_url
        self.login_params = '/login.jsp'
        self.admin_login_params = '/secure/admin/ViewApplicationProperties.jspa'
        self.logout_params = '/logoutconfirm.jsp'
        self.dashboard_params = '/secure/Dashboard.jspa'
        self.issue_params = f"/browse/{issue_key}"
        self.project_summary_params = f"/projects/{project_key}/summary"
        self.jql_params = f"/issues/?jql={jql}"
        self.edit_issue_params = f"/secure/EditIssue!default.jspa?id={issue_id}"
        self.edit_comments_params = f"/secure/AddComment!default.jspa?id={issue_id}"
        self.projects_list_params = f'/secure/BrowseProjects.jspa?selectedCategory=all&selectedProjectType=all&page=' \
                                    f'{projects_list_page}'
        self.boards_list_params = '/secure/ManageRapidViews.jspa'
        self.scrum_board_backlog_params = f"/secure/RapidBoard.jspa?rapidView={board_id}&view=planning"
        self.scrum_board_params = f"/secure/RapidBoard.jspa?rapidView={board_id}"
        self.last_log_view_log = '/secure/admin/ViewLastLog!default.jspa'
        self.xcharts_resources_view = '/secure/ChartResourcesIndex!default.jspa'
        self.xcharts_data_scripts_view = '/secure/ScriptedChartsIndex!default.jspa'
        self.admin_toolbox_issue_types_view = '/secure/admin/ViewIssueTypes.jspa'
        self.jwt_test_issue_view = '/browse/AFOCIA-1'
        self.calc_rules = '/secure/SumUpViewRule!default.jspa'
        self.issues_calc = '/issues/?jql=watcher%20is%20not%20EMPTY%20and%20project%20%3D%20"VLLR"'
        self.global_settings = '/secure/SumUpAdminConfiguration!default.jspa'

    def login_url(self):
        return f"{self.host}{self.login_params}"

    def admin_login_url(self):
        return f"{self.host}{self.admin_login_params}"

    def dashboard_url(self):
        return f"{self.host}{self.dashboard_params}"

    def issue_url(self):
        return f"{self.host}{self.issue_params}"

    def project_summary_url(self):
        return f"{self.host}{self.project_summary_params}"

    def jql_search_url(self):
        return f"{self.host}{self.jql_params}"

    def edit_issue_url(self):
        return f"{self.host}{self.edit_issue_params}"

    def edit_comments_url(self):
        return f"{self.host}{self.edit_comments_params}"

    def projects_list_page_url(self):
        return f"{self.host}{self.projects_list_params}"

    def boards_list_page_url(self):
        return f"{self.host}{self.boards_list_params}"

    def scrum_board_backlog_url(self):
        return f"{self.host}{self.scrum_board_backlog_params}"

    def scrum_board_url(self):
        return f"{self.host}{self.scrum_board_params}"

    def logout_url(self):
        return f"{self.host}{self.logout_params}"

    def last_log_view_log_url(self):
        return f"{self.host}{self.last_log_view_log}"

    def xcharts_resources_view_url(self):
        return f"{self.host}{self.xcharts_resources_view}"

    def xcharts_data_scripts_view_url(self):
        return f"{self.host}{self.xcharts_data_scripts_view}"

    def admin_toolbox_issue_types_view_url(self):
        return f"{self.host}{self.admin_toolbox_issue_types_view}"

    def jwt_test_issue_view_url(self):
        return f"{self.host}{self.jwt_test_issue_view}"

    def calc_rules_url(self):
        return f"{self.host}{self.calc_rules}"

    def issues_calc_view_url(self):
        return f"{self.host}{self.issues_calc}"

    def global_settings_url(self):
        return f"{self.host}{self.global_settings}"


class LoginPageLocators:
    login_url = UrlManager().login_url()
    admin_login_url = UrlManager().admin_login_url()
    login_params = UrlManager().login_params

    # First time login setup page
    continue_button = (By.ID, 'next')
    avatar_page_next_button = (By.CSS_SELECTOR, "input[value='Next']")
    explore_current_projects = (By.CSS_SELECTOR, "a[data-step-key='browseprojects']")
    login_field = (By.ID, 'login-form-username')
    password_field = (By.ID, 'login-form-password')
    secure_password_field = (By.ID, 'login-form-authenticatePassword')
    login_submit_button = (By.ID, 'login-form-submit')
    system_dashboard = (By.ID, "dashboard")
    system_settings = (By.ID, "main")
    secure_login = (By.ID, "login-form")


class LogoutLocators:
    logout_url = UrlManager().logout_url()
    logout_submit_button = (By.ID, "confirm-logout-submit")
    login_button_link = (By.CLASS_NAME, "login-link")


class DashboardLocators:
    dashboard_url = UrlManager().dashboard_url()
    dashboard_params = UrlManager().dashboard_params
    dashboard_window = (By.CLASS_NAME, "page-type-dashboard")


class IssueLocators:
    issue_title = (By.ID, "summary-val")

    create_issue_button = (By.ID, "create_link")
    # Issue create modal form
    issue_modal = (By.ID, "create-issue-dialog")
    issue_summary_field = (By.ID, "summary")
    issue_description_field_RTE = (By.XPATH, "//div[textarea[@id='description']]//iframe")
    issue_description_field = (By.XPATH, "//textarea[@id='description']")
    tinymce_description_field = (By.ID, "tinymce")
    issue_assign_to_me_link = (By.ID, 'assign-to-me-trigger')
    issue_resolution_field = (By.ID, 'resolution')
    issue_type_field = (By.ID, 'issuetype-field')
    issue_types_options = (By.ID, "issuetype-options")
    issue_type_dropdown_elements = (By.CLASS_NAME, "aui-list-item")
    issue_ready_to_save_spinner = (By.CSS_SELECTOR, ".buttons>.throbber")
    issue_submit_button = (By.ID, "create-issue-submit")

    # Edit Issue page
    edit_issue_page = (By.ID, "issue-edit")
    edit_issue_description = (By.ID, 'description')
    edit_issue_submit = (By.ID, 'issue-edit-submit')

    # Edit Comments page
    edit_comment_add_comment_button = (By.ID, "comment-add-submit")
    edit_comment_text_field_RTE = (By.XPATH, "//div[textarea[@id='comment']]//iframe")
    edit_comment_text_field = (By.XPATH, "//textarea[@id='comment']")


class ProjectLocators:
    project_summary_property_column = (By.CLASS_NAME, 'project-meta-column')

    # projects list locators
    projects_list = (By.CSS_SELECTOR, "tbody.projects-list")
    projects_not_found = (By.CLASS_NAME, "none-panel")


class SearchLocators:
    search_issue_table = (By.ID, "issuetable")
    search_issue_content = (By.ID, "issue-content")
    search_no_issue_found = (By.CLASS_NAME, "no-results-message")


class BoardsListLocators:
    boards_list_url = UrlManager().boards_list_page_url()
    boards_list_params = UrlManager().boards_list_params

    boards_list = (By.CSS_SELECTOR, "#ghx-content-main table.aui")


class LastLogViewLocators:
    last_log_view_url = UrlManager().last_log_view_log_url()
    log = (By.CSS_SELECTOR, "#logContent")
    loading_spinner = (By.CSS_SELECTOR, "#reload-spinner > aui-spinner")
    apply_filter_button = (By.CSS_SELECTOR, "#send")
    log_content = (By.CSS_SELECTOR, "#logContent")
    reload_button = (By.CSS_SELECTOR, "#reload")


class XChartsResourcesViewLocators:
    xcharts_resources_view_url = UrlManager().xcharts_resources_view_url()
    create_resources_button = (By.CSS_SELECTOR, "#content > div > div > section > header > div > div.aui-page-header-actions > div > a")
    resource_name_input_field = (By.CSS_SELECTOR, "#name")
    resource_description_input_field = (By.CSS_SELECTOR, "#description")
    resource_type_input_field = (By.CSS_SELECTOR, "#type-field")
    resource_data_tab_button = (By.CSS_SELECTOR, "#content > div > div > section > div > form > div.aui-group.aui-group-split > div:nth-child(1) > div > div:nth-child(2)")
    resource_data_input = (By.CSS_SELECTOR, "#data")
    resource_save_button = (By.CSS_SELECTOR, "#content > div > div > section > div > form > div.aui-group.aui-group-split > div:nth-child(2) > div:nth-child(1) > input")

    table_resource = (By.CSS_SELECTOR, ".xcharts-table")
    table_resource_name = (By.CSS_SELECTOR, "#content > div > div > section > table > tbody > tr:nth-child(1) > td:nth-child(1) > a")
    table_resource_description = (By.CSS_SELECTOR, "#content > div > div > section > table > tbody > tr:nth-child(1) > td:nth-child(1) > div")
    table_resource_type = (By.CSS_SELECTOR, "#content > div > div > section > table > tbody > tr:nth-child(1) > td:nth-child(2) > span")
    table_resource_delete_button = (By.CSS_SELECTOR, "#content > div > div > section > table > tbody > tr:nth-child(1) > td.cell-type-collapsed.action > ul > li:nth-child(2) > a")
    table_resource_delete_confirm_button = (By.CSS_SELECTOR, "#content > div > div > section > form > div.buttons-container > div > input")
    table_resource_rows = (By.CSS_SELECTOR, "#content > div > div > section > table > tbody > tr:not(.noresult)")


class XChartsDataScriptsViewLocators:
    xcharts_data_scripts_view_url = UrlManager().xcharts_data_scripts_view_url()
    create_script_button = (By.CSS_SELECTOR, "#content > div > div > section > header > div > div.aui-page-header-actions > div > a.aui-button.trigger-scripted-chart-add-dialog")
    script_name_input_field = (By.CSS_SELECTOR, "#name")
    script_description_input_field = (By.CSS_SELECTOR, "#description")
    script_example_input_field = (By.CSS_SELECTOR, "#template-field")
    script_example_first_option = (By.CSS_SELECTOR, "[id^=\"timeseries-chart-\"] > a")
    script_add_button = (By.CSS_SELECTOR, "#trigger-scripted-chart-add-dialog > div.jira-dialog-content > form > div.buttons-container > div > input.aui-button.aui-button-primary")
    script_jql_parameter_input = (By.CSS_SELECTOR, "#JQL")
    script_preview_button = (By.CSS_SELECTOR, "#previewButton")
    script_preview_iframe = (By.CSS_SELECTOR, "#chart-preview-iframe")
    script_save_and_close_button = (By.CSS_SELECTOR, "#content > div > div > section > div.aui-page-panel-content > div.aui-group.aui-group-split > div:nth-child(2) > div:nth-child(1) > input.aui-button.aui-button-primary.submit-and-close")

    table_script = (By.CSS_SELECTOR, ".xcharts-table")
    table_script_rows = (By.CSS_SELECTOR, "#content > div > div > section > table > tbody > tr:not(.noresult)")
    table_script_name = (By.CSS_SELECTOR, "#content > div > div > section > table > tbody > tr:nth-child(1) > td:nth-child(1) > a")
    table_script_description = (By.CSS_SELECTOR, "#content > div > div > section > table > tbody > tr:nth-child(1) > td:nth-child(1) > div")
    table_script_layout = (By.CSS_SELECTOR, "#content > div > div > section > table > tbody > tr:nth-child(1) > td:nth-child(2) > a")
    table_script_delete_button = (By.CSS_SELECTOR, "#content > div > div > section > table > tbody > tr:nth-child(1) > td:nth-child(6) > ul > li:nth-child(3) > a")
    table_script_delete_submit_button = (By.CSS_SELECTOR, "#content > div > div > section > form > div.buttons-container > div > input")


class AdminToolboxViewLocators:
    admin_toolbox_issue_types_view_url = UrlManager().admin_toolbox_issue_types_view_url()
    filter_bar = (By.CSS_SELECTOR, ".xtools-navigator-filter")
    filter_id_column = (By.CSS_SELECTOR, "th.xtools-id")
    filter_settings_button = (By.CSS_SELECTOR, "div.aui-button.xtools-filter-configuration > span")
    filter_name_select = (By.CSS_SELECTOR, "#main > form > div.aui-toolbar2 > div > div > div.aui-toolbar2-primary.xtools-filter-list > div:nth-child(1) > "
                                           "div.xtools-filter-selector.aui-button.drop-arrow")
    filter_name_dropdown_container = (By.CSS_SELECTOR, "#issuetype-suggestions")
    filter_name_bug_option = (By.CSS_SELECTOR, "#suggestions li:nth-child(1) label")
    filter_name_second_visible_table_row = (By.CSS_SELECTOR, "#issue-types-table > tbody > tr:nth-child(2)")
    filter_reset_all_button = (By.CSS_SELECTOR, ".xtools-reset-all-filters")
    filter_settings_show_hide_button = (By.CSS_SELECTOR, "#jira > div.ajs-layer.box-shadow.active > form > div > ul:nth-child(2) > li:nth-child(1) > label")
    filter_settings_show_hide_checkbox = (By.CSS_SELECTOR, "#jira > div.ajs-layer.box-shadow.active > form > div > ul:nth-child(2) > li:nth-child(1) > label > [type=\"checkbox\"]")
    filter_settings_smart_view_button = (By.CSS_SELECTOR, "#jira > div.ajs-layer.box-shadow.active > form > div > ul:nth-child(2) > li:nth-child(2) > label")
    filter_settings_smart_view_checkbox = (By.CSS_SELECTOR, "#jira > div.ajs-layer.box-shadow.active > form > div > ul:nth-child(2) > li:nth-child(2) > label > [type=\"checkbox\"]")
    filter_smart_view_related_schemes_button = (By.CSS_SELECTOR, "#issue-types-table > tbody > tr:nth-child(1) > td:nth-child(4) > button")


class JwtTestIssueViewLocators:
    jwt_test_issue_view_url = UrlManager().jwt_test_issue_view_url()
    transition_button = (By.CSS_SELECTOR, "#action_id_51")
    transition_screen_submit_button = (By.CSS_SELECTOR, "#issue-workflow-transition-submit")
    transition_screen_cancel_button = (By.CSS_SELECTOR, "#issue-workflow-transition-cancel")
    transition_screen_error = (By.CSS_SELECTOR, ".error")
    summary = (By.CSS_SELECTOR, "#summary-val")
    transition_summary = (By.CSS_SELECTOR, "#summary")
    assignee = (By.CSS_SELECTOR, "#assignee-val")
    issue_updated_flag = (By.CSS_SELECTOR, "#aui-flag-container > div[open=\"open\"]")
    issue_updated_flag_close_button = (By.CSS_SELECTOR, ".aui-close-button")

    calc_field_value = (By.CSS_SELECTOR, "#customfield_11200-val")

    assign_to_me_button = (By.CSS_SELECTOR, "#assign-to-me")

    priority_button = (By.CSS_SELECTOR, "#priority-val")
    first_priority_option = (By.CSS_SELECTOR, ".aui-list-item.active")
    submit_priority_button = (By.CSS_SELECTOR, "#priority-form > div.save-options > button.aui-button.submit")
    priority_select_loading = (By.CSS_SELECTOR, "#priority-single-select.aui-disabled")


class SumUpLocators:
    # issues calc
    issues_calc_view_url = UrlManager().issues_calc_view_url()
    switch_layout_button = (By.CSS_SELECTOR, "#layout-switcher-button")
    list_view_layout_option = (By.CSS_SELECTOR, "[data-layout-key=\"list-view\"]")
    columns_button = (By.CSS_SELECTOR, "#main > div > div.issue-search-header > form > div.aui-group > div:nth-child(2) > div > div.aui-item.column-picker-container > div > button")
    columns_search_bar = (By.CSS_SELECTOR, "#user-column-sparkler-input")
    columns_submit_button = (By.CSS_SELECTOR, "#inline-dialog-column-picker-dialog > div.aui-inline-dialog-contents.contents > div > form > div.button-panel > input")
    watchers_column_header = (By.CSS_SELECTOR, "[data-id=\"watches\"]")
    watchers_checkbox_label = (By.CSS_SELECTOR, "#watches-1 > label")
    watchers_checkbox = (By.CSS_SELECTOR, "#watches-1 > label > input[type=checkbox]")
    calculate_toggle = (By.CSS_SELECTOR, "#sumup-navigator-toggle")
    page_sum_row = (By.CSS_SELECTOR, ".pageSumRow")
    total_sum_row = (By.CSS_SELECTOR, ".sumRow")

    # global settings
    global_settings_url = UrlManager().global_settings_url()
    supported_apps_table = (By.CSS_SELECTOR, "#supportedAppsTable")
    active_jira_core_toggle = (By.CSS_SELECTOR, "#jira-core > td.status-row > aui-toggle[checked]")
    active_jira_software_toggle = (By.CSS_SELECTOR, "#com-pyxis-greenhopper-jira > td.status-row > aui-toggle[checked]")
    inactive_jira_core_toggle = (By.CSS_SELECTOR, "#jira-core > td.status-row > aui-toggle:not([checked])")
    inactive_jira_software_toggle = (By.CSS_SELECTOR, "#com-pyxis-greenhopper-jira > td.status-row > aui-toggle:not([checked])")
    open_flag = (By.CSS_SELECTOR, "#aui-flag-container > div[open=\"open\"]")
    flag_close_button = (By.CSS_SELECTOR, ".aui-close-button")

    # cal rules
    calc_rules_url = UrlManager().calc_rules_url()
    add_new_rule_button = (By.CSS_SELECTOR, "#main > header > div > div.aui-page-header-actions > div > a")
    new_rule_field_select = (By.CSS_SELECTOR, "#customFieldDisplayNameSelect-field")
    watchers_field_select_option = (By.CSS_SELECTOR, "[id^=\"watchers-\"]")
    rule_name_field = (By.CSS_SELECTOR, "#name")
    submit_button = (By.CSS_SELECTOR, "#submit-form")
    first_rule = (By.CSS_SELECTOR, "#main > table > tbody > tr")
    no_rule_message = (By.CSS_SELECTOR, "#main > div > p > strong")
    delete_first_rule_button = (By.CSS_SELECTOR, "#main > table > tbody > tr > td:nth-child(7) > ul > li:nth-child(2) > a")


class BoardLocators:
    # Scrum boards
    scrum_board_backlog_content = (By.CSS_SELECTOR, "#ghx-backlog[data-rendered]:not(.browser-metrics-stale)")
    board_columns = (By.CSS_SELECTOR, ".ghx-column")
