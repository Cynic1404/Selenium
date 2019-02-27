import re
from model.contact import Contact

def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(name="Contact for modification", mobile_phone="+111111111", secondaryphone="44444444",
                    homephone="5455554353", workphone="324234324"))
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_contact_view_page(contact_from_edit_page)
    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_edit_page.last_name == contact_from_edit_page.last_name


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_contact_view_page(contact):
    return "\n".join(filter(lambda x: x is not None,
                     (filter(lambda x: x!= "",
                             map(lambda x: clear(x), [contact.homephone, contact.mobile_phone, contact.workphone, contact.secondaryphone])))))