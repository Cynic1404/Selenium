from selenium.webdriver.firefox.webdriver import WebDriver


class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def add_group(self, group):
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        # fill the forms
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submt group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def add_contact(self, contact):
        wd = self.wd
        wd.find_element_by_xpath('//*[@id="nav"]/ul/li[2]/a').click()
        wd.find_element_by_xpath('//*[@id="content"]/form/input[3]').send_keys(contact.name)
        wd.find_element_by_xpath('//*[@id="content"]/form/input[5]').send_keys(contact.last_name)
        wd.find_element_by_xpath('//*[@id="content"]/form/input[11]').send_keys(contact.mobile_phone)
        wd.find_element_by_xpath('//*[@id="content"]/form/input[9]').send_keys(contact.company)
        wd.find_element_by_xpath('// *[ @ id = "content"] / form / input[1]').click()

    def destroy(self):
        self.wd.quit()

