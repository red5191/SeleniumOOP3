# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)
# pip3 install faker (Устанавливаем библиотеку faker)

# импортируем необходимые библиотеки и элементы
import time
# from datetime import datetime, timedelta
# from faker import Faker
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page_login import LoginIn


# создаем класс который:
class AutoTest:

    def __init__(self, link, headless=False):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        if headless:
            self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))
        self.base_url = link

    def test_start(self):
        # запускает драйвер по указанной ссылке
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        # производит авторизацию
        login_in = LoginIn(self.driver)
        login_in.authorization(login_name = 'standard_user', login_password = 'secret_sauce')

    def business_process(self):
        # выбирает товар
        select_product = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print('Select product')

        # открывает корзину
        button_cart_link = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-test='shopping-cart-link']")))
        button_cart_link.click()
        print('Enter Cart')

        # проверяет что он в корзине
        page_test = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        page_title = page_test.text
        assert page_title == 'Your Cart'
        print('Title matches')


    # завершает тест и закрывает браузер
    def test_end(self, seconds=5):
        time.sleep(seconds)
        self.driver.quit()

# вызываем экземпляр класса и методы
base_url = 'https://www.saucedemo.com/'
test = AutoTest(base_url, headless=False)
test.test_start()
test.test_end()