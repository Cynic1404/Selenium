from model.contact import Contact

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
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("company", contact.mobile_phone)



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
        return Contact(name= name, last_name=lastname, homephone=homephone, mobile_phone=mobile_phone, workphone=workphone, secondaryphone=secondaryphone, id=id)




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
                all_phones = cells[5].text.splitlines()
                homephone = all_phones[0]
                mobile_phone = all_phones[1]
                workphone = all_phones[2]
                secondaryphone = all_phones[3]


                self.contacts_cache.append(Contact(id = id, name=first_name, last_name=last_name, homephone=homephone, mobile_phone=mobile_phone, workphone=workphone,secondaryphone=secondaryphone))
        return self.contacts_cache

