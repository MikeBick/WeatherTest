This folder contains feature files and automated steps to test the five day weather application

Instructions below are to test the application using Chrome browser, which needs to be installed.

## Prerequisites

### Clone a copy of both repositories to your local PC.

- acceptance-testing-master - the application under test
- this one - the integration_tests folder.

### Install Python and dependent modules

Requires:
- Python 2.7
- ensure python is added to your PATH
- Pip should be pre-installed ( under C:\Python27\Scripts), if not download pip

To install the requisite Python modules:
- change directory into the 'integration_test' subfolder
- type:
```pip install -r requirements.txt```

### Download and install WebDriver

- http://www.seleniumhq.org/projects/webdriver/
- ensure that the ChromeDriver file downloaded is saved to a location in your PATH

### Chrome browser

installed from https://www.google.com/chrome/browser/desktop/index.html

### Run the application under test ('five day weather application')

The application is assumed to be running on your local PC (instructions as per README.md in the top level 'acceptance-testing-master' folder)

### How to run the features

 - change directory into the 'integration_test' subfolder
 - to execute all completed features use the command:

```behave --tags=-wip```

(this excludes features that are not yet complete/automation steps not yet complete)

- various additional options are available at the command line to control which features you wish to execute - see: https://pythonhosted.org/behave/tutorial.html#controlling-things-with-tags

## Future improvements

The functionality included here is limited by time available to complete the exercise - a few hours.

Suggested next steps:
- look into improving the way I retrieve 'data-test' elements - I suspect this can be done better / faster.
* similarly consider getting IDs added to all page objects to aid testability.. we want to avoid identifying objects by XPath etc. where possible
- add functionality to capture screenshots in the event of failure
- consider some tests that verify the data shown on the UI against that returned by the API (or against the stubbed data in the 'src' folder )
  * above would require importing modules to read JSON
- speak with Dev team about adding some page fully loaded indicators (aids testability)
  - implement TODO's marked in code
- there are some product expected behaviours that would need clarified by PO. (see TODO's in feature files)
- improve the logging to add timings and function titles (i.e. where are we)
- structure the utility modules into seperate folder from the .feature files.

### Trade offs

I've not attempted to implement all the feature steps, but instead I've tried to give an idea of my approach and focus on some key requirements.

I've focused on the happy paths and not thought too much about negative tests.  I tried to give an outline of key scenarios even if I did not implement all the steps (yet).

I'd also usually spend a bit more time upfront seeing if there are any obvious bugs before I start automating. e.g looking at some of the summary calculations etc.

Some tidy up and refactoring would be required too - I got to a point where I thought I'd done enough for the exercise and left it at that!

I tend to prefer to close Browser between scenarios for cleanliness, but this does slow the run down, so could be optional/changed.

### Before Commit

- ensure PEP8 compliance
- remove any wip tags that have been implemented


