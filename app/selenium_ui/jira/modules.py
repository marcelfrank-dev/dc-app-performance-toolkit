import random
import urllib.parse
import time

from selenium.webdriver.common.by import By

from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login, PopupManager, Issue, Project, Search, ProjectsList, \
    BoardsList, Board, Dashboard, Logout, LastLogView, AdminLogin, SecureLogin, SumUpCalcRulesView, SumUpGlobalSettingsView, SumUpCalculationView, JwtTestIssueView, AdminToolboxIssueTypeView, XChartsResourcesView, XChartsDataScriptsView, XChartsChartView, XChartsChartView
from util.api.jira_clients import JiraRestClient
from util.conf import JIRA_SETTINGS

client = JiraRestClient(JIRA_SETTINGS.server_url, JIRA_SETTINGS.admin_login, JIRA_SETTINGS.admin_password)
rte_status = client.check_rte_status()

KANBAN_BOARDS = "kanban_boards"
SCRUM_BOARDS = "scrum_boards"
USERS = "users"
ISSUES = "issues"
CUSTOM_ISSUES = "custom_issues"
JQLS = "jqls"
PROJECTS = "projects"


def setup_run_data(datasets):
    page_size = 25
    projects_count = len(datasets[PROJECTS])
    user = random.choice(datasets[USERS])
    issue = random.choice(datasets[ISSUES])
    if CUSTOM_ISSUES in datasets:
        if len(datasets[CUSTOM_ISSUES]) > 0:
            custom_issue = random.choice(datasets[CUSTOM_ISSUES])
            datasets['custom_issue_key'] = custom_issue[0]
            datasets['custom_issue_id'] = custom_issue[1]
    scrum_boards = random.choice(datasets[SCRUM_BOARDS])
    kanban_boards = random.choice(datasets[KANBAN_BOARDS])
    projects = random.choice(datasets[PROJECTS])
    datasets['username'] = user[0]
    datasets['password'] = user[1]
    datasets['issue_key'] = issue[0]
    datasets['issue_id'] = issue[1]
    datasets['project_key'] = projects[0]
    datasets['scrum_board_id'] = scrum_boards[0]
    datasets['kanban_board_id'] = kanban_boards[0]
    datasets['jql'] = urllib.parse.quote(random.choice(datasets[JQLS][0]))
    datasets['project_pages_count'] = projects_count // page_size if projects_count % page_size == 0 \
        else projects_count // page_size + 1


def login(webdriver, datasets):
    setup_run_data(datasets)

    @print_timing("selenium_login")
    def measure():
        login_page = Login(webdriver)

        @print_timing("selenium_login:open_login_page")
        def sub_measure():
            login_page.go_to()

        sub_measure()

        @print_timing("selenium_login:login_and_view_dashboard")
        def sub_measure():
            login_page.set_credentials(username=datasets['username'], password=datasets['password'])
            if login_page.is_first_login():
                login_page.first_login_setup()
            if login_page.is_first_login_second_page():
                login_page.first_login_second_page_setup()
            login_page.wait_for_page_loaded()
            webdriver.node_id = login_page.get_node_id()
            print(f"node_id:{webdriver.node_id}")

        sub_measure()

    measure()
    PopupManager(webdriver).dismiss_default_popup()


def adminLogin(webdriver):
    @print_timing("selenium_admin_login")
    def measure():
        login_page = AdminLogin(webdriver)
        secure_login_page = SecureLogin(webdriver)

        @print_timing("selenium_admin_login:open_login_page")
        def sub_measure():
            login_page.go_to()

        sub_measure()

        @print_timing("selenium_admin_login:login_and_view_system_settings")
        def sub_measure():
            login_page.set_credentials(username="admin", password="admin")
            secure_login_page.wait_until_visible((By.ID, "login-form-authenticatePassword"), 30000)
            secure_login_page.set_credentials()
            login_page.wait_for_page_loaded()

        sub_measure()

    measure()
    PopupManager(webdriver).dismiss_default_popup()


def secureLogin(webdriver):
    @print_timing("selenium_admin_login")
    def measure():
        login_page = SecureLogin(webdriver)
        login_page.wait_for_page_loaded()

        @print_timing("selenium_admin_login:login_and_view_system_settings")
        def sub_measure():
            login_page.set_credentials()

        sub_measure()

    measure()
    PopupManager(webdriver).dismiss_default_popup()


def view_issue(webdriver, datasets):
    issue_page = Issue(webdriver, issue_key=datasets['issue_key'])

    @print_timing("selenium_view_issue")
    def measure():
        issue_page.go_to()
        issue_page.wait_for_page_loaded()

    measure()


def view_project_summary(webdriver, datasets):
    project_page = Project(webdriver, project_key=datasets['project_key'])

    @print_timing("selenium_project_summary")
    def measure():
        project_page.go_to()
        project_page.wait_for_page_loaded()

    measure()


def create_issue(webdriver, dataset):
    issue_modal = Issue(webdriver)

    @print_timing("selenium_create_issue")
    def measure():
        @print_timing("selenium_create_issue:open_quick_create")
        def sub_measure():
            issue_modal.open_create_issue_modal()

        sub_measure()

        @print_timing("selenium_create_issue:fill_and_submit_issue_form")
        def sub_measure():
            issue_modal.fill_summary_create()  # Fill summary field
            issue_modal.fill_description_create(rte_status)  # Fill description field
            issue_modal.assign_to_me()  # Click assign to me
            issue_modal.set_resolution()  # Set resolution if there is such field
            issue_modal.set_issue_type()  # Set issue type, use non epic type

            @print_timing("selenium_create_issue:fill_and_submit_issue_form:submit_issue_form")
            def sub_sub_measure():
                issue_modal.submit_issue()

            sub_sub_measure()

        sub_measure()

    measure()
    PopupManager(webdriver).dismiss_default_popup()


def search_jql(webdriver, datasets):
    search_page = Search(webdriver, jql=datasets['jql'])

    @print_timing("selenium_search_jql")
    def measure():
        search_page.go_to()
        search_page.wait_for_page_loaded()

    measure()


def edit_issue(webdriver, datasets):
    issue_page = Issue(webdriver, issue_id=datasets['issue_id'])

    @print_timing("selenium_edit_issue")
    def measure():
        @print_timing("selenium_edit_issue:open_edit_issue_form")
        def sub_measure():
            issue_page.go_to_edit_issue()  # open editor

        sub_measure()

        issue_page.fill_summary_edit()  # edit summary
        issue_page.fill_description_edit(rte_status)  # edit description

        @print_timing("selenium_edit_issue:save_edit_issue_form")
        def sub_measure():
            issue_page.edit_issue_submit()  # submit edit issue
            issue_page.wait_for_issue_title()

        sub_measure()

    measure()


def save_comment(webdriver, datasets):
    issue_page = Issue(webdriver, issue_id=datasets['issue_id'])

    @print_timing("selenium_save_comment")
    def measure():
        @print_timing("selenium_save_comment:open_comment_form")
        def sub_measure():
            issue_page.go_to_edit_comment()  # Open edit comment page

        sub_measure()

        issue_page.fill_comment_edit(rte_status)  # Fill comment text field

        @print_timing("selenium_save_comment:submit_form")
        def sub_measure():
            issue_page.edit_comment_submit()  # Submit comment

        sub_measure()

    measure()


def browse_projects_list(webdriver, datasets):
    @print_timing("selenium_browse_projects_list")
    def measure():
        projects_list_page = ProjectsList(webdriver, projects_list_pages=datasets['project_pages_count'])
        projects_list_page.go_to()
        projects_list_page.wait_for_page_loaded()

    measure()


def browse_boards_list(webdriver, datasets):
    @print_timing("selenium_browse_boards_list")
    def measure():
        boards_list_page = BoardsList(webdriver)
        boards_list_page.go_to()
        boards_list_page.wait_for_page_loaded()

    measure()
    PopupManager(webdriver).dismiss_default_popup()


def view_backlog_for_scrum_board(webdriver, datasets):
    scrum_board_page = Board(webdriver, board_id=datasets['scrum_board_id'])

    @print_timing("selenium_view_scrum_board_backlog")
    def measure():
        scrum_board_page.go_to_backlog()
        scrum_board_page.wait_for_scrum_board_backlog()

    measure()


def view_scrum_board(webdriver, datasets):
    scrum_board_page = Board(webdriver, board_id=datasets['scrum_board_id'])

    @print_timing("selenium_view_scrum_board")
    def measure():
        scrum_board_page.go_to()
        scrum_board_page.wait_for_page_loaded()

    measure()


def view_kanban_board(webdriver, datasets):
    kanban_board_page = Board(webdriver, board_id=datasets['kanban_board_id'])

    @print_timing("selenium_view_kanban_board")
    def measure():
        kanban_board_page.go_to()
        kanban_board_page.wait_for_page_loaded()

    measure()


def view_dashboard(webdriver, datasets):
    dashboard_page = Dashboard(webdriver)

    @print_timing("selenium_view_dashboard")
    def measure():
        dashboard_page.go_to()
        dashboard_page.wait_dashboard_presented()

    measure()


def log_out(webdriver, datasets):
    logout_page = Logout(webdriver)

    @print_timing("selenium_log_out")
    def measure():
        logout_page.go_to()
        logout_page.click_logout()
        logout_page.wait_for_page_loaded()

    measure()


# SUM UP
def browse_calc_issues_view(webdriver):
    @print_timing("selenium_browse_calc_issues_view")
    def measure():
        sum_up_calc_issues_view_page = SumUpCalculationView(webdriver)
        sum_up_calc_issues_view_page.go_to()
        sum_up_calc_issues_view_page.wait_for_page_loaded()

    measure()
    PopupManager(webdriver).dismiss_default_popup()


def browse_calc_rules_view(webdriver):
    @print_timing("selenium_browse_calc_rules_view")
    def measure():
        sum_up_calc_rules_view_page = SumUpCalcRulesView(webdriver)
        sum_up_calc_rules_view_page.go_to()
        sum_up_calc_rules_view_page.wait_for_page_loaded()

    measure()
    PopupManager(webdriver).dismiss_default_popup()


def browse_global_settings_view(webdriver):
    @print_timing("selenium_browse_global_settings_view")
    def measure():
        sum_up_global_settings_view_page = SumUpGlobalSettingsView(webdriver)
        sum_up_global_settings_view_page.go_to()
        sum_up_global_settings_view_page.wait_for_page_loaded()

    measure()
    PopupManager(webdriver).dismiss_default_popup()


# LAST LOG
def last_log_view_log(webdriver):
    @print_timing("selenium_last_log_view_log")
    def measure():
        last_log_view_page = LastLogView(webdriver)
        last_log_view_page.go_to()
        last_log_view_page.wait_for_page_loaded()

    measure()
    PopupManager(webdriver).dismiss_default_popup()

def last_log_apply_filter(webdriver):
    @print_timing("selenium_last_log_apply_filter")
    def measure():
        last_log_view_page = LastLogView(webdriver)
        last_log_view_page.remove_log()
        last_log_view_page.apply_filter()
        time.sleep(1)
        last_log_view_page.check_log_exists()
        last_log_view_page.check_log_visibility()

    measure()
    PopupManager(webdriver).dismiss_default_popup()

def last_log_reload_action(webdriver):
    @print_timing("selenium_last_log_reload_action")
    def measure():
        last_log_view_page = LastLogView(webdriver)
        last_log_view_page.remove_log()
        last_log_view_page.reload()
        time.sleep(1)
        last_log_view_page.check_log_exists()
        last_log_view_page.check_log_visibility()
    measure()
    PopupManager(webdriver).dismiss_default_popup()



#XCHARTS
def xcharts_add_js_ressource(webdriver):
    @print_timing("selenium_xcharts_add_js_ressource")
    def measure():
        xcharts_resources_page = XChartsResourcesView(webdriver)
        xcharts_resources_page.go_to()
        xcharts_resources_page.wait_for_page_loaded()
        PopupManager(webdriver).dismiss_default_popup()
        xcharts_resources_page.click_create_resources_button()
        xcharts_resources_page.set_resource_name("JavaScript resource name")
        xcharts_resources_page.set_resource_description("JavaScript resource description")
        xcharts_resources_page.change_to_data_tab()
        xcharts_resources_page.set_resource_data("console.log(\"this is xcharts\")")
        xcharts_resources_page.click_save_resource_button()
        xcharts_resources_page.wait_for_page_loaded()
        xcharts_resources_page.check_resource_data("JavaScript resource name", "JavaScript resource description", "JavaScript")
        xcharts_resources_page.delete_first_resource()
        xcharts_resources_page.check_empty_resource_table()

    measure()
    PopupManager(webdriver).dismiss_default_popup()

def xcharts_add_css_ressource(webdriver):
    @print_timing("selenium_xcharts_add_css_ressource")
    def measure():
        xcharts_resources_page = XChartsResourcesView(webdriver)
        xcharts_resources_page.go_to()
        xcharts_resources_page.wait_for_page_loaded()
        PopupManager(webdriver).dismiss_default_popup()
        xcharts_resources_page.click_create_resources_button()
        xcharts_resources_page.set_resource_name("CSS resource name")
        xcharts_resources_page.set_resource_description("CSS resource description")
        xcharts_resources_page.change_resource_type()
        xcharts_resources_page.change_to_data_tab()
        xcharts_resources_page.set_resource_data(".test {color: #fff;}")
        xcharts_resources_page.click_save_resource_button()
        xcharts_resources_page.wait_for_page_loaded()
        xcharts_resources_page.check_resource_data("CSS resource name", "CSS resource description", "CSS")
        xcharts_resources_page.delete_first_resource()
        xcharts_resources_page.check_empty_resource_table()
    measure()
    PopupManager(webdriver).dismiss_default_popup()

def xcharts_add_data_script(webdriver):
  @print_timing("selenium_xcharts_add_data_script")
  def measure():
        xcharts_data_script_page = XChartsDataScriptsView(webdriver)
        xcharts_data_script_page.go_to()
        xcharts_data_script_page.wait_for_page_loaded()
        PopupManager(webdriver).dismiss_default_popup()
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

  measure()
  PopupManager(webdriver).dismiss_default_popup()

def xcharts_open_default_chart(webdriver):
    @print_timing("selenium_xcharts_open_default_chart")
    def measure():
        xcharts_charts_view = XChartsChartView(webdriver)
        xcharts_charts_view.go_to()
        xcharts_charts_view.wait_for_page_loaded()
        xcharts_charts_view.checkTop10ReporterChart()
    measure()
    PopupManager(webdriver).dismiss_default_popup()

# JWT
def browse_jwt_test_issue(webdriver):
    @print_timing("selenium_browse_jwt_test_issue")
    def measure():
        jwt_test_issue_view_page = JwtTestIssueView(webdriver)
        jwt_test_issue_view_page.go_to()
        jwt_test_issue_view_page.wait_for_page_loaded()

    measure()
    PopupManager(webdriver).dismiss_default_popup()


# ADMIN TOOLBOX
def browse_admin_toolbox_issue_types_view(webdriver):
    @print_timing("selenium_browse_admin_toolbox_issue_types_view")
    def measure():
        admin_toolbox_issue_type_view_page = AdminToolboxIssueTypeView(webdriver)
        admin_toolbox_issue_type_view_page.go_to()
        admin_toolbox_issue_type_view_page.wait_for_page_loaded()

    measure()
    PopupManager(webdriver).dismiss_default_popup()
