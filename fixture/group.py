from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("New")) >0 :
            return
        else:
            wd.find_element_by_link_text("groups").click()

    def fill_group_form(self, group):
        self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header",group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            print(text)
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()


    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        # fill the forms
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()


    def delete_first_grpoup(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def delete_all_froups(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_all_groups()
        wd.find_element_by_name("delete").click()

    def select_all_groups(self):
        wd = self.app.wd
        for i in (wd.find_elements_by_name("selected[]")):
            i.click()

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        group = []
        for el in wd.find_elements_by_css_selector('span.group'):
            text = el.text
            id = el.find_element_by_name("selected[]").get_attribute("value")
            group.append(Group(id = id, name = text))
        return group

