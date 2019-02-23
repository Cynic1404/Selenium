from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group for deleting"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_grpoup()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups.pop(0)
    assert new_groups == old_groups


def test_delete_all_groups(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group for deleting"))
    app.group.delete_all_froups()