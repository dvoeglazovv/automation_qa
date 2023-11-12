from base.base_class import Base
from utilities.logger import Logger

class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    # Getters

    # Actions

    # Methods
    def finish(self):
        Logger.add_start_step(method="finish")
        self.get_current_url()
        self.get_screenshot()
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")
        Logger.add_end_step(url=self.driver.current_url, method="finish")