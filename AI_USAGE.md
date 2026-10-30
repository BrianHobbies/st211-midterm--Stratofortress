# AI Usage Declaration and Audit

**Group:** Stratofortress  **Members:** Aung San Thu Rain Tun ,Moe Pyae Kyaw ,May Than Thar Ko

**Part D3 of the midterm — 20 marks.** Part 1 is required but carries no marks;
its absence is an academic-honesty matter. Part 2 is worth 16 (2 per test).
Parts 3 and 4 together are worth 4.

Before you submit, check all eight boxes:

- [ ] Part 1 declaration complete, or the "no AI used" statement written
- [ ] All eight tests appear in the summary table with a verdict
- [ ] All eight have **two** pasted evidence runs (shipped code, and your fixed code)
- [ ] Part 3 coverage table filled in against `FINDINGS.md`
- [ ] Part 4 verdict written, under 400 words
- [ ] Every audit entry names the member who did it
- [ ] No claim made that you cannot demonstrate from pasted output
- [ ] File committed as `AI_USAGE.md` in the repository root

---

## Part 1 — AI usage declaration (required, unmarked)

Every AI tool any member used anywhere in this project. Using AI is allowed.
Not declaring it is not.

| Tool | What we used it for | Where in the project | How we checked it before relying on it |
|---|---|---|---|

| ChatGPT | Understanding assignment instructions and GitHub workflow | AI_USAGE.md and repository workflow | Checked explanations against assignment instructions and GitHub files |
| ChatGPT | Suggesting Python bug fixes and regression tests | bookstore_app/, tests/test_bookstore.py, FINDINGS.md | Reviewed suggestions, modified code, and verified results using pytest |
| ChatGPT | Helping create smoke tests for login, catalog, cart, and checkout | tests/test_bookstore.py | Ran the four smoke tests and confirmed they passed |
| ChatGPT | Explaining AI-generated test auditing and reporting requirements | AI_USAGE.md | Audit conclusions will be checked against actual test outputs |

If you kept prompts worth showing, add them in an appendix at the end of this
file. Do not paste whole conversations.

If no AI tools were used anywhere, write this instead of the table:



---

## Part 2 — Audit of the supplied test set (16 marks)

`ai_review/test_ai_suggested.py` contains eight tests presented as a finished
AI bug hunt for this bookstore. They are confident and they are not all
correct. Your job is to establish, for each one, what it actually does.

### How to classify a test

A single test run cannot tell you. "Fails against the buggy code" does **not**
mean the test found a bug — a test demanding behaviour the application was
never meant to have also fails. You need two runs, and the pair of results is
what identifies the category:

| Shipped Code | Fixed Code | What This Tells You | Verdict |
|---|---|---|---|
| ❌ FAIL | ✅ PASS | The test failed when the bug existed and passed after the bug was fixed. It successfully detected a real defect. | **Genuine detection** |
| ✅ PASS | ✅ PASS | The test passed before and after the fix. It never noticed the bug, so it provides false confidence. | **Detects nothing** |
| ✅ PASS | ❌ FAIL | The test expected the buggy behaviour. After the bug was fixed, the test broke. | **Locks in the bug** |
| ❌ FAIL | ❌ FAIL | The test failed both before and after the fix. It is testing something unrelated to the bug, or a requirement that does not exist. | **Invented requirement** |

The third row is the one to think hardest about. A test that locks in a bug is
worse than one that detects nothing: a team that trusts its suite will see the
test go red after a correct fix, conclude the fix was wrong, and revert it. The
bug then has a test defending it.

### How to produce the evidence

Run each test twice — once with the application as you received it, once with
your fixes in place. If you have already fixed the code, you can get back to
the shipped state with git:

```bash
# your fixed code
pytest ai_review/test_ai_suggested.py -v | tee /tmp/fixed.txt

# the code as it was shipped (replace <sha> with your first commit)
git stash
git checkout <sha> -- bookstore_app/
pytest ai_review/test_ai_suggested.py -v | tee /tmp/shipped.txt
git checkout HEAD -- bookstore_app/
git stash pop
```

Paste the real output. Not a screenshot, not a retyped summary — the text.

### Marks, per test

| | marks |
|---|---|
| Correct verdict | 1 |
| Both evidence runs pasted, showing the outcome you claim | 1 |

**A claim you cannot demonstrate costs a mark.** If you assert a test is broken
and the output does not support it, you lose more than you would have gained by
leaving the row blank. Check before you write.

### Summary table — fill this in first

| # | Test | What it claims to catch | Shipped | Fixed | Verdict | Auditor |
|---|---|---|---|---|---|---|
| 1 | test_cart_total_sums_items | Cart total calculation | FAIL | PASS | Genuine detection | Moe Pyae Kyaw |
| 2 | test_login_rejects_wrong_password | Reject incorrect password | PASS | PASS | Detects nothing | Moe Pyae Kyaw |
| 3 | test_search_finds_exact_title | Find matching book title | PASS | PASS | Detects nothing | Moe Pyae Kyaw |
| 4 | test_import_returns_count | Return correct imported item count | FAIL | PASS | Genuine detection | Moe Pyae Kyaw |
| 5 | test_register_duplicate_returns_false | Reject duplicate registration | PASS | PASS | Detects nothing | Moe Pyae Kyaw |
| 6 | test_checkout_empty_returns_none | Return None for empty checkout | FAIL | PASS | Genuine detection | Moe Pyae Kyaw |
| 7 | test_add_to_cart_returns_true_for_known_product | Accept a known product | PASS | PASS | Detects nothing | Moe Pyae Kyaw |
| 8 | test_search_is_limited_to_ten_results | Limit search results to ten | FAIL | PASS | Genuine detection | Moe Pyae Kyaw |

### Detail entries

Copy the block below once for each of the eight tests. Do not paste the test
code — it is in the repository and identical for everyone. Reference it by name
and line instead.

---

 
### Test 1: test_cart_total_sums_items

**Audited by:** Moe Pyae Kyaw

**What it claims to catch:**  
This test claims to check whether the cart total correctly adds the prices of items.

**Evidence — shipped code:**  
>       assert c.total() == 30
E       assert 10 == 30
E        +  where 10 = total()

/workspaces/st211-midterm--Stratofortress/ai_review/test_ai_generated.py:16: AssertionError
Result: FAILED

**Evidence — fixed code:**  
  ai_review/test_ai_generated.py::test_cart_total_sums_items PASSED [ 12%]
Result: PASSED

**What the pair proves:**  
The original code returned 10 instead of the expected total of 30. After fixing the cart total calculation, the test passed. This confirms that the test detected a real bug.

**Verdict:** Genuine detection.

---

### Test: `test_login_rejects_wrong_password`

**Audited by:** Moe Pyae Kyaw
**1. What it claims to catch**

This test checks whether the login function rejects an incorrect password. It is intended to verify that a user cannot log in with the wrong credentials.

**2. Evidence – against the shipped code**

Command: `python -m pytest ai_review/test_ai_generated.py::test_login_rejects_wrong_password -v`

Result: PASSED (1 passed)

**3. Evidence – against the fixed code**

Command: `python -m pytest ai_review/test_ai_generated.py::test_login_rejects_wrong_password -v`

Result: PASSED (1 passed)

**4. What that pair proves**

The test passed against both the original buggy code and the fixed code. It checks incorrect-password rejection but does not detect any of the identified bugs.

**5. Verdict**

- [x] Detects nothing – PASS then PASS
---

### Test: `test_search_finds_exact_title`

**Audited by:** Moe Pyae Kyaw

**1. What it claims to catch**

Evidence — shipped code:

Result: PASSED

Evidence — fixed code:

Result: PASSED

What the pair proves:

The test passed against both the original and fixed versions. It checks whether a product can be found by its exact title, but it does not detect the search result limit bug.

Verdict: Detects nothing.

Test 4: test_import_returns_count

Audited by: Moe Pyae Kyaw

What it claims to catch:

This test checks whether import_products() returns the correct number of imported products.

Evidence — shipped code:

>       assert c.import_products([(1, "A", 5), (2, "B", 6)]) == 2
E       AssertionError: assert 3 == 2
E        +  where 3 = import_products([(1, 'A', 5), (2, 'B', 6)])
/workspaces/st211-midterm--Stratofortress/ai_review/test_ai_generated.py:34: AssertionError

Result: FAILED

Evidence — fixed code:

ai_review/test_ai_generated.py::test_import_returns_count PASSED [ 50%]

Result: PASSED

What the pair proves:

The original code returned 3 after importing only 2 products. After fixing the incorrect count, the test passed. This confirms that the test detected a real bug.

Verdict: Genuine detection.

Test 5: test_register_duplicate_returns_false

Audited by: Moe Pyae Kyaw

What it claims to catch:

This test checks whether the system rejects a duplicate username during registration.

Evidence — shipped code:

Result: PASSED

Evidence — fixed code:

Result: PASSED

What the pair proves:

The test passed with both the original and fixed code. Although it checks duplicate registration, it did not detect any of the planted bugs.

Verdict: Detects nothing.

Test 6: test_checkout_empty_returns_none

Audited by: Moe Pyae Kyaw

What it claims to catch:

This test checks whether checkout returns None when the shopping cart is empty.

Evidence — shipped code:

Result: FAILED

Evidence — fixed code:

Result: PASSED

What the pair proves:

The test failed with the original code because checkout did not return None for an empty cart. After the checkout function was fixed, the test passed. This shows that the test detected a real bug.

Verdict: Genuine detection.

Test 7: test_add_to_cart_returns_true_for_known_product

Audited by: Moe Pyae Kyaw

What it claims to catch:

This test checks whether the cart accepts a product that exists in the catalog and returns True when the product is added.

Evidence — shipped code:

Result: PASSED

Evidence — fixed code:

Result: PASSED

What the pair proves:

The test passed with both the original and fixed code. It checks basic add-to-cart functionality but did not detect any of the planted bugs.

Verdict: Detects nothing.

Test 8: test_search_is_limited_to_ten_results

Audited by: Moe Pyae Kyaw

What it claims to catch:

This test checks whether the catalog search function returns no more than 10 matching products.

Evidence — shipped code:

>       assert len(cat.search("match")) <= 10
E       AssertionError: assert 20 <= 10
E        +  where 20 = len([0, 1, 2, 3, 4, 5, ...])
/workspaces/st211-midterm--Stratofortress/ai_review/test_ai_generated.py:60: AssertionError

Result: FAILED

Evidence — fixed code:

ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results PASSED [100%]
1 passed in 0.02s

Result: PASSED

What the pair proves:

The original code returned 20 matching products even though the search results should be limited to 10. After fixing the catalog search function, the test passed. This confirms that the test detected a real bug.

Verdict: Genuine detection.
## Part 3 — Coverage against your own bug hunt

One row per bug you recorded in `FINDINGS.md`, plus a row for any bug the
supplied set caught that you had not found yourself.


| Bug (your description) | We found it | The supplied set catches it | Which test, and how you established that |
|---|---|---|---|
| Bug 1 – Cart total misses an item | Yes | Yes | `test_cart_total_sums_items`: failed on shipped code, passed after the fix. |
| Bug 2 – Import returns incorrect count | Yes | Yes | `test_import_returns_count`: failed on shipped code, passed after the fix. |
| Bug 3 – Search returns more than 10 results | Yes | Yes | `test_search_is_limited_to_ten_results`: failed on shipped code, passed after the fix. |
| Bug 4 – Search is case-sensitive | Yes | No | No supplied test checks lowercase and uppercase variations. Our regression test `test_search_is_case_insensitive` detected it separately. |
| Bug 5 – Login does not check password correctly | Yes | No | `test_login_rejects_wrong_password` passed on the shipped code, so it did not detect this bug. |
| Bug 6 – Empty-cart checkout returns wrong value | Yes | Yes | `test_checkout_empty_returns_none`: failed on shipped code, passed after the fix. |
  

This is a factual cross-reference, not an opinion. Every "yes" in the third
column must point at a test you classified as a genuine detection in Part 2.

---



## Part 4 – Verdict (4 marks, 400 words maximum)

1. **Which failure mode was most common?**

   There was a tie between genuine bug detection and tests that detected nothing. Out of 8 supplied AI-generated tests, 4 failed on the original buggy code and passed after the fixes. The other 4 passed on both versions. This showed that only half of the supplied tests actually detected bugs.

2. **Why is a test that passes against buggy code more dangerous than one that crashes?**

   A passing test can make us think the program is correct even when a bug still exists. For example, the supplied wrong-password login test passed on the original code, although we found a password-checking problem separately. A crashing test is easier to notice because it clearly shows something needs attention.

3. **Did the supplied set catch anything you had missed?**

   No. We had already investigated the cart total, product import count, empty-cart checkout, and search result limit problems. The supplied tests helped confirm these problems, but they did not identify a new bug that our team had missed.

4. **What will you check before trusting a generated test in future?**

   We will first read the test and check whether its expected result matches the function requirements. We will also run it against both the original buggy code and the corrected version. In this exercise, we found that some tests passed even when bugs existed. We will therefore check the assertions carefully and make sure each test can actually detect the problem it claims to test.
  

---

## Appendix (optional)

Prompts, or notes on AI use, that support Part 1.
