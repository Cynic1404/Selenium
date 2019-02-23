
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name ="First class group", header ="First class header", footer ="Firt class footer")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    print("ok")


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    new_group = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


