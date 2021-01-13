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
            "https://de-de.facebook.com/",
            "https://www.python.org",
            "https://www.selenium.dev/documentation/en/webdriver/driver_requirements/",
            ]

for index, website in enumerate(websites):
    driver.get(website)
    sleep(1)

    # Add more words to trigger the functions which clicks on the cookie banner
    namen = [
        "Alle akzeptieren",
        "Auswahl akzeptieren",
        "Akzeptieren",
        "akzeptieren",
        "Auswahl",
        "auswahl",
        "Alle",
        "alle",
        "stimme",
        "Stimme",
        "Agree",
        "agree"
        "accept",
        "Accept"
        "understand",
        "Understand",
        "einverstanden",
        "Einverstanden",
        "Verweigern",
        "verweigern"
        ]

    # default banner button
    try:
        driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]').click()
        print("default")
    except:
        pass

    for name in enumerate(namen):
        try:
            elements = driver.find_elements_by_xpath("//*[contains(text(),'" + name[1] + "')]")
            for element in enumerate(elements):
                try:
                    element[1].click()
                    print("cookie")
                    sleep(1)
                    break
                except:
                    pass
            break
        except:
            pass

    match = re.search('https?://([A-Za-z_0-9.-]+).*', website)
    driver.get_screenshot_as_file("screenshot" + str(index) +  "_" + str(match.group(1)) + ".png")
    print("Progress: (" + str(index+1) + "/" + str(len(websites)) + ")")

driver.quit()

print("Done")
