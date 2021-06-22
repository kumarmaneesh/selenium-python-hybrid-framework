class LoginPage:

    txt_username_id="Email"
    txt_password_id="Password"
    btn_login_xpath="//button[@class='button-1 login-button']"
    lnk_logout_linktext="Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.txt_username_id).clear()
        self.driver.find_element_by_id(self.txt_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.txt_password_id).clear()
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.lnk_logout_linktext).click()
