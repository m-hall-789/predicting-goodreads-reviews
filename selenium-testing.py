from selenium import webdriver
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path_to_driver = "../drivers/geckodriver-v0.33.0-linux64.tar.gz"
abs_file_path_to_driver = os.path.join(script_dir, rel_path_to_driver)
os.environ['PATH'] += abs_file_path_to_driver

print(abs_file_path_to_driver)
