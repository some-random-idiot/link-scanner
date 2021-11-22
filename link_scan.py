"""A program that scans all links on a provided webpage."""

import sys
import urllib.request
import urllib.error
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
    # Get all anchor web elements on the page.
    anchor_web_element_list = browser.find_elements(By.TAG_NAME, 'a')
    # Get all anchor web elements' href attributes.
    link_list = [element.get_attribute('href') for element in anchor_web_element_list]
    # Remove all links that are None.
    link_list = [href for href in link_list if href is not None]
    # Remove fragments and query parameters from all links.
    for link in link_list:
        index = link_list.index(link)
        if '#' in link:
            link_list[index] = link[index]
        if '?' in link:
            link_list[index] = link[index]
    # Remove any duplicates.
    link_list = list(dict.fromkeys(link_list))
    return link_list


def is_valid_url(url):
    """Check if the given url is valid.

    Returns:
        True if the url is valid, False otherwise.
    """
    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError as exception:
        # Check whether the error code is caused by permission denial.
        if exception.code == 403:
            return True
        return False
    return True


if __name__ == "__main__":
    # Get the url from the command line.
    url = sys.argv[1]
    print("Setting up the web driver...")

    # Set up the webdriver.
    browser_options = Options()
    browser_options.driver_path = "geckodriver.exe"
    browser_options.headless = True
    browser = webdriver.Firefox(options=browser_options)
    print("Done!")

    # Get the links on the provided page.
    print("Scanning the webpage for links...")
    unchecked_link_list = get_links(url)
    print("All links found!")

    # Validate acquired links.
    print("Validating links...")

    browser.quit()
