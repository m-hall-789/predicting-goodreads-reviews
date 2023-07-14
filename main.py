from bookreviews.bookreviews import BookReviews
import bookreviews.constants as const
import os

import time

script_dir = os.path.dirname(__file__)
rel_path_to_driver = const.DRIVER_REL_PATH
abs_file_path_to_driver = os.path.join(script_dir, rel_path_to_driver)

# start = time.time()

with BookReviews(abs_file_path_to_driver) as br:
    books = br.get_books()
    print(f"Finished retrieving {len(books)} books! \n")
    book_urls = br.get_review_urls(books)
    reviews_dataset = br.get_all_reviews_and_save(book_urls)
    print(f"Finished creating the reviews dataset! \n")

# end=time.time()
# print(f"The time it took to scrape reviews for 4 books is {end-start} seconds.")
