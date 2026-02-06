from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def check_title(self,title):
        page_title = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
        assert page_title.text == title

    def check_products_count(self, count):
        products = self.wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, '.product-wrap'))
        assert len(products) == count

    def check_title_shop(self,title):
        page_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.rs-shop-header')))
        assert page_title.text.strip() == title
