from unittest import TestCase

from wiki.web import user
from wiki.web.routes import bp
from wiki.web.user import UserManager, protect


class UserTestCase(TestCase):
    """
        Contains various tests for the wiki.web.user.User class.
    """

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






