from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get('https://www.apple.com/')
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    def get_logo(self):
        return self.driver.find_element(By.XPATH, '//a[@aria-label="Apple"]')

    def get_all_navigation_links_count(self):
        links = []
        links.append(self.driver.find_element(By.XPATH, '//a[@aria-label="Apple"]'))
        menu_text = ['Store', 'Mac', 'iPad', 'iPhone', 'Watch', 'Vision', 'AirPods', 'TV & Home', 'Entertainment', 'Accessories', 'Support']
        for text in menu_text:
            try:
                element = self.driver.find_element(By.XPATH, f'//a[text()="{text}"]')
                links.append(element)
            except:
                element = self.driver.find_element(By.XPATH, f'//a[contains(text(), "{text}")]')
                links.append(element)
        links.append(self.driver.find_element(By.XPATH, '//a[@aria-label="Search apple.com"]'))
        links.append(self.driver.find_element(By.ID, 'globalnav-bag'))
        return len(links)

    def click_button(self):
        iphone_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Learn more, iPhone"]')))
        iphone_button.click()

    def click_shop_button(self):
        shop_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Shop iPhone"]')))
        shop_button.click()