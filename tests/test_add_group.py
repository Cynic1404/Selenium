import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.add_group(Group(name ="First class group", header ="First class header", footer ="Firt class footer"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.add_group(Group(name="", header="", footer=""))
    app.logout()

