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

# ---- YOUR SLOW TESTS (at least 2) ----
