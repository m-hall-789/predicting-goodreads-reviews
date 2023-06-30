from selenium import webdriver
from selenium.webdriver.common.by import By
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
# rel_path_to_driver = "../drivers/geckodriver-v0.33.0-linux64.tar.gz"
rel_path_to_driver = "../drivers/chromedriver"
abs_file_path_to_driver = os.path.join(script_dir, rel_path_to_driver)
os.environ['PATH'] += abs_file_path_to_driver

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
goodreads_url = "https://www.goodreads.com/book/show/2657/reviews"

driver.get(goodreads_url)
driver.implicitly_wait(20)

# button_to_reviews = driver.find_element(By.CSS_SELECTOR, "[aria-label='Tap to show more reviews and ratings']")
# button_to_reviews.click()

button = driver.find_element(By.XPATH,"//span[text()='Show more reviews']")
button.click()
