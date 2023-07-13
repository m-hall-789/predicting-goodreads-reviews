import types
import typing
import bookreviews.constants as const
from selenium.webdriver.common.by import By

from selenium import webdriver
import os
import math
import time
import csv



# options = Options()
# options.add_argument('--headless=new')
# driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)

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
    # def get_book_list(self):
    #     url = const.BOOKS_LIST + "1"
    #     self.get(url)
    #     elements = self.find_elements(By.XPATH, "//a[@class='bookTitle']")
    #     titles = [ele.get_attribute('href') for ele in elements]
    #     print(len(elements))
    #     print(len(titles))
    #     print(titles[:5])

    def get_books(self, num_books=const.NUM_BOOKS):
        page=1
        num_pages = math.floor(num_books/100)
        book_urls = []
        while page <= num_pages:
            url=const.BOOKS_LIST + str(page)
            self.get(url)
            self.check_for_popup()
            elements = self.find_elements(By.XPATH, "//a[@class='bookTitle']")
            book_urls.extend([ele.get_attribute('href') for ele in elements])
            page+=1
        if num_books%100:
            url=const.BOOKS_LIST + str(page)
            self.get(url)
            self.check_for_popup()
            elements = self.find_elements(By.XPATH, "//a[@class='bookTitle']")
            book_urls.extend([ele.get_attribute('href') for ele in elements[:(num_books%100)]])
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

    # def get_books_and_review_urls(self):
    #     self.get_books()

    def check_for_popup(self):
        time.sleep(2)
        try:
            popup = self.find_element(By.XPATH, "//div[@class='Overlay Overlay--floating']")
            close_button = popup.find_element(By.XPATH, "//i[@class='Icon CloseIcon']")
            close_button.click()
            time.sleep(2)
        except:
            pass

    def select_english_filter(self):
        button = self.find_element(By.XPATH,"//button[@class='Button Button--secondary Button--medium']")
        button.click()
        time.sleep(2)
        languages = self.find_elements(By.XPATH,"//div[@class='RadioGroup']")[-1]
        english = languages.find_element(By.XPATH, ".//label[@for='en']")
        english.click()
        time.sleep(2)
        apply_button = self.find_element(By.XPATH, "//span[@class='Button__labelItem' and text()='Apply']")
        apply_button.click()
        time.sleep(2)
        return

    # This class method requires logging into goodreads, which I don't want to
    # hardcode in and publish on my github. However, if already logged in then
    # it can be used as is.
    # def load_more_reviews(self):
    #     bottom_divider = self.find_element(By.XPATH, "//div[@class='Divider Divider--contents Divider--largeMargin']")
    #     load_more_button = bottom_divider.find_element(By.XPATH, "//span[@class='Button__labelItem']")
    #     load_more_button.click()
    #     time.sleep(3)

    def get_reviews_for_single_book(self, url):
        incomplete = True
        while incomplete:
            try:
                self.get(url)
                self.check_for_popup()
                self.select_english_filter()
                review_scores = self.find_elements(By.XPATH, "//span[@class='RatingStars RatingStars__small']")
                review_texts = self.find_elements(By.XPATH, "//span[@class='Formatted']")
                single_book_reviews = []
                for review_score, review_text in zip(review_scores, review_texts):
                    actual_score = review_score.get_attribute("aria-label")[7]
                    actual_text = review_text.text
                    single_book_reviews.append([actual_score, actual_text])
                incomplete=False
            except:
                time.sleep(5)
        print(f"Have scraped {len(single_book_reviews)} reviews for the book.")
        return single_book_reviews

    def get_all_reviews_and_save(self, review_urls):
        first_line = ['review score', 'review text']
        reviews_count = 0
        with open('goodreads-reviews-sample-dataset2.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(first_line)
            for review_url in review_urls:
                single_book_reviews = self.get_reviews_for_single_book(review_url)
                writer.writerows(single_book_reviews)
                reviews_count += 1
                if reviews_count%1 == 0:
                    print(f"Added reviews for {reviews_count} books so far!")
        return
