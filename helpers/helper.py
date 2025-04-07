from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from drivers.constants import SERVER_URL_BASE
from drivers.desired_capabilities import capabilities

class AppiumHelper:
    def __init__(self, driver = None):
        if driver:
            self.driver = driver
        else:
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

    def clicar_tag(self, accessibility_id: str) -> str:
        try:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, accessibility_id).click()
            return f"✅ Tag {accessibility_id} selecionada"
        except NoSuchElementException:
            return f"❌ Tag '{accessibility_id}' NÃO encontrada!"
        except Exception as e:
            return f"⚠️ Erro ao selecionar tag '{accessibility_id}': {e}"

    def ir_a_tag(self, accessibility_id: str) -> str:
        try:
            self.driver.execute_script("mobile: scroll", {
                "strategy": "accessibility id",
                "selector": accessibility_id
            })
            return f"✅ Scroll realizado até a tag '{accessibility_id}'"

        except NoSuchElementException:
            return f"❌ Tag '{accessibility_id}' NÃO encontrada para scroll."

        except Exception as e:
            return f"⚠️ Erro ao fazer scroll até a tag '{accessibility_id}': {e}"
