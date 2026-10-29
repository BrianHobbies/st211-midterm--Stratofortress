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
| 1 | test_cart_total_sums_items | Cart total calculation | PASS | PASS | Detects nothing | Moe Pyae Kyaw |
| 2 | test_login_rejects_wrong_password | Reject incorrect password | PASS | PASS | Detects nothing | Moe Pyae Kyaw |
| 3 | test_search_finds_exact_title | Find matching book title | PASS | PASS | Detects nothing | Moe Pyae Kyaw |
| 4 | test_import_returns_count | Return correct imported item count | FAIL | PASS | Genuine detection | Moe Pyae Kyaw |
| 5 | test_register_duplicate_returns_false | Reject duplicate registration | PASS | PASS | Detects nothing | Moe Pyae Kyaw |
| 6 | test_checkout_empty_returns_none | Return None for empty checkout | FAIL | PASS | Genuine detection | Moe Pyae Kyaw |
| 7 | test_add_to_cart_returns_true_for_known_product | Accept a known product | PASS | PASS | Detects nothing | Moe Pyae Kyaw |
| 8 | test_search_is_limited_to_ten_results | Limit search results to ten | FAIL | FAIL | Needs investigation | Moe Pyae Kyaw |

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
Command: `pytest ai_review/test_ai_generated.py::test_cart_total_sums_items -v`  
Result: PASSED

**Evidence — fixed code:**  
Command: `pytest ai_review/test_ai_generated.py::test_cart_total_sums_items -v`  
Result: PASSED

**What the pair proves:**  
The test passed with both the original buggy code and the fixed code. It did not detect the planted cart total bug.

**Verdict:** Detects nothing.

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

This test checks whether the catalog search function can find a book by its exact title. It verifies basic search functionality but does not specifically test the maximum number of search results.
## Part 3 — Coverage against your own bug hunt

One row per bug you recorded in `FINDINGS.md`, plus a row for any bug the
supplied set caught that you had not found yourself.

| Bug (your description) | We found it | The supplied set catches it | Which test, and how you established that |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

This is a factual cross-reference, not an opinion. Every "yes" in the third
column must point at a test you classified as a genuine detection in Part 2.

---

## Part 4 — Verdict (4 marks, 400 words maximum)

Four questions. Be specific and cite your own table.

1. **Which failure mode was most common** in the supplied set? Give the count
   from your summary table.
2. **Why is a test that passes against buggy code more dangerous than one that
   crashes?** A crashing test gets attention. Say what happens to the other
   kind.
3. **Did the supplied set catch anything you had missed?** If yes, what, and
   what would have led you to it. If no, say so — that is a legitimate answer
   and does not cost marks.
4. **What will you check before trusting a generated test in future?** Name
   checks you actually performed in this exercise, not general principles.

Answers that could have been written about any project score half marks at
best.

---

## Appendix (optional)

Prompts, or notes on AI use, that support Part 1.
