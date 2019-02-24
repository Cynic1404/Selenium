from model.contact import Contact
from random import randrange

def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name = "Contact for modification"))
    index = randrange(app.contact.count())
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(name="Modified name by index", last_name="Modified last name", mobile_phone="+111111111")
    contact.id = old_contacts[index].id
    old_contacts[index] = contact
    app.contact.modify_contact_by_index(contact, index)
    new_contacts = app.contact.get_contacts_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

