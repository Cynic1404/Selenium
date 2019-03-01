from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium import webdriver


class Application: #constructor of fixture
    def __init__(self, browser = "chrome"):
        if browser == "chrome":
            self.wd = webdriver.Chrome("C:\Python\chromedriver.exe")
        elif browser == "firefox":
            self.wd = WebDriver(capabilities={"marionette": False})
        else:
            raise ValueError ("Unrecognized browser %s" % browser)

        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")



    def destroy(self): #
        self.wd.quit()

