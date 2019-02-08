# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
import pytest
from group import Group
from application import Application
from selenium import webdriver


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

