"""
Script to get screenshots from websites
"""
# Author Roman Werner - github@roman-werner.de

# pip install selenium
# download firefox driver https://github.com/mozilla/geckodriver/releases
# add to path setx /m path "%path%;C:\WebDriver\bin\"  (https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)
# download firefox

import re
from selenium import webdriver


options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)

# add url's of websites you want so screenshot
websites = [
            "https://www.python.org",
            "https://www.selenium.dev/documentation/en/webdriver/driver_requirements/", 
            "https://www.google.de/"
            ]

for index, website in enumerate(websites):
    driver.get(website)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)

    # May need manual adjustment
    driver.set_window_size(S('Width'),S('Height'))
    match = re.search('https?://([A-Za-z_0-9.-]+).*', website)
    driver.find_element_by_tag_name('body').screenshot( "screenshot_complete" + str(index) +  "_" + str(match.group(1)) + ".png")
    print("Progress: (" + str(index+1) + "/" + str(len(websites)) + ")")

driver.quit()

print("Done")
