from model.group import Group
from random import randrange

def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group for modification"))
    index = randrange(app.group.count())
    old_groups = app.group.get_group_list()
    group = Group(name ="Modified name", header="Modified header", footer="Modifiesd footer")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(group, index)
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)



def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group for modification"))
    old_groups = app.group.get_group_list()
    group = Group(name ="New name")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group for modification"))
    app.group.modify_first_group(Group(header="new header"))


