"""Your test suite. Write smoke, regression, and slow tests here.

Every test MUST carry exactly one marker (@pytest.mark.smoke / regression /
slow) and name its author in the docstring, e.g.:

    @pytest.mark.smoke
    def test_login_works():
        '''Author: <name>. Smoke test for login.'''

Run:  pytest            (all)     pytest -m smoke     pytest -m regression
"""
    
import pytest
from bookstore_app import Users, Catalog, Cart


@pytest.mark.smoke
def test_example_register():
    """Author: <example>. Smoke: a new user can register."""
    assert Users().register("newuser", "password123") is True


# ---- YOUR SMOKE TESTS (at least 5) ----
@pytest.mark.smoke
def test_smoke_register_new_user_and_reject_duplicate():
    """Author: Aung San Thu Rain Tun. Smoke: registration succeeds for a new user, the
    account is actually stored, and a duplicate username is refused.
    Catches: 'user registration always fails'."""
    users = Users()
    assert users.register("alice", "secret123") is True
    assert "alice" in users.users      
    assert users.register("alice", "other456") is False

# ---- YOUR REGRESSION TESTS (the bug hunt) ----
@pytest.mark.regression
def test_login_must_not_strip_characters_from_password():
    """Author: <ASTRH>. Regression for Users.login.
    Observed: login() strips every non-alphanumeric character from the
    supplied password before comparing. A user who registered "p@ss!word"
    can never log in (returns False), and a wrong password containing extra
    symbols, "a-b-c-1-2-3", is accepted for the real password "abc123".
    Expected: the password must match exactly as registered."""
    users = Users()
    users.register("dave", "p@ss!word")
    users.register("eve", "abc123")
    assert users.login("dave", "p@ss!word") is True
    assert users.login("eve", "abc123") is True
    assert users.login("eve", "a-b-c-1-2-3") is False
 # ---- YOUR SLOW TESTS (at least 2) ----
