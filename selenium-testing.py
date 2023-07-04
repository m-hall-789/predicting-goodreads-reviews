from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
import os
import time

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
# rel_path_to_driver = "../drivers/geckodriver-v0.33.0-linux64.tar.gz"
rel_path_to_driver = "../drivers/chromedriver"
abs_file_path_to_driver = os.path.join(script_dir, rel_path_to_driver)
os.environ['PATH'] += abs_file_path_to_driver

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
goodreads_url = "https://www.goodreads.com/book/show/2657/reviews"

driver.get(goodreads_url)
driver.maximize_window()
driver.implicitly_wait(8)

# button_to_reviews = driver.find_element(By.CSS_SELECTOR, "[aria-label='Tap to show more reviews and ratings']")
# button_to_reviews.click()
# try:
#     button = driver.find_element(By.XPATH,"//span[text()='Show more reviews']")
#     button.click()
# except:
#     print("Could not find button")

# Getting English filter
button = driver.find_element(By.XPATH,"//button[@class='Button Button--secondary Button--medium']")
button.click()
time.sleep(4)
languages = driver.find_elements(By.XPATH,"//div[@class='RadioGroup']")[-1]
english = languages.find_element(By.XPATH, ".//label[@for='en']")
english.click()
time.sleep(3)
apply_button = driver.find_element(By.XPATH, "//span[@class='Button__labelItem' and text()='Apply']")
apply_button.click()
time.sleep(4)
bottom_divider = driver.find_element(By.XPATH, "//div[@class='Divider Divider--contents Divider--largeMargin']")
load_more_button = bottom_divider.find_element(By.XPATH, "//button[@class='Button Button--secondary Button--small']")
load_more_button.click()
time.sleep(3)
# try:
#     button = driver.find_element(By.XPATH,"//button[@class='Button Button--secondary Button--medium']")
#     button.click()
#     time.sleep(4)
#     languages = driver.find_elements(By.XPATH,"//div[@class='RadioGroup']")[-1]
#     english = languages.find_element(By.XPATH, ".//input[@value='en']")
#     try:
#         english.click()

    # select = Select(driver.find_element(By.NAME, str('language_code')))
    # select = Select(driver.find_element(By.NAME, str('language')))
    # select.select_by_value('en')
    # select = Select(driver.find_element(By.XPATH, "//div[@class='RadioGroup']"))
    # select = Select(driver.find_element(By.XPATH, "//div[@class='ReviewFiltersModal']"))
    # print(select.options)
    # lan_filter = driver.find_element(By.XPATH, "//label[@class='RadioInput'][@for='en']")

    # if lan_filter:
    #     print("found it")
    # elif not lan_filter:
    #     print("filter button not found")
    # lan_filter.()
#     time.sleep(5)
# except:
#     print("Couldn't find filter button")
