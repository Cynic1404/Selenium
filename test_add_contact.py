# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from selenium import webdriver
from time import sleep
from contact import Contact



class test_add_contact(unittest.TestCase):
    def setUp(self):
        #self.wd = webdriver.Chrome("C:\Python\chromedriver.exe")
        self.wd = WebDriver(capabilities={"marionette": False})
        #self.wd = webdriver.Firefox("C:\Python\geckodriver.exe")
        #self.wd = webdriver.Edge("C:\Python\MicrosoftWebDriver.exe")
        self.wd.implicitly_wait(60)


    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_contact(wd, Contact(name="First contact", last_name="last", mobile_phone="mobile", company="company"))
        self.logout(wd)

    def test_add_emplty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_contact(wd, Contact(name="", last_name="", mobile_phone="", company=""))
        self.logout(wd)

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


    def add_contact(self, wd, contact):
        wd.find_element_by_xpath('//*[@id="nav"]/ul/li[2]/a').click()
        wd.find_element_by_xpath('//*[@id="content"]/form/input[3]').send_keys(contact.name)
        wd.find_element_by_xpath('//*[@id="content"]/form/input[5]').send_keys(contact.last_name)
        wd.find_element_by_xpath('//*[@id="content"]/form/input[11]').send_keys(contact.mobile_phone)
        wd.find_element_by_xpath('//*[@id="content"]/form/input[9]').send_keys(contact.company)
        wd.find_element_by_xpath('// *[ @ id = "content"] / form / input[1]').click()
        sleep(3)


    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()