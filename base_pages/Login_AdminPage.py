from selenium.webdriver.common.by import By


class Login_AdminPage:
    textbox_Email_Xpath = "//input[@id='Email']"
    textbox_password_Xpath = "//input[@id='Password']"
    button_login_Xpath = "//button[normalize-space()='Log in']"

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(By.XPATH,self.textbox_Email_Xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Email_Xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_Xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_Xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_Xpath).click()