# Bug-Hunt Findings Log

Fill in one entry per bug you find, AS YOU FIND IT (before doing the AI
comparison). Write in your own words, like a detective's notebook. Show the real
path -- including things you tried that did not work.

Group: <Stratofortress>   
| Member  | ID | Username |
| ------------- | ------------- | ------------- |
| Aung San Thu Rain Tun  | 6805142005 | BrianHobbies |
| May Than Thar Ko  | 6805140051 | 6805140051-oss |
| Moe Pyae Kyaw  | 6805142010 | 6805142010-hue |

---

## Bug 1

Bug 1

* Module / function: bookstore_app/cart.py -> Cart.total()
* What we suspected and why: We suspected that the cart total was not adding all the product prices correctly.
* What we did: We added two products priced at 10 and 20 to the cart and checked the total.
* What we observed (the wrong result): The function returned 10 instead of 30.
* What we expected instead: The total should be 30 because 10 + 20 = 30.
* The fix we made: We corrected the calculation so that it includes all items in the cart.
* Author of this finding: May Than Thar Ko

---

## Bug 2

Bug 2

* Module / function: bookstore_app/cart.py -> Cart.import_products()
* What we suspected and why: We suspected that the function was returning the wrong number of imported products.
* What we did: We imported two products using [(1, "A", 5), (2, "B", 6)] and checked the returned count.
* What we observed (the wrong result): The function returned 3 even though only 2 products were imported.
* What we expected instead: The function should return 2 because we imported only two products.
* The fix we made: We corrected the counting logic so that the function returns the actual number of imported products.
* Author of this finding: May Than Thar Ko

---

## Bug 3

Bug 3

* Module / function: bookstore_app/catalog.py -> Catalog.search()
* What we suspected and why: We suspected that the search function was returning too many matching products.
* What we did: We added 20 products with the title “match” and searched for “match”.
* What we observed (the wrong result): The function returned 20 matching products.
* What we expected instead: The search function should return no more than 10 matching products.
* The fix we made: We limited the returned search results to the first 10 matches using results[:10].
* Author of this finding: May Than Thar Ko

⸻

## Bug 4

Bug4

* Module / function: bookstore_app/catalog.py -> Catalog.search()
* What we suspected and why: We suspected that the search function was returning too many matching products.
* What we did: We added 20 products with the title “match” and searched for “match”.
* What we observed (the wrong result): The function returned 20 matching products.
* What we expected instead: The search function should return no more than 10 matching products.
* The fix we made: We limited the returned search results to the first 10 matches using results[:10].
* Author of this finding: May Than Thar Ko

## Bug 5

Bug5

* Module / function: bookstore_app/users.py -> Users.login()
* What we suspected and why: We suspected that the login function was not checking the password correctly.
* What we did: We reviewed the original login code and checked how it validated the username and password.
* What we observed (the wrong result): The original code only checked whether the username existed. It did not compare the entered password with the stored password.
* What we expected instead: Login should return True only when both the username and password are correct.
* The fix we made: We changed the login function to compare the stored password with the entered password using return stored == password.
* Author of this finding: May Than Thar Ko

⸻

## Bug 6

Bug 6

* Module / function: bookstore_app/catalog.py -> Catalog.search()
* What we suspected and why: We suspected that the search function was case-sensitive and could not find products when the keyword used different uppercase or lowercase letters.
* What we did: We added a product titled “Python Testing” and tested the search function using “Python”, “python”, and “TESTING”.
* What we observed (the wrong result): The original search function returned an empty list for “python” and “TESTING”, even though the product title contained those words.
* What we expected instead: The search function should find matching products regardless of uppercase or lowercase letters.
* The fix we made: We updated the search logic to compare the keyword and product title without case sensitivity.
* Author of this finding: Aung San Thu Rain Tun

⸻