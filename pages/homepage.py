from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.apple.com/')

    def click_button(self):
        iphone_button = self.driver.find_element(By.XPATH, '//a[@aria-label="Learn more, iPhone"]')
        iphone_button.click()