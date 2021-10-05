from pages.landing_page import LandingPage
from pages.fridge_door_page import FridgeDoorPage
from pages.login_page import LoginPage
from pages.header_bar_page import HeaderBarPage
from pages.cart_page import CartPage
from pages.collections_page import CollectionsPage
from pages.product_list_page import ProductListPage
from pages.product_page import ProductPage
import allure


@allure.feature("Check user can Log In to the system and add product to the cart")
def test_add_product_to_cart(browser):
    email = "Brad_br+04@onevillage.io"
    passwd = "1234567890_OV"
    with allure.step("Open Landing page"):
        landing_page = LandingPage(browser)
        landing_page.open_landing_page()
    with allure.step("Open Log In page"):
        landing_page.open_login_page()
    with allure.step("Check Log In page displays"):
        login_page = LoginPage(browser)
        login_page.should_be_login_page()
    with allure.step("Log In user to the system"):
        login_page.login(email, passwd)
    with allure.step("Check Fridge Door page is open"):
        fridge_door_page = FridgeDoorPage(browser)
        fridge_door_page.should_be_fridge_page()
    with allure.step("Open Cart page"):
        header_bar_page = HeaderBarPage(browser)
        header_bar_page.open_cart_page()
    with allure.step("Check cart is empty"):
        cart_page = CartPage(browser)
        cart_page.check_cart_is_empty()
    with allure.step("Open Collections page"):
        cart_page.open_collections()
        collections_page = CollectionsPage(browser)
        collections_page.should_be_collections_page()
    with allure.step("Open Meal Delivery Section in collections"):
        collections_page.open_meal_delivery_section()
        product_list_page = ProductListPage(browser)
        product_list_page.should_be_product_list_page()
    with allure.step("Open product page"):
        product_list_page.open_product_page()
    with allure.step("Add product to the cart"):
        product_page = ProductPage(browser)
        product_page.add_product_to_cart()
    with allure.step("Open Cart page"):
        header_bar_page.open_cart_page()
    with allure.step("Check product in cart"):
        cart_page.check_product_in_cart()
