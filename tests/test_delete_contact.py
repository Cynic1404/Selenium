from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Contact for deleting"))
    index = randrange(app.contact.count())
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.pop(index)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



# def test_delete_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(name = "Contact for deleting", mobile_phone="+111111111", secondaryphone="44444444", homephone="5455554353", workphone="324234324"))
#     old_contacts = app.contact.get_contacts_list()
#     app.contact.delete_first_contact()
#     assert len(old_contacts) - 1 == app.contact.count()
#     new_contacts = app.contact.get_contacts_list()
#     old_contacts.pop(0)
#     assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts, key=Contact.id_or_max)


# def test_delete_all_contacts(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(name = "Contact for deleting", mobile_phone="+111111111", secondaryphone="44444444", homephone="5455554353", workphone="324234324"))
#     app.contact.delete_all_contacts()
#     assert app.contact.count() == 0
#
