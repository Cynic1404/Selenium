from model.contact import Contact

def test_add_contact(app):
        old_contacts = app.contact.get_contacts_list()
        contact = Contact(name="hhgrdgrghh", last_name="lhhthrfhfast", mobile_phone="mobhfhtfdhfile")
        app.contact.create(contact)
        new_contacts = app.contact.get_contacts_list()
        assert len(new_contacts)-len(old_contacts) == 1
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_emplty_contact(app):
        old_contacts = app.contact.get_contacts_list()
        contact = Contact(name="", last_name="", mobile_phone="", company="")
        app.contact.create(contact)
        new_contacts = app.contact.get_contacts_list()
        assert len(new_contacts) - len(old_contacts) == 1
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



