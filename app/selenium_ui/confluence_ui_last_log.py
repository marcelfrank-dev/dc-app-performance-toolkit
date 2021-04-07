import time

from extension.confluence import extension_ui  # noqa F401
from selenium_ui.confluence import modules
# this action should be the first one
from selenium_ui.confluence.pages.pages import LastLogView


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
def test_1_selenium_a_login(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.admin_login(confluence_webdriver)


# ----------------------- LAST LOG ------------------------
def test_1_selenium_browse_last_log_view_action(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.browse_last_log_view_log(confluence_webdriver)


def test_1_selenium_last_log_apply_filter_action(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    last_log_view_page = LastLogView(confluence_webdriver)
    last_log_view_page.remove_log()
    last_log_view_page.apply_filter()
    time.sleep(1)
    last_log_view_page.check_log_exists()
    last_log_view_page.check_log_visibility()


def test_1_selenium_last_log_reload_action(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    last_log_view_page = LastLogView(confluence_webdriver)
    last_log_view_page.remove_log()
    last_log_view_page.reload()
    time.sleep(1)
    last_log_view_page.check_log_exists()
    last_log_view_page.check_log_visibility()


# this action should be the last one
def test_2_selenium_z_log_out(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.log_out(confluence_webdriver, confluence_datasets)
