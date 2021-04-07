from selenium.webdriver.common.by import By

from util.conf import CONFLUENCE_SETTINGS


class UrlManager:

    def __init__(self, page_id=None):
        self.host = CONFLUENCE_SETTINGS.server_url
        self.login_params = '/login.action'
        self.admin_login_params = '/admin/viewgeneralconfig.action'
        self.secure_login_params = '/authenticate.action?destination=/admin/viewgeneralconfig.action'
        self.page_params = f"/pages/viewpage.action?pageId={page_id}"
        self.dashboard_params = '/dashboard.action#all-updates'
        self.edit_page_params = f'/pages/editpage.action?pageId={page_id}'
        self.logout_params = "/logout.action"
        self.space_admin_browser = "/admin/plugins/spaceadmin/browser.action"
        self.space_admin_shuttle = "/admin/plugins/spaceadmin/spaceshuttle.action"
        self.space_admin_permissions = "/admin/plugins/spaceadmin/permissions.action"
        self.space_admin_attachment_service = "/admin/plugins/spaceadmin/index.action"
        self.space_admin_settings = "/admin/plugins/spaceadmin/configure.action"
        self.last_log_view_log = '/admin/plugins/lastlog/viewlog.action'

    def login_url(self):
        return f"{self.host}{self.login_params}"

    def admin_login_url(self):
        return f"{self.host}{self.admin_login_params}"

    def secure_login_url(self):
        return f"{self.host}{self.secure_login_params}"

    def dashboard_url(self):
        return f"{self.host}{self.dashboard_params}"

    def page_url(self):
        return f"{self.host}{self.page_params}"

    def edit_page_url(self):
        return f"{self.host}{self.edit_page_params}"

    def logout_url(self):
        return f"{self.host}{self.logout_params}"

    def space_admin_browser_url(self):
        return f"{self.host}{self.space_admin_browser}"

    def space_admin_shuttle_url(self):
        return f"{self.host}{self.space_admin_shuttle}"

    def space_admin_permissions_url(self):
        return f"{self.host}{self.space_admin_permissions}"

    def space_admin_attachment_service_url(self):
        return f"{self.host}{self.space_admin_attachment_service}"

    def space_admin_settings_url(self):
        return f"{self.host}{self.space_admin_settings}"

    def last_log_view_log_url(self):
        return f"{self.host}{self.last_log_view_log}"


class PopupLocators:
    timezone_popups = '.button-panel-button .set-timezone-button'
    skip_onbording_1 = '.aui-button aui-button-link .skip-onboarding'
    skip_onboarding_2 = '.aui-button.aui-button-link.skip-onboarding'
    time_saving_template = '#closeDisDialog'


class LoginPageLocators:
    login_page_url = UrlManager().login_url()
    login_button = (By.ID, "loginButton")
    login_username_field = (By.ID, "os_username")
    login_password_field = (By.ID, "os_password")

    # Setup user page per first login
    first_login_setup_page = (By.ID, "grow-ic-nav-container")
    current_step_sel = (By.CLASS_NAME, "grow-aui-progress-tracker-step-current")
    skip_welcome_button = (By.ID, "grow-intro-video-skip-button")
    skip_photo_upload = (By.CSS_SELECTOR, ".aui-button-link")
    skip_find_content = (By.CSS_SELECTOR, ".intro-find-spaces-space>.space-checkbox")
    finish_setup = (By.CSS_SELECTOR, ".intro-find-spaces-button-continue")

    logout_button = (By.CSS_SELECTOR, "#login-container > div > p.last > a:nth-child(2)")
    secure_login = UrlManager().secure_login_url()
    secure_password_field = (By.CSS_SELECTOR, "#password")
    secure_login_submit_button = (By.CSS_SELECTOR, "#authenticateButton")
    admin_login_url = UrlManager().admin_login_url()
    system_settings = (By.CSS_SELECTOR, "#admin-body-content > form > h2:nth-child(2) > a")
    login_field = (By.CSS_SELECTOR, "#os_username")
    password_field = (By.CSS_SELECTOR, "#os_password")
    login_submit_button = (By.CSS_SELECTOR, "#loginButton")


class AllUpdatesLocators:
    updates_content = (By.CLASS_NAME, "list-container-all-updates")


class PageLocators:
    page_title = (By.ID, "title-text")
    comment_text_field = (By.CSS_SELECTOR, ".quick-comment-prompt")


class DashboardLocators:
    dashboard_url = UrlManager().dashboard_url()
    updated_items = (By.CLASS_NAME, "update-items")


class TopPanelLocators:
    create_button = (By.ID, "quick-create-page-button")


class EditorLocators:
    publish_button = (By.ID, "rte-button-publish")
    confirm_publishing_button = (By.ID, "qed-publish-button")
    title_field = (By.ID, "content-title")
    page_content_field = (By.ID, "wysiwygTextarea_ifr")
    tinymce_page_content_field = (By.ID, "tinymce")
    tinymce_page_content_parahraph = (By.TAG_NAME, 'p')

    status_indicator = (By.CLASS_NAME, "status-indicator-message")
    save_spinner = (By.ID, "rte-spinner")


class SpaceAdminViewLocators:
    space_admin_browser_url = UrlManager().space_admin_browser_url()
    browser_container = (By.CSS_SELECTOR, "#spad-content > div.space-admin-container")

    space_admin_shuttle_url = UrlManager().space_admin_shuttle_url()
    shuttle_container = (By.CSS_SELECTOR, "#space-shuttle-config")
    shuttle_add_category_button = (By.CSS_SELECTOR, "#addCategory")
    shuttle_category_name_input = (By.CSS_SELECTOR, "#com-atlassian-confluence > section > div > form > div:nth-child(1) > input")
    shuttle_category_submit_button = (By.CSS_SELECTOR, "#dialog-save-button")
    shuttle_browser_category_name = (By.CSS_SELECTOR, "#space-shuttle-categories > li > div > strong")
    shuttle_browser_category_delete_button = (By.CSS_SELECTOR, "#space-shuttle-categories > li > div > div > a.aui-button.aui-button-link.remove-category")
    shuttle_browser_category_delete_confirm_button = (By.CSS_SELECTOR, "#dialog-save-button")
    shuttle_browser_categories = (By.CSS_SELECTOR, ".space-shuttle-category")

    space_admin_permissions_url = UrlManager().space_admin_permissions_url()
    permissions_container = (By.CSS_SELECTOR, "#admin-body-content > div > div > form")
    permission_user_search_input = (By.CSS_SELECTOR, "#select2-drop > div > input")
    permission_user_select = (By.CSS_SELECTOR, "#s2id_username > a")
    permission_user_select_option = (By.CSS_SELECTOR, "#select2-drop > ul > li > div")
    permission_show_button = (By.CSS_SELECTOR, "#submit-button-user-group")
    permission_approve_icons = (By.CSS_SELECTOR, "#admin-body-content > div > form > table > tbody > tr:nth-child(2) > td > span")

    space_admin_attachment_service_url = UrlManager().space_admin_attachment_service_url()
    attachment_service_container = (By.CSS_SELECTOR, "#admin-body > form")

    space_admin_settings_url = UrlManager().space_admin_settings_url()
    settings_container = (By.CSS_SELECTOR, "#admin-body-content > form")


class LastLogViewLocators:
    last_log_view_url = UrlManager().last_log_view_log_url()
    log = (By.CSS_SELECTOR, "#logContent")
    loading_spinner = (By.CSS_SELECTOR, "#reload-spinner > aui-spinner")
    apply_filter_button = (By.CSS_SELECTOR, "#send")
    log_content = (By.CSS_SELECTOR, "#logContent")
    reload_button = (By.CSS_SELECTOR, "#reload")