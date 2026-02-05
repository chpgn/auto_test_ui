from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def check_title(self,title):
        page_title = self.driver.find_element(By.TAG_NAME, 'h1')
        assert page_title.text == title

    def check_products(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, '.product-wrap')
        assert len(products) == 9


