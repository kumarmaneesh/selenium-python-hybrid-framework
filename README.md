# selenium-python-hybrid-framework

Python-Selenium Hybrid Framework

- Reusable and Maintainable
- Selenium, Python, PyTest, Page Object Model, HTML Reports


Run Tests:
pytest -v -s test_case.py —browser chorme

Run Tests at parallel:
pytest -v -s -n=3 test_case.py —browser firefox

NOTE: -n=3 will look for how many test methods are inside the test case module file

Run Tests with HTML report: (logs also shown in the html report, remove -s for showing up logs)
pytest -v --html Reports/report.html testCases/Test_Login.py --browser chrome


Group Tests for Execution

create pytest.ini file and define markers (under testCases folder)

[pytest]
markers=
	sanity
	regression

add these markers on top of test methds
@pytest.mark.sanity
@pytest.mark.regression

run like this: pytest -v -m "regression" --html Reports/report.html testCases/Test_Login.py --browser chrome
