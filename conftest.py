from fixture.application import Application
import pytest


fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None:
        fixture = Application(browser = browser)
    else:
        if not fixture.is_valid():
            fixture = Application(browser = browser)
    fixture.session.ensure_login(username="admin", password="secret")

    return fixture

@pytest.fixture (scope = "session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
	parser.addoption("--browser" , action = "store", default = "chrome")
