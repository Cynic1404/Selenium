class ContactHelper:
    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="nav"]/ul/li[2]/a').click()
        wd.find_element_by_xpath('//*[@id="content"]/form/input[3]').send_keys(contact.name)
        wd.find_element_by_xpath('//*[@id="content"]/form/input[5]').send_keys(contact.last_name)
        wd.find_element_by_xpath('//*[@id="content"]/form/input[11]').send_keys(contact.mobile_phone)
        wd.find_element_by_xpath('//*[@id="content"]/form/input[9]').send_keys(contact.company)
        wd.find_element_by_xpath('// *[ @ id = "content"] / form / input[1]').click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        wd.switch_to_alert().accept()

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="nav"]/ul/li[1]/a').click()

