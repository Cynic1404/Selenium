from model.contact import Contact
import pytest
import string
import random
from random import randint

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+" "
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

def random_phone():
    return "+" + str(randint(1,10)) + "-" + "".join([random.choice(string.digits) for i in range(3)]) + "-" + "".join([random.choice(string.digits) for i in range(3)])+"-"+"".join([random.choice(string.digits) for i in range(2)])+"-"+"".join([random.choice(string.digits) for i in range(2)])

def random_email():
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(1,10))])+"@"+ "".join([random.choice(symbols) for i in range(random.randrange(1,10))]) + random.choice([".ru", ".com"])


testdata = [Contact(name="", last_name="", address="")]+\
           [Contact(name=random_string("name", 10), last_name=random_string("lastname",10),
                    homephone=random_phone(), mobile_phone=random_phone(), workphone=random_phone(), secondaryphone= random_phone(),
                    email=random_email(), email2=random_email(), email3=random_email()) for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids = [repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert app.contact.count() - len(old_contacts) == 1
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)





# def test_add_contact(app):
#         old_contacts = app.contact.get_contacts_list()
#         contact = Contact(name="11", last_name="11zxvzv", mobile_phone="+th", secondaryphone="ht", homephone="gt", workphone="54y", address="825 Marshall sthtrht")
#         app.contact.create(contact)
#         new_contacts = app.contact.get_contacts_list()
#         assert app.contact.count()-len(old_contacts) == 1
#         old_contacts.append(contact)
#         assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#
#
# def test_add_empty_contact(app):
#         old_contacts = app.contact.get_contacts_list()
#         contact = Contact(name="", last_name="", mobile_phone="", company="")
#         app.contact.create(contact)
#         new_contacts = app.contact.get_contacts_list()
#         assert app.contact.count() - len(old_contacts) == 1
#         old_contacts.append(contact)
#         assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#
#
#
