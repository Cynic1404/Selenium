from fixture.application import Application
import pytest
from model.contact import Contact
from fixture.session import SessionHelper



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(name="First contact", last_name="last", mobile_phone="mobile", company="company"))
        app.session.logout()

def test_add_emplty_contact(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(name="", last_name="", mobile_phone="", company=""))
        app.session.logout()

