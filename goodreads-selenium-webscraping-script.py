import os
from selenium import webdriver
from selenium.webdriver.common.by import By

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path_to_driver = "../drivers/chromedriver"
abs_file_path_to_driver = os.path.join(script_dir, rel_path_to_driver)
os.environ['PATH'] += abs_file_path_to_driver

driver = webdriver.Chrome()
