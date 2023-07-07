from bookreviews.bookreviews import BookReviews
import bookreviews.constants as const
import os

script_dir = os.path.dirname(__file__)
rel_path_to_driver = const.DRIVER_REL_PATH
abs_file_path_to_driver = os.path.join(script_dir, rel_path_to_driver)

with BookReviews(abs_file_path_to_driver) as br:
    br.get_books()
    print("Exiting...")
