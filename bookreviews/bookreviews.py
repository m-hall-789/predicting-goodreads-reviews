import types
import typing
import bookreviews.constants as const
from selenium.webdriver.common.by import By

from selenium import webdriver
import os
import math

# script_dir = os.path.dirname(__file__)
# rel_path_to_driver = "../drivers/chromedriver"
# abs_file_path_to_driver = os.path.join(script_dir, rel_path_to_driver)
# os.environ['PATH'] += abs_file_path_to_driver

class BookReviews(webdriver.Chrome):
    def __init__(self, driver_path, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += driver_path
        super(BookReviews, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __enter__(self):
            return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.teardown:
            self.quit()

    # One for testing
    def get_book_list(self):
        url = const.BOOKS_LIST + "1"
        self.get(url)
        elements = self.find_elements(By.XPATH, "//a[@class='bookTitle']")
        titles = [ele.get_attribute('href') for ele in elements]
        print(len(elements))
        print(len(titles))
        print(titles[:5])

    def get_books(self):
        page=1
        num_pages = math.floor(const.NUM_BOOKS/50)
        book_urls = []
        while page <= num_pages:
            url=const.BOOKS_LIST + str(page)
            self.get(url)
            elements = self.find_elements(By.XPATH, "//a[@class='bookTitle']")
            book_urls.extend([ele.get_attribute('href') for ele in elements])
            page+=1
        if const.NUM_BOOKS%50:
            url=const.BOOKS_LIST + str(page)
            self.get(url)
            elements = self.find_elements(By.XPATH, "//a[@class='bookTitle']")
            book_urls.extend([ele.get_attribute('href') for ele in elements[:(const.NUM_BOOKS%50)]])
        return book_urls

    def get_review_urls(self, book_urls):
        review_urls = []
        for book_url in book_urls:
            distinct_url = book_url[36:]
            first_stop = distinct_url.find(".")
            first_dash = distinct_url.find("-")
            if first_stop == -1:
                important_index = first_dash
            elif first_dash == -1:
                important_index = first_stop
            elif first_stop < first_dash:
                important_index = first_stop
            elif first_dash < first_stop:
                important_index = first_dash
            review_url = const.BEGIN_URL + distinct_url[:important_index] + "/reviews"
            review_urls.append(review_url)
        return review_urls

    def select_english_filter(self):
        return


    def get_reviews_for_books(self, review_urls):
        for review_url in review_urls:
            self.get(review_url)
        return
