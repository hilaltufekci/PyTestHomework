from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait # ilgili drverı bekleten kısım
from selenium.webdriver.support import expected_conditions as ec #bekleten koşullar 
from selenium.webdriver.common.action_chains import ActionChains #aksiyonları sıraya koymamıza yardımcı olur.
import pytest


class Test_Sauce5:

     def test_invalid_login(self):
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window()
        usernameInput=driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("locked_out_user")
        passwordInput=driver.find_element(By.ID,"password")
        passwordInput.send_keys("1234")
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"Test Sonucu: {testResult}")

    

