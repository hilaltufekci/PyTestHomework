from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.action_chains import ActionChains 
import pytest

class Test_Sauce8:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_invalid_login(self,username,password):
        usernameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click() 
        headerLogo=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='header_container']/div[1]/div[2]/div")))
        testResult=headerLogo.text =="Swag Labs"     
        self.driver.execute_script("window.scrollTo(0,500)")
        addToCart=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")))
        addToCart.click()
        shoppingCart=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='shopping_cart_container']/a")))
        shoppingCart.click()
        headerContainer=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH," //*[@id='header_container']/div[2]/span ")))
        assert headerContainer.text =="Your Cart" 
        openMenu=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH," //*[@id='react-burger-menu-btn']")))
        openMenu.click()
        aboutButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"about_sidebar_link")))
        aboutButton.click()
        headerName=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH," //*[@id='__next']/header/div/div/div[1]/div[2]/div/div[1]/div[1]/div[1]/span")))
        assert headerName.text =="Products" 
        sleep (10)    


   
                                                                            
                                                                                        
