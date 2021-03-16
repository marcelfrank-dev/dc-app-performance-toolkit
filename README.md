# App specific selenium tests

### LastLog:
- Navigate to View log page
- Click apply filter button and wait till the log is loaded
- Click the reload button and wait till the log is loaded twice

### SumUp:
- Navigate to the Calculation rules page
- Add a new Rule with the Watchers field
  <br/><br/>
- Navigate to issue search with JQL: watcher is not EMPTY and project = "VLLR" (174 issues)
- Change to List view
- Click calculate button -> get an error because no field with a rule is visible
- Add watchers as column
- Click calculate button -> the watcher field should be summarized and two sum columns should be displayed
- Click calculate button -> the sum columns should disappear
- Remove watcher as column
  <br/><br/>
- Navigate to the Calculation rules page
- Delete the newly added rule
- Navigate to the Global settings page
- Deactivate Jira Core and Jira Software
- Activate Jira Core and Jira Software


### Jira Workflow Toolbox:
- Navigate to issue with key AFOCIA-1
- The value of the field Calculated Number Field (by JWT) should be 1
- Change the priority -> Summary and Assignee should be changed to unassigned by automation rule
- Condition: The transition JWT-TRANSITION should not be visible
- Click Assign to me button
- Condition: The transition JWT-TRANSITION should be visible
- Execute JWT-TRANSTION without changes on the screen: Validator should fail
- Change the summary on the screen and execute again: Validator should pass
- The summary should be changed to "JWT-Summary"

#### Needed data:
- Issue with key: AFOCIA-1
- Transition on first position (action_id_51): JWT-TRANSITION
- An Update or copy field post function that updates the summary to "JWT-Summary"
- An Only users in a field condition that checks if the current user is the assignee
- A Fields required or changed validator that checks if the summary changed
- Calculated number field that shows the number of linked issues (the issue should have one linked issue)
- Automation rule that clears the assignee and set summary on Priority change


### Admin Toolbox:
- Navigate to Issues -> Issue types page
- Activate/Deactivate Show / Hide ID column settings
- Activate/Deactivate Smart View settings
- Filter issue types by Name
- Clear filter


### xCharts:
- navigate to the xCharts resources page
- click create resource button
- set resource name (JavaScript resource name)
- set resource description (JavaScript resource description)
- change to data tab
- set resource data (console.log("this is xcharts"))
- save resource
- check saved resource
- delete resource
  <br/><br/>
- navigate to the xCharts resources page
- click create resource button
- set resource type to CSS
- set resource name (CSS resource name)
- set resource description (CSS resource description)
- change to data tab
- set resource data (.test {color: #fff;})
- save resource
- check saved resource
- delete resource
  <br/><br/>
- navigate to Chart Data Scripts page
- create a new script
- set script name
- set script description
- set Timeseries chart as template
- set JQL parameter to <b>project = "VLLR"</b>
- run preview
- save chart data script
- check saved chart data script
- delete chart data script


### SpaceAdmin:
- Browse to the space admin browser page
- Browse to the Permission Browser page
- Browse to the Space Admin Settings page
- Browse to the Attachment Service page
- Browse to the Space Shuttle Configuration page
  <br/><br/>
- Navigate to the Permission Manager page
- Select the user whose permission is to be viewed
- Click on submit button
- Verify that the permissions are displayed correctly
  <br/><br/>
- Navigate to the Space Shuttle browser
- Create a category
- Verify that it is created
- Remove the category
- Verify that it is removed

# Data Center App Performance Toolkit 
The Data Center App Performance Toolkit extends [Taurus](https://gettaurus.org/) which is an open source performance framework that executes JMeter and Selenium.

This repository contains Taurus scripts for performance testing of Atlassian Data Center products: Jira, Jira Service Management, Confluence, and Bitbucket.

## Supported versions
* Supported Jira versions: 
    * Jira [Long Term Support release](https://confluence.atlassian.com/enterprise/atlassian-enterprise-releases-948227420.html): `8.13.3`, `8.5.11`

* Supported Jira Service Management versions: 
    * Jira Service Management [Long Term Support release](https://confluence.atlassian.com/enterprise/atlassian-enterprise-releases-948227420.html): `4.13.2`, `4.5.10`
    
* Supported Confluence versions:
    * Confluence [Long Term Support release](https://confluence.atlassian.com/enterprise/atlassian-enterprise-releases-948227420.html): `7.4.6`  
    * Confluence Platform release: `7.0.5`

* Supported Bitbucket Server versions:
    * Bitbucket Server [Long Term Support release](https://confluence.atlassian.com/enterprise/atlassian-enterprise-releases-948227420.html): `7.6.2`, `6.10.7`  
    * Bitbucket Server Platform release: `7.0.5`

## Support
In case of technical questions, issues or problems with DC Apps Performance Toolkit, contact us for support in the [community Slack](http://bit.ly/dcapt_slack) **#data-center-app-performance-toolkit** channel.

## Installation and set up

#### Dependencies
* Python 3.6-3.8 and pip
* JDK 8
* Google Chrome web browser
* Git client (only for Bitbucket Server)

Please make sure you have a version of Chrome browser that is compatible with [ChromeDriver](http://chromedriver.chromium.org/downloads) version set in app/$product.yml file (modules->selenium->chromedriver->version).

If a first part of ChromeDriver version does not match with a first part of your Chrome browser version, update Chrome browser or set compatible [ChromeDriver](http://chromedriver.chromium.org/downloads) version in .yml file.

### macOS/Linux
Make sure that you have [Python](https://www.python.org/downloads/) (see [dependencies](#dependencies) section for supported versions), pip, and [JDK 8](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) installed:
```
python3 --version
pip --version
java -version
```
For Bitbucket Server check that [Git](https://git-scm.com/downloads) is installed:
```
git --version
```

We recommend using virtualenv for Taurus.

1. Install virtualenv with pip:
```
pip install virtualenv
```
2. Create new virtual env with python3:
```
virtualenv venv -p python3
```
3. Activate virtual env:
```
source venv/bin/activate
```
4. Install dependencies:
```
pip install -r requirements.txt
```

### Windows
#### Installing Taurus manually
Make sure you have [Python](https://www.python.org/downloads/) (see [dependencies](#dependencies) section for supported versions), pip, and [JDK 8](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) installed:
```
python --version or python3 --version
pip --version
java -version
Microsoft Visual C++ 14
Windows 10 SDK
```
For Bitbucket Server check that [Git](https://git-scm.com/downloads) is installed:
```
git --version
```

Make sure you have Visual Studio build tool v14.22 installed. 
Otherwise, download it from [Microsoft Visual C++ Build Tools:](https://visualstudio.microsoft.com/downloads) and do the following:
1. Select **Tools for Visual Studio 2019**.
2. Download and run **Build Tools for Visual Studio 2019**.
3. Select the **C++ build tools** check box.
4. Select the **MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.22)** check box (clear all the others).
5. Click **Install**.

Setup [Windows 10 SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/)

We recommend using virtualenv for Taurus.
1. Install virtualenv with pip:
```
pip install virtualenv
```
2. Create new virtual env with python3:
```
virtualenv venv -p python
```
3. Activate virtual env:
```
venv\Scripts\activate
```
4. Install dependencies:
```
pip install -r requirements.txt
```

## Upgrading the toolkit
Get latest codebase from master branch:
```
git pull
```
Activate virtual env for the toolkit and install latest versions of libraries:
```
pip install -r requirements.txt
```

## Additional info
Official Taurus installation instructions are located [here](https://gettaurus.org/docs/Installation/).

## Analytics
The Data Center App Performance Toolkit includes some simple usage analytics.  
We collect this data to better understand how the community is using the Performance Toolkit, and to help us plan our roadmap.
When a performance tests is completed we send one HTTP POST request with analytics.

The request include the following data, and will in no way contain PII (Personally Identifiable Information).
- application under test (Jira/Confluence/Bitbucket)
- timestamp of performance toolkit run
- performance toolkit version
- operating system
- `concurrency` and `test_duration` from `$product.yml` file
- actual run duration
- executed action names and success rates
- unique user identifier (non PII)

To help us continue improving the Toolkit, we’d love you to keep these analytics enabled in testing, staging, and production. If you don’t want to send us analytics, you can turn off the `allow_analytics` toggle in `$product.yml` file.

## Running Taurus
Navigate to [docs](docs) folder and follow instructions.
