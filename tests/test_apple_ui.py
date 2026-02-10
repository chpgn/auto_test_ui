from pages.homepage import HomePage
from pages.product import ProductPage
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_navigation_menu(driver):
    homepage = HomePage(driver)
    homepage.open()
    nav = driver.find_element(By.ID, 'globalnav')
    assert nav.is_displayed()
    print('navigation menu opened')

def test_open_iphone(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_button()
    product_page = ProductPage(driver)
    product_page.check_title('iPhone')

def test_nine_products(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_button()
    product_page = ProductPage(driver)
    product_page.check_products_count(9)

def test_open_shop_iphone(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_shop_button()
    product_page = ProductPage(driver)
    product_page.check_title_shop('Shop iPhone')