Please click on the edit icon to see the properly formatted report. 

The Black76 formula is taken from the following resource, which is used also to validate the input data. 
https://www.lme.com/en/trading/contract-types/options/black-scholes-76-formula
This has been chosen as a sufficient testing example as it is step by step and breaks down the intermediate values clearly. Due to time constrain

The project contains the following files:

app.py - the flask application with routes
black76.py - where the calculations are carried out
data.csv - this is data uploaded by the user of the route in app.py. It is in this folder for simplicity, but would 
			otherwise have its own folder for data uploads
data.xlsx - I have kept this as a backup of the csv in case you overwrite data.csv. The unit tests at present rely on data.csv values
test_black76.py - tests the calculations
test_app.py - tests the flask application

TEST COVERAGE REPORT

Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
app.py               24     14    42%   8-9, 16-21, 38-42, 45
black76.py           62      5    92%   41, 46, 48, 89, 126
test_app.py          24      6    75%   19-20, 33-34, 38-39
test_black76.py      48      3    94%   40-41, 112
-----------------------------------------------
TOTAL               158     28    82%

