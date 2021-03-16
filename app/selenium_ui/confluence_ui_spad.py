from selenium_ui.confluence import modules
from extension.confluence import extension_ui  # noqa F401


# this action should be the first one
from selenium_ui.confluence.pages.pages import SpaceAdminBrowserView, SpaceAdminShuttleView, SpaceAdminPermissionsView, SpaceAdminAttachmentServiceView, SpaceAdminSettingsView


def test_0_selenium_a_login(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.login(confluence_webdriver, confluence_datasets)


def test_1_selenium_view_page(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.view_page(confluence_webdriver, confluence_datasets)


def test_1_selenium_create_page(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.create_confluence_page(confluence_webdriver, confluence_datasets)


def test_1_selenium_edit_page(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.edit_confluence_page(confluence_webdriver, confluence_datasets)


def test_1_selenium_create_comment(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.create_comment(confluence_webdriver, confluence_datasets)


def test_1_selenium_view_blog(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.view_blog(confluence_webdriver, confluence_datasets)


def test_1_selenium_view_dashboard(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.view_dashboard(confluence_webdriver, confluence_datasets)


"""
Add custom actions anywhere between login and log out action. Move this to a different line as needed.
Write your custom selenium scripts in `app/extension/confluence/extension_ui.py`.
Refer to `app/selenium_ui/confluence/modules.py` for examples.
"""
# def test_1_selenium_custom_action(confluence_webdriver, confluence_datasets, confluence_screen_shots):
#     extension_ui.app_specific_action(confluence_webdriver, confluence_datasets)


# ----------------------- ADMIN MODE ------------------------
def test_1_selenium_a_login(jira_webdriver, jira_datasets, jira_screen_shots):
    modules.admin_login(jira_webdriver)


def test_1_selenium_browse_spad_pages_action(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    space_admin_browser = SpaceAdminBrowserView(confluence_webdriver)
    space_admin_browser.go_to()
    space_admin_browser.wait_for_page_loaded()

    space_admin_shuttle = SpaceAdminShuttleView(confluence_webdriver)
    space_admin_shuttle.go_to()
    space_admin_shuttle.wait_for_page_loaded()

    space_admin_permissions = SpaceAdminPermissionsView(confluence_webdriver)
    space_admin_permissions.go_to()
    space_admin_permissions.wait_for_page_loaded()

    space_admin_attachment_service = SpaceAdminAttachmentServiceView(confluence_webdriver)
    space_admin_attachment_service.go_to()
    space_admin_attachment_service.wait_for_page_loaded()

    space_admin_settings = SpaceAdminSettingsView(confluence_webdriver)
    space_admin_settings.go_to()
    space_admin_settings.wait_for_page_loaded()


def test_1_selenium_check_permissions_action(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    space_admin_permissions = SpaceAdminPermissionsView(confluence_webdriver)
    space_admin_permissions.go_to()
    space_admin_permissions.wait_for_page_loaded()
    space_admin_permissions.select_admin()
    space_admin_permissions.click_show_button()
    space_admin_permissions.check_permissions()


def test_1_selenium_shuttle_action(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    space_admin_permissions = SpaceAdminShuttleView(confluence_webdriver)
    space_admin_permissions.go_to()
    space_admin_permissions.wait_for_page_loaded()
    space_admin_permissions.click_add_category_button()
    space_admin_permissions.set_category_name("Test category")
    space_admin_permissions.click_category_submit_button()
    space_admin_permissions.check_created_category("Test category")
    space_admin_permissions.remove_category()
    space_admin_permissions.check_for_no_results()


# this action should be the last one
def test_2_selenium_z_log_out(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.log_out(confluence_webdriver, confluence_datasets)
