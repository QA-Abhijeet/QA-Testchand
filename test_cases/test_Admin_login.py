import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_AdminPage import Login_AdminPage  #To get locaters
from utilities.custom_logger import Log_maker #to get logs


class Test_01_Admin_Login:
    admin_loginPage_url = "https://admin-demo.nopcommerce.com/"
    Email = "admin@yourstore.com"
    password = "admin"
    invalid_username = "adminInvalid@yourstore.com"
    logger = Log_maker.log_gen()  #to get logs

    def test_Title_Verification(self, setup):
        self.logger.info("*************Test_01_Admin_Login*************")  #to get logs
        self.driver = setup

        self.driver.get(self.admin_loginPage_url)
        time.sleep(3)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Title_Verification.png")
            self.logger.info("*************test_Title_Verification_failed*************")  #to get logs
            self.driver.close()
            assert False

    def test_login_valid(self, setup):
        self.driver = setup

        self.driver.get(self.admin_loginPage_url)
        time.sleep(3)
        self.admin_lp = Login_AdminPage(self.driver)
        self.admin_lp.enter_username(self.Email)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.implicitly_wait(10)
        self.driver.find_elements(By.XPATH,"/html/body//div[1]/div/div[1]/div/label/input").click()

        act_dashboard_text = self.driver.title

        if act_dashboard_text == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login_valid.png")
            self.logger.info("*************test_login_valid_failed*************")  #to get logs
            self.driver.close()
            assert False

    def test_login_invalid(self, setup):
        self.driver = setup

        self.driver.get(self.admin_loginPage_url)
        time.sleep(3)
        self.admin_lp = Login_AdminPage(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.implicitly_wait(10)
        self.driver.find_elements(By.XPATH, "/html/body//div[1]/div/div[1]/div/label/input").click()

        error_message = self.driver.find_element(By.XPATH,"//li[normalize-space()='No customer account found']").text
        if error_message == "No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login_invalid.png")
            self.logger.info("*************test_login_invalid_failed*************")  #to get logs
            self.driver.close()
            assert False
