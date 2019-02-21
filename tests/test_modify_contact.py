from model.contact import Contact

def test_modify_firs_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name = "Contact for modification"))
    app.contact.modify_first_contact(Contact(name="Modified name", last_name="Modified last name", mobile_phone="+111111111"))

