from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group for deleting"))
    app.group.delete_first_grpoup()

def test_delete_all_groups(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group for deleting"))
    app.group.delete_all_froups()