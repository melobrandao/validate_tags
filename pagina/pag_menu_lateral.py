from elementos.menu_lateral import MenuLateral
from helpers.helper import AppiumHelper

class PagMenuLateral:
    def __init__(self, driver):
        self.helper = AppiumHelper(driver)
    def botao_estorno(self):
        return self.helper.verificar_tag(MenuLateral.btn_refund_menu)

    def botao_reenviar_comp(self):
        return self.helper.verificar_tag(MenuLateral.btn_resend_receipt_menu)

    def botao_relatorio(self):
        return self.helper.verificar_tag(MenuLateral.btn_reports_menu)

    def botao_gerir_terminal(self):
        return self.helper.verificar_tag(MenuLateral.btn_manage_terminal_menu)

    def botao_dev(self):
        return self.helper.verificar_tag(MenuLateral.btn_developer_options_menu)

    def botao_merchant_info(self):
        return self.helper.verificar_tag(MenuLateral.btn_merchant_info_menu)

    def botao_operators(self):
        return self.helper.verificar_tag(MenuLateral.btn_operators_menu)

    def botao_initialization(self):
        return self.helper.verificar_tag(MenuLateral.btn_initialization_menu)

    def botao_apps(self):
        return self.helper.verificar_tag(MenuLateral.btn_apps_menu)

    def botao_test(self):
        return self.helper.verificar_tag(MenuLateral.btn_test_menu)

    def botao_reset_data(self):
        return self.helper.verificar_tag(MenuLateral.btn_reset_data_menu)

    def botao_export_data(self):
        return self.helper.verificar_tag(MenuLateral.btn_export_data_menu)

    def botao_last_error(self):
        return self.helper.verificar_tag(MenuLateral.btn_last_error_menu)

    def botao_settings(self):
        return self.helper.verificar_tag(MenuLateral.btn_settings_menu)

    def botao_app_information(self):
        return self.helper.verificar_tag(MenuLateral.btn_app_information_menu)

    def botao_device(self):
        return self.helper.verificar_tag(MenuLateral.btn_device_menu)

    def botao_supervisor_options(self):
        return self.helper.verificar_tag(MenuLateral.btn_supervisor_options_menu)

'''
pagina = PagMenuLateral()
print(pagina.botao_estorno())
print(pagina.botao_reenviar_comp())
print(pagina.botao_relatorio())
print(pagina.botao_gerir_terminal())
print(pagina.botao_dev())
print(pagina.botao_apps())
print(pagina.botao_initialization())
print(pagina.botao_operators())
print(pagina.botao_reset_data())
print(pagina.botao_app_information())
print(pagina.botao_last_error())
print(pagina.botao_test())
print(pagina.botao_device())
print(pagina.botao_supervisor_options())
'''