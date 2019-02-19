from model.contact import Contact

def test_add_contact(app):
        app.contact.create(Contact(name="First contact", last_name="last", mobile_phone="mobile", company="company"))
def test_add_emplty_contact(app):
        app.contact.create(Contact(name="", last_name="", mobile_phone="", company=""))


