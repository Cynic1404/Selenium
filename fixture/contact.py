from model.contact import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="nav"]/ul/li[2]/a').click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath('// *[ @ id = "content"] / form / input[1]').click()
        self.contacts_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("company", contact.company)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)



    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath('//*[@id="maintable"]/tbody/tr[2]/td[8]/a/img').click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.open_contacts_page()
        self.contacts_cache = None

    def modify_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_name("entry")[index].find_elements_by_tag_name("td")[7].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.open_contacts_page()
        self.contacts_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_name("entry")[index].find_elements_by_tag_name("td")[7].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(name= name, last_name=lastname, homephone=homephone, mobile_phone=mobile_phone,
                       address=address, workphone=workphone, secondaryphone=secondaryphone, id=id,
                       email = email, email2 = email2, email3 =email3)




    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None



    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def open_contacts_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("addressbook/"):
            return
        else:
            wd.find_element_by_xpath('//*[@id="nav"]/ul/li[1]/a').click()

    def select_all_contacts(self):
        wd = self.app.wd
        for i in (wd.find_elements_by_name("selected[]")):
            i.click()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_all_contacts()
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))


    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache == None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contacts_cache = []
            for el in wd.find_elements_by_name("entry"):
                id = el.find_element_by_name("selected[]").get_attribute("value")
                cells = el.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                all_phones = cells[5].text
                address = cells[3].text
                all_emails = cells[4].text
                self.contacts_cache.append(Contact(id = id, name=first_name, last_name=last_name,
                                                   all_phones=all_phones, address=address, all_emails = all_emails))
        return self.contacts_cache

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_name("entry")[index].find_elements_by_tag_name("td")[6].click()


    def contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondaruphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobile_phone=mobile_phone,secondaryphone=secondaruphone)