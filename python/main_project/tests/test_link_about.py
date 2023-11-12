# python -m pytest -s -v .\tests\test_link_about.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_page
from pages.main_page import Main_page

def test_link_about(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = (webdriver.Chrome(options=options, service=g))

    print("Start test")

    login = Login_page(driver)
    login.authorization()

    main = Main_page(driver)
    main.select_menu_about()

    driver.quit()