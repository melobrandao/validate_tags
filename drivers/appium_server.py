from appium.webdriver.appium_service import AppiumService

class AppiumServer:
    service: AppiumService = None

    @classmethod
    def __init_service(cls):
        if cls.service is None:
            cls.service = AppiumService()

    @classmethod
    def setup_appium(cls) -> str:
        cls.__init_service()

        if cls.service.is_running:
            return "⚠️ Servidor Appium já está rodando."
        else:
            try:
                cls.service.start()
                if cls.service.is_running:
                    return "✅ Servidor Appium iniciado com sucesso."
                else:
                    return "❌ Falha ao iniciar o servidor Appium."
            except Exception as e:
                return f"❌ Erro ao iniciar Appium: {e}"

    @classmethod
    def tear_appium(cls) -> str:
        cls.__init_service()

        if cls.service.is_running:
            cls.service.stop()
            return "🛑 Servidor Appium parado com sucesso."
        else:
            return "⚠️ Servidor Appium já estava parado."


