# SeleniumPython
Sample selenium-python test framework

1. Tech stack: Selenium, Python, Pytest, , Allure, Jenkins CI.
2. To run tests:

> Run default browser -> pytest -v -s <path-to-test-file.py>
>
> Run with specific browser -> pytest -v -s <path-to-test-file.py> --browser <browser-name>
>
> Run in parallel mode -> pytest -v -s -n=<parallel-runs-number> <path-to-test-file.py> --browser <browser-name>
>
> Run generating report -> pytest -v -s --html=<path-to-generate-report> <path-to-test-file.py> --browser <browser-name>
>
> Run with markers -> pytest -v -s -m "regression" --html=./Reports/report.html testCases/ --browser <browser-name>
