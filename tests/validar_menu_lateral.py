from time import sleep

import elementos.menu_lateral
from helpers.helper import AppiumHelper
from elementos.idle import Idle
from elementos.menu_lateral import MenuLateral
import pytest, pytest_html
from pagina.pag_menu_lateral import PagMenuLateral
from drivers import desired_capabilities, constants
from appium import webdriver
from appium.options.android import UiAutomator2Options

def validar_menu__lateral():
    # inicia só 1 vez
    cap = desired_capabilities.capabilities()
    options = UiAutomator2Options()
    options.load_capabilities(cap)
    driver = webdriver.Remote(constants.SERVER_URL_BASE, options=options)
    helper = AppiumHelper(driver)
    idle = Idle()
    menu_lateral = MenuLateral()
    print(helper.clicar_tag(idle.btn_menu_idle))
    print(helper.verificar_tag(menu_lateral.btn_resend_receipt_menu))
    print(helper.verificar_tag(menu_lateral.btn_refund_menu))
    print(helper.verificar_tag(menu_lateral.btn_reports_menu))
    print(helper.verificar_tag(menu_lateral.btn_manage_terminal_menu))
    print(helper.verificar_tag(menu_lateral.btn_developer_options_menu))
    print(helper.clicar_tag(menu_lateral.btn_manage_terminal_menu))
    print(helper.verificar_tag(menu_lateral.btn_merchant_info_menu))
    print(helper.verificar_tag(menu_lateral.btn_operators_menu))
    print(helper.verificar_tag(menu_lateral.btn_initialization_menu))
    print(helper.verificar_tag(menu_lateral.btn_apps_menu))
    print(helper.verificar_tag(menu_lateral.btn_test_menu))
    print(helper.verificar_tag(menu_lateral.btn_reset_data_menu))
    print(helper.ir_a_tag(menu_lateral.btn_export_data_menu))
    print(helper.verificar_tag(menu_lateral.btn_export_data_menu))
    print(helper.verificar_tag(menu_lateral.btn_last_error_menu))
    print(helper.verificar_tag(menu_lateral.btn_settings_menu))
    print(helper.clicar_tag(menu_lateral.btn_settings_menu))
    print(helper.verificar_tag(menu_lateral.btn_app_information_menu))
    print(helper.verificar_tag(menu_lateral.btn_device_menu))
    print(helper.verificar_tag(menu_lateral.btn_supervisor_options_menu))


validar_menu__lateral()