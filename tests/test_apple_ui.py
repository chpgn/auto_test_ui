from pages.homepage import HomePage
from pages.product import ProductPage
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Проверка отображения навигационного меню:
# открывает главную страницу → проверяет что меню отображается на странице
def test_navigation_menu(driver):
    homepage = HomePage(driver)
    homepage.open()
    nav = driver.find_element(By.ID, 'globalnav')
    assert nav.is_displayed()
    print('navigation menu opened')

# Проверка количества ссылок в навигационном меню:
# открывает главную страницу → подсчитывает все ссылки (логотип, пункты меню, иконки)
def test_navigation_links_count(driver):
    homepage = HomePage(driver)
    homepage.open()
    links_count = homepage.get_all_navigation_links_count()
    assert links_count == 14, f"navigation {links_count} links, count 14"
    print(f"navigation links count: {links_count}")
    # print('navigation links count opened') упрощённый способ

# Переход на страницу iPhone через кнопку 'Learn more':
# открывает главную страницу → кликает по кнопке 'Learn more, iPhone' → проверяет что открылась страница iPhone с заголовком 'iPhone'
def test_open_iphone(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_button()
    product_page = ProductPage(driver)
    product_page.check_title('iPhone')

# Проверка количества продуктов на странице iPhone:
# открывает главную страницу → переходит на страницу iPhone по кнопке 'Learn more' → подсчитывает все элементы с классом 'product-wrap' → проверяет что их количество
def test_nine_products(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_button()
    product_page = ProductPage(driver)
    product_page.check_products_count(9)

# Переход в магазин iPhone через кнопку 'Shop iPhone':
# открывает главную страницу → кликает по кнопке 'Shop iPhone' → проверяет что открылась страница магазина с заголовком 'Shop iPhone'
def test_open_shop_iphone(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_shop_button()
    product_page = ProductPage(driver)
    product_page.check_title_shop('Shop iPhone')