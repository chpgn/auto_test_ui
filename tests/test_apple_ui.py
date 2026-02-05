from selenium.webdriver.common.by import By

import time
from pages.homepage import HomePage
from pages.product import ProductPage



def test_open_iphone(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_button()
    # driver.get('https://www.apple.com/')
    # iphone_button = driver.find_element(By.XPATH, '//a[@aria-label="Learn more, iPhone"]')
    # iphone_button.click()
    time.sleep(3) # переписать на лучший вариант
    product_page = ProductPage(driver)
    product_page.check_title('iPhone')
    # title = driver.find_element(By.TAG_NAME, 'h1' )
    # assert title.text == 'iPhone'

def test_nine_products(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_button()
    # driver.get('https://www.apple.com/')
    # iphone_button = driver.find_element(By.XPATH, '//a[@aria-label="Learn more, iPhone"]')
    # iphone_button.click()
    time.sleep(3) # переписать на лучший вариант
    products = driver.find_elements(By.CSS_SELECTOR, '.product-wrap')
    assert len(products) == 9

