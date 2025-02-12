from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginIn:
    def __init__(self, driver):
        self.driver = driver
    def authorization(self, login_name, login_password):
        # вводит имя пользователя
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        user_name.send_keys(login_name)
        print('Input Login')

        # вводит пароль
        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, "password")))
        password.send_keys(login_password)
        print('Input password')

        # авторизуется
        password.send_keys(Keys.ENTER)
        print('Logged in')
