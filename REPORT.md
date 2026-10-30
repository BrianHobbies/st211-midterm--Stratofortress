# REPORT.md

Group: <Stratofortress>   
| Member  | ID | Username |
| ------------- | ------------- | ------------- |
| Aung San Thu Rain Tun  | 6805142005 | BrianHobbies |
| May Than Thar Ko  | 6805140051 | 6805140051-oss |
| Moe Pyae Kyaw  | 6805142010 | 6805142010-hue |
## Part A -- Test types
*Smoke. Quick, shallow checks that the core features work at all. Run on every push or deployment, first in the pipeline, so a badly broken build is rejected within seconds. Examples: register a new user then log in; add a product, add it to the cart and check out a non-empty cart.

*Regression. A test written for a specific bug that was found and fixed, which fails while the bug exists and passes once fixed. It guards against the bug returning. Run on every change before merging and in the full suite before release. Examples: the cart total includes the last item; login rejects a wrong password.

*Slow. A test that takes a long time because of large data or many operations. Too slow to run on every commit, so run nightly or before a release. Examples: import 50,000 products and search them; add items to the cart and check out in a loop of thousands of orders.

## Part B -- Scenario classification
1. Password-reset email within one minute: slow. It waits on an external email system for up to a minute, so it can never be a quick check. It could also count as smoke if reset is business-critical, but the wait makes slow the main label.
2. Previously fixed shipping-cost bug has not returned: regression. It exists to guard one fixed defect. It is fast and should run on every change. 
3. Nightly job generating a report from ten years of orders: slow. The size of the data is the whole point. It runs on the nightly schedule, not per commit. It is not regression, since no past bug is named.
4. Payment page loads after every deployment: smoke. It is a fast check of a core feature, run on every deployment as a gate. If the page fails to load, nothing else is worth testing.
5. Refund issued twice does not credit twice: regression. This is a customer-reported fault from last quarter, so the test pins a known bug. It is not smoke.
6. Recommendation engine with one million titles: slow. It is a scale test of a large catalogue. It would become slow and regression only if it came from a past failure at that size.


## Part F -- Team reflection

1. Why is running only regression tests before every commit inefficient?

Running only regression tests before every commit is inefficient because there can be many tests, and some take a long time. This slows down our work, especially when we make small changes. We think it is better to run smoke tests first and run the full regression tests when needed.

2. Why do smoke tests usually run first in a CI/CD pipeline?

Smoke tests run first because they are fast and check whether the main features still work. In our bookstore project, important features include login, searching for books, and using the cart. If a smoke test fails, we can find the problem early without waiting for slower tests.

3. What risks arise if slow tests are never run?

If we never run slow tests, we might miss bugs that only appear in more detailed or complicated situations. The smoke tests may pass, but some parts of the bookstore application could still have problems. This could make us think the application is ready when it is not.

4. Can one test belong to two categories? Give an example.

Yes, one test can belong to two categories. For example, a test that checks whether the cart calculates the correct total can be both a regression test and a smoke test. It is a regression test because it checks that a fixed bug does not return. It can also be a smoke test because cart calculation is an important feature of our bookstore application.

5. Bug-finders and bug-fixers are often different people in a real QA team. What does that separation change about how a bug report must be written?

When the person who finds a bug is different from the person who fixes it, the bug report needs to be clear and detailed. It should explain what went wrong, how to reproduce the problem, the actual result, and the expected result. In our team, we used FINDINGS.md to record these details so other members could understand the bugs and work on the fixes without guessing.