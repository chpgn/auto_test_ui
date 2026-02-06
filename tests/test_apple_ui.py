from pages.homepage import HomePage
from pages.product import ProductPage


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