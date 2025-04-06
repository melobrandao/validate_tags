from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from drivers.constants import SERVER_URL_BASE
from drivers.desired_capabilities import capabilities


class AppiumHelper:
    def __init__(self):
        cap = capabilities()
        options = UiAutomator2Options()
        options.load_capabilities(cap)
        self.driver = webdriver.Remote(SERVER_URL_BASE, options=options)

    def verificar_tag(self, accessibility_id: str) -> str:
        try:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, accessibility_id)
            return f"✅ Tag '{accessibility_id}' encontrada!"
        except NoSuchElementException:
            return f"❌ Tag '{accessibility_id}' NÃO encontrada!"
        except Exception as e:
            return f"⚠️ Erro ao procurar tag '{accessibility_id}': {e}"

    def 