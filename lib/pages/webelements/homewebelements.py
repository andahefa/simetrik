from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.CSS_SELECTOR, '.primary-content h2')
    signin_button = (By.CSS_SELECTOR, '.menu__wrapper .menu-label__wrapper button')
    search_button = (
        By.CSS_SELECTOR, '.pageContent .SearchPage__FrontDoor .HPw7-form-fields-and-submit .HPw7-submit button')
    origin_input = (By.XPATH,
                    "//input[@aria-label='Origen']")
    destination_input = (By.XPATH, "//input[@aria-label='Destino']")
    start_date_span = (By.XPATH, "//span[@aria-label='Fecha de inicio en el calendario']")
    fin_date_span = (By.XPATH, "//span[@aria-label='Fecha final en el calendario']")
    search_button = (By.XPATH, "//div[@class='zEiP-formField zEiP-submit']//button[@type='submit']")

    @staticmethod
    def getElementOption(option_name):
        option_locator = (By.XPATH, f"//div[text()='{option_name}']")
        return option_locator
