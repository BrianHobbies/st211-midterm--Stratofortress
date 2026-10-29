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

# ---- YOUR SMOKE TESTS (at least 5) ----
@pytest.mark.smoke
def test_example_register():
    """Author: <example>. Smoke: a new user can register."""
    assert Users().register("newuser", "password123") is True

@pytest.mark.smoke
def test_smoke_login_accepts_correct_and_rejects_wrong_password():
    """Author: May Than Thar Ko. Smoke: correct login succeeds,
    wrong password and unknown user are rejected."""
    users = Users()
    users.register("bob", "pass1234")
    assert users.login("bob", "pass1234") is True
    assert users.login("bob", "wrongpass") is False
    assert users.login("nobody", "pass1234") is False


@pytest.mark.smoke
def test_smoke_add_product_is_saved_and_searchable():
    """Author: May Than Thar Ko. Smoke: an added product is saved
    with its details and can be found by search."""
    catalog = Catalog()
    catalog.add_product(1, "Python Basics", 20.0)
    assert 1 in catalog.products
    assert catalog.products[1]["title"] == "Python Basics"
    assert catalog.products[1]["price"] == 20.0
    assert catalog.search("Python") == [1]

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

def test_cart_total_includes_every_item():
    """Author: <ASTRH>. Regression for Cart.total.
    Observed: the loop runs over range(len(items) - 1), so the LAST item is
    never added: items priced 10, 20, 30 give 30 instead of 60.
    Expected: total() is the sum of the prices of all items in the cart."""
    catalog = Catalog()
    catalog.add_product(1, "A", 10)
    catalog.add_product(2, "B", 20)
    catalog.add_product(3, "C", 30)
    cart = Cart(catalog)
    for pid in (1, 2, 3):
        cart.add(pid)
    assert cart.total() == 60

@pytest.mark.regression
def test_checkout_empty_cart_returns_none_and_records_no_order():
    """Author: <ASTRH>. Regression for Cart.checkout.
    Observed: checking out an empty cart returns [] and appends an empty
    order to the history.
    Expected: the docstring says it returns None if the cart is empty, and
    no order should be recorded."""
    cart = Cart(Catalog())
    assert cart.checkout() is None
    assert cart.history() == []
 
 
@pytest.mark.regression
def test_search_is_case_insensitive():
    """Author: <ASTRH>. Regression for Catalog.search.
    Observed: search("python") returns [] for a product titled
    "Python Testing", and search("TESTING") also returns []. Only an exact
    case match is found.
    Expected: search returns every product whose title contains the keyword
    regardless of letter case, as a shopper would expect."""
    catalog = Catalog()
    catalog.add_product(1, "Python Testing", 30)
    assert catalog.search("Python") == [1]
    assert catalog.search("python") == [1]
    assert catalog.search("TESTING") == [1]
 
 
@pytest.mark.regression
def test_import_products_returns_exact_count():
    """Author: <ASTRH>. Regression for Cart.import_products.
    Observed: importing 3 products returns 4 (count + 1).
    Expected: it returns how many were imported, i.e. 3."""
    cart = Cart(Catalog())
    imported = cart.import_products([(1, "A", 5), (2, "B", 6), (3, "C", 7)])
    assert imported == 3
    assert len(cart.catalog.products) == 3

# ---- YOUR SLOW TESTS (at least 2) ----
@pytest.mark.slow
def test_slow_bulk_import_fifty_thousand_products():
    """Author: <ASTRH>. Slow: bulk-import 150,000 products and confirm every
    one is stored and searchable.
    # SLOW BECAUSE: import_products loops over every product and yields the scheduler each iteration via time.sleep(0), and the follow-up 
    # checks scan all 150,000 catalog entries"""
    catalog = Catalog()
    cart = Cart(catalog)
    n = 150_000
    products = [(i, f"Book number {i}", 10.0 + (i % 50)) for i in range(n)]
    cart.import_products(products)
    assert len(catalog.products) == n
    assert catalog.products[0]["title"] == "Book number 0"
    assert catalog.products[n - 1]["title"] == f"Book number {n - 1}"
    assert catalog.search("Book number 49999") == [49999]
    assert len(catalog.search("Book")) == n

@pytest.mark.smoke
def test_smoke_add_to_cart_reaches_the_cart():
    """Author: Moe Pyae Kyaw. Smoke: adding products puts them
    in the cart, and unknown products are rejected."""
    catalog = Catalog()
    catalog.add_product(1, "Python Basics", 20.0)
    catalog.add_product(2, "Data Science", 30.0)

    cart = Cart(catalog)

    assert cart.add(1) is True
    assert cart.add(2) is True
    assert cart.items == [1, 2]

    assert cart.add(999) is False
    assert 999 not in cart.items


@pytest.mark.smoke
def test_smoke_checkout_produces_an_order_and_empties_cart():
    """Author: Moe Pyae Kyaw. Smoke: checkout creates an order,
    saves it in history, and empties the cart."""
    catalog = Catalog()
    catalog.add_product(1, "Python Basics", 20.0)
    catalog.add_product(2, "Data Science", 30.0)

    cart = Cart(catalog)
    cart.add(1)
    cart.add(2)

    order = cart.checkout()

    assert order is not None
    assert order == [1, 2]
    assert cart.history() == [[1, 2]]
    assert cart.items == []