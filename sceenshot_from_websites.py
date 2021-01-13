"""
Script to get screenshots from websites
"""
# Author Roman Werner - github@roman-werner.de

# pip install selenium
# download firefox driver https://github.com/mozilla/geckodriver/releases
# add to path setx /m path "%path%;C:\WebDriver\bin\"  (https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)
# download firefox

import re
from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()

# add url's of websites you want so screenshot
websites = [
            "https://www.python.org",
            "https://www.selenium.dev/documentation/en/webdriver/driver_requirements/",
            "https://www.google.de/"
            ]

for index, website in enumerate(websites):
    driver.get(website)
    sleep(1)
    match = re.search('https?://([A-Za-z_0-9.-]+).*', website)
    driver.get_screenshot_as_file("screenshot" + str(index) +  "_" + str(match.group(1)) + ".png")
    print("Progress: (" + str(index+1) + "/" + str(len(websites)) + ")")

driver.quit()

print("Done")
