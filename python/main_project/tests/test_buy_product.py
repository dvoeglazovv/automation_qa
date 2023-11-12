# python -m pytest -s -v
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page

@pytest.mark.run(order=3)
def test_buy_product_1(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = (webdriver.Chrome(options=options, service=g))

    print("Start test 1")

    login = Login_page(driver)
    login.authorization()

    main = Main_page(driver)
    main.select_products_1()

    cp = Cart_page(driver)
    cp.confirm_product()

    cip = Client_info_page(driver)
    cip.input_info()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    print("Finish test 1")
    driver.quit()

@pytest.mark.run(order=1)
def test_buy_product_2(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = (webdriver.Chrome(options=options, service=g))

    print("Start test 2")

    login = Login_page(driver)
    login.authorization()

    main = Main_page(driver)
    main.select_products_2()

    cp = Cart_page(driver)
    cp.confirm_product()

    cip = Client_info_page(driver)
    cip.input_info()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    print("Finish test 2")
    driver.quit()

@pytest.mark.run(order=2)
def test_buy_product_3(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = (webdriver.Chrome(options=options, service=g))

    print("Start test 3")

    login = Login_page(driver)
    login.authorization()

    main = Main_page(driver)
    main.select_products_3()

    cp = Cart_page(driver)
    cp.confirm_product()

    cip = Client_info_page(driver)
    cip.input_info()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    print("Finish test 3")
    driver.quit()