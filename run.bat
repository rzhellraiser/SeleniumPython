rem edge
pytest -v -s -m "regression" --html=./Reports/report-edge.html testCases/
rem pytest -v -s -m "sanity" --html=./Reports/report-edge.html testCases/
rem pytest -v -s -m "sanity or regression" --html=./Reports/report-edge.html testCases/
rem pytest -v -s -m "sanity and regression" --html=./Reports/report-edge.html testCases/

rem chrome
rem pytest -v -s -m "sanity" --html=./Reports/report-chrome.html testCases/ --browser=chrome
rem pytest -v -s -m "regression" --html=./Reports/report-chrome.html testCases/ --browser=chrome
rem pytest -v -s -m "sanity or regression" --html=./Reports/report-chrome.html testCases/ --browser=chrome
rem pytest -v -s -m "sanity and regression" --html=./Reports/report-chrome.html testCases/ --browser=chrome

rem firefox
rem pytest -v -s -m "sanity" --html=./Reports/report-firefox.html testCases/ --browser=firefox
rem pytest -v -s -m "regression" --html=./Reports/report-firefox.html testCases/ --browser=firefox
rem pytest -v -s -m "sanity or regression" --html=./Reports/report-firefox.html testCases/ --browser=firefox
rem pytest -v -s -m "sanity and regression" --html=./Reports/report-firefox.html testCases/ --browser=firefox