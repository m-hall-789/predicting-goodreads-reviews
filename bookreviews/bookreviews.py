import types
import typing
import bookreviews.constants as const

from selenium import webdriver
import os
import math

# script_dir = os.path.dirname(__file__)
# rel_path_to_driver = "../drivers/chromedriver"
# abs_file_path_to_driver = os.path.join(script_dir, rel_path_to_driver)
# os.environ['PATH'] += abs_file_path_to_driver

class BookReviews(webdriver.Chrome):
    def __init__(self, driver_path):
        self.driver_path = driver_path
        os.environ['PATH'] += driver_path
        super(BookReviews, self).__init__()

    def __enter__(self):
            return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.quit()

    # One for testing
    def get_book_list(self):
        url = const.BOOKS_LIST + "1"
        self.get(url)

    def get_books(self):
        page=1
        num_pages = math.floor(const.NUM_BOOKS/50)
        book_urls = []
        while page <= num_pages:
            url=const.BOOKS_LIST + str(page)
            # Enter actual scraping here
            page+=1
        if const.NUM_BOOKS%50:
            url=const.BOOKS_LIST + str(page)
            # again, actual scraping
