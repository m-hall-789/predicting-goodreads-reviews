from bookreviews.bookreviews import BookReviews
import os

script_dir = os.path.dirname(__file__)
rel_path_to_driver = "../drivers/chromedriver"
abs_file_path_to_driver = os.path.join(script_dir, rel_path_to_driver)

with BookReviews(abs_file_path_to_driver) as br:
    br.get_books()
    print("Exiting...")
