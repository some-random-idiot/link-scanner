import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def get_links(url):
    """Find all links on page at the given url.

    Returns:
        A list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    browser.get(url)
    # Get all anchor web elements in the page.
    anchor_web_element_list = browser.find_elements(By.TAG_NAME, 'a')
    # Get all anchor web elements' href attributes.
    link_list = [element.get_attribute('href') for element in anchor_web_element_list]
    # Remove all links that are None.
    link_list = [href for href in link_list if href is not None]
    # Remove fragments and query parameters from all links.
    for link in link_list:
        if '#' in link:
            link_list[link_list.index(link)] = link[:link.index('#')]
        if '?' in link:
            link_list[link_list.index(link)] = link[:link.index('?')]
    return link_list


# Get the url from the command line.
url = sys.argv[1]
print("Setting up the web driver...")

# Set up the webdriver.
browser_options = Options()
browser_options.driver_path = "geckodriver.exe"
browser_options.headless = True
browser = webdriver.Firefox(options=browser_options)
print("Done!")

# Get the links in the provided page.
print("Scanning URLs...")
links = get_links(url)
print("Done!")

browser.quit()
