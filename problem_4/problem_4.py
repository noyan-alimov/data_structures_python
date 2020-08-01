class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    users = group.get_users()
    if user in users:
        return True

    groups = group.get_groups()
    for gr in groups:
        return is_user_in_group(user, gr)

    return False


def test_function_true(user, group):
    result = is_user_in_group(user, group)
    if result:
        print('Test success')
    else:
        print('Test failed')

def test_function_false(user, group):
    result = is_user_in_group(user, group)
    if result is False:
        print('Test success')
    else:
        print('Test failed')

def test_function_error(user, group):
    try:
        is_user_in_group(user, group)
    except AttributeError:
        print('Test success')
    else:
        print('Test failed')



parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child2 = Group("subchild2")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
child.add_group(sub_child2)
parent.add_group(child)


test_function_true(sub_child_user, parent) # expect to return True
test_function_false('', parent) # expect to return False
test_function_error('hi', '') # expect to show an attribute error