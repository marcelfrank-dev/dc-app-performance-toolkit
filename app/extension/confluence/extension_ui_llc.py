from selenium_ui.base_page import BasePage
from selenium_ui.confluence import modules


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_pages']:
        app_specific_page_id = datasets['custom_page_id']

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out
    # @print_timing("selenium_app_specific_user_login")
    # def measure():
    #     def app_specific_user_login(username='admin', password='admin'):
    #         login_page = Login(webdriver)
    #         login_page.delete_all_cookies()
    #         login_page.go_to()
    #         login_page.wait_for_page_loaded()
    #         login_page.set_credentials(username=username, password=password)
    #         login_page.click_login_button()
    #         if login_page.is_first_login():
    #             login_page.first_user_setup()
    #         all_updates_page = AllUpdates(webdriver)
    #         all_updates_page.wait_for_page_loaded()
    #     app_specific_user_login(username='admin', password='admin')
    # measure()

    # ----------------------- ADMIN MODE ------------------------
    def test_1_selenium_a_login(webdriver, datasets):
        modules.admin_login(webdriver)

    test_1_selenium_a_login(webdriver, datasets)

    def test_10_selenium_browse_last_log_view_action(webdriver, datasets):
        modules.last_log_view_log(webdriver)

    test_10_selenium_browse_last_log_view_action(webdriver, datasets);

    def test_20_selenium_last_log_apply_filter_action(webdriver, datasets):
        modules.last_log_apply_filter(webdriver)

    test_20_selenium_last_log_apply_filter_action(webdriver, datasets);

    def test_30_selenium_last_log_reload_action(webdriver, datasets):
        modules.last_log_reload_action(webdriver)

    test_30_selenium_last_log_reload_action(webdriver, datasets);