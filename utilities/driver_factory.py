import undetected_chromedriver as uc

class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser.lower() == "chrome":
            options = uc.ChromeOptions()

            return uc.Chrome(options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
