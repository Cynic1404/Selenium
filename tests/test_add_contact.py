from model.contact import Contact

def test_add_contact(app):
        old_contacts = app.contact.get_contacts_list()
        contact = Contact(name="11", last_name="11zxvzv", mobile_phone="+th", secondaryphone="ht", homephone="gt", workphone="54y", address="825 Marshall sthtrht")
        app.contact.create(contact)
        new_contacts = app.contact.get_contacts_list()
        assert app.contact.count()-len(old_contacts) == 1
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
        old_contacts = app.contact.get_contacts_list()
        contact = Contact(name="", last_name="", mobile_phone="", company="")
        app.contact.create(contact)
        new_contacts = app.contact.get_contacts_list()
        assert app.contact.count() - len(old_contacts) == 1
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



