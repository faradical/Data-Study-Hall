# Selenium Installation Instructions
![selenium logo](https://www.cis-openscraper.com/static/images/stack/selenium-logo.png?v=c1dd8fe99eb9bbeccb2d47383ced00ae)\
Selenium for Python is a powerful web scraping and browser automation tool that allows us to retrieve data and automate web tasks. Installation of Selenium is a two phased operation: installing the Selenium Python module and downloading the necessary browser driver for it to control.

## Selenium Module Installation
Installing the selenium module is as easy as running the following in your terminal:\
```pip install selenium```\
So long as your pip is working correctly and you have an internet connection, this should complete without any major problems.

## Downloading a Driver
The driver is the program that allows selenium to actually hijack your browser. It must be downloaded seperately. There are multiple drivers available for this purpose, but this tutorial will focus on installing Geckodriver for Firefox.

### Install Firefox
![look how they ruined a good logo](https://i.redd.it/r4mgmbrs0no31.jpg)\
If Firefox is not already installed, visit https://www.mozilla.org/en-US/firefox/ and click download in the top right to download the installer. Run it and follow all standard installation instructions.

### Download Geckodriver
Geckodriver can be downloaded [here](https://github.com/mozilla/geckodriver/releases). Download the appropriate release for your machine and extract (unzip) all files in your downloads folder.

### Add Geckodriver To $PATH
There are plenty of ways to complete adding the driver to your path variable. Copy it to the bin/ directory, add a new folder to your path for webdrivers, or try running the appropriate included drivetopath.sh file in Bash.

| **Downloads** |
| ------------- |
| [**drivetopath_Mac.sh**](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/faradical/Data-Study-Hall/blob/master/Web%20Scraping/Selenium%20Installation/drivetopath_Mac.sh)|
| [**drivetopath_Windows.sh**](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/faradical/Data-Study-Hall/blob/master/Web%20Scraping/Selenium%20Installation/drivetopath_Windows.sh) |

For Windows users, simply click the file to run with with git bash. On Mac, it may be necessary to first run the following in your terminal:\
```chmod +x /path/to/drivetopath_Mac.sh```\
This command will add executable permissions to your script. Now you can simply click the file to run it or use 
```./path/to/drivetopath_Mac.sh```\
while you are still in your terminal to run it as well.

### Verify $PATH
To verify the geckodriver was successfully added to your path, simply type ```geckodriver``` in your command line. If you see ouput like this then you are good to go!
![geckodriver output](https://raw.githubusercontent.com/faradical/Data-Study-Hall/master/Web%20Scraping/Selenium%20Installation/images/geckodriver_terminal_output.png)
