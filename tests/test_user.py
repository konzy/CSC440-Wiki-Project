from unittest import TestCase
from wiki.web.user import UserManager
import os

class UserTestCase(TestCase):
    """
        Tests creating a new json file, and tries to create a new file when one is already made
    """

    def test_new_json_file(self):
        os.remove("tests/users.json")
        um = UserManager("tests")

        um = UserManager("tests")

    """
        Tests creating a new json file, and tries to create a new file when one is already made
    """
    def test_user_read_write_json(self):
        um = UserManager("tests")
        json = um.read()

        assert json is not None

        um.write(json)

        assert um.read() is not None

    def test_user_creation_cleartext(self):
        # print(os.getcwd())

        username = "clear name"
        password = "clear pass"
        um = UserManager("tests")

        cleartext_user = um.add_user(username, password, True, ["admin"], "cleartext")

        assert cleartext_user is not None

    def test_same_name(self):
        username = "clear name"
        password = "clear pass"
        um = UserManager("tests")

        cleartext_user = um.add_user(username, password, True, ["admin"], "cleartext")

        assert cleartext_user is not None

    def test_not_implemented_auth(self):
        username = "none name"
        password = "none pass"
        um = UserManager("tests")

        is_caught = False

        try:
            um.add_user(username, password, True, ["admin"], "asdf")
        except NotImplementedError:
            is_caught = True

        assert is_caught is True

    def test_user_creation_hash(self):
        # print(os.getcwd())

        username = "hash name"
        password = "hash pass"
        um = UserManager("tests")

        hash_user = um.add_user(username, password, True, ["admin"], "hash")

        assert hash_user is not None

    def test_user_get(self):
        username = "get name"
        password = "get pass"
        um = UserManager("tests")

        cleartext_user = um.add_user(username, password, True, ["admin"], "cleartext")

        assert um.get_user(username) is not None

    def test_user_delete(self):
        username = "delete name"
        password = "delete pass"
        um = UserManager("tests")

        cleartext_user = um.add_user(username, password, True, ["admin"], "cleartext")

        assert um.get_user(username) is not None

        um.delete_user(username)

        assert um.get_user(username) is None

        assert um.delete_user("user never has been created") is False

    def test_user_update(self):
        username = "update name"
        password = "update pass"
        um = UserManager("tests")

        cleartext_user = um.add_user(username, password, True, ["admin"], "cleartext")

        data = cleartext_user.data

        um.update(username, data)


    def test_simple_user(self):
        """
            Assert a simple User is created correctly.
        """
        name = 'Hash'
        password = 'password'
        active = True
        roles = ['Admin']
        authentication_method = 'hash'
        user_manager = UserManager('')
        hash_user = user_manager.add_user(name, password, active, roles, authentication_method)

        assert hash_user.is_active()

        assert hash_user.is_authenticated() is False

        hash_user.set('authenticated', True)
        assert hash_user.get('authenticated')

        assert hash_user.get_id() == name

        assert hash_user.is_anonymous() is False

        assert hash_user.check_password(password)

        name2 = 'Test2'
        authentication_method2 = 'cleartext'
        clear_user = user_manager.add_user(name2, password, active, roles, authentication_method2)
        assert clear_user.check_password(password)

        assert hash_user.check_password('hi') is False

        hash_user.set('authentication_method', 'hi')
        is_caught = False
        try:
            hash_user.check_password('hi')
        except NotImplementedError:
            is_caught = True
        assert is_caught






