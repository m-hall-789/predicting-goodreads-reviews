# Predicting Goodreads review scores from the review text on Goodreads

**Current Project**

This will involve webscraping review texts and scores from popular books on Goodreads
(using Selenium), cleaning and preparing the data for sentiment analysis, and then training
a model to predict the review score from the review text.

Current level of progress: <br/>
Webscraping: :heavy_check_mark: <br/>
Data preprocessing: :heavy_check_mark: <br/>
Model construction and training: :heavy_check_mark: <br/>

The model is significantly more accurate than the baseline. Working can be seen on
the jupyter notebook 'dataset-exploration.ipynb'. Could be much more optimised,
will continue to tweak.

**Using the webscraping package**

The webscraping elements can be used, but will require a bit of setup.
Ensure that selenium is installed. Next, you will need to install the correct
driver for your version of Chrome.

[Website link to download driver](https://chromedriver.chromium.org/downloads)

When this driver is downloaded and saved, you will need to update the DRIVER_REL_PATH in the "constants.py" so that it matches
the relative path to the driver from this directory.

Once this is done, you should be able to run the "main.py" file from the console, and the webscraping should begin.

### Future work ons

1. Change the webscraper so it catches error 404 exceptions and deals with them properly rather than constantly reloading
2. Change the webscraper so that it gets the text hidden behind spoiler tags
3. Consider using pretrained embedding (such as 'glove-wiki-gigaword-50' from gensim) for the modelling
4. Try lemmatizing and removing stop words as part of the data preprocessing
5. Optimise the model architecture (layer structure, loss functions, activation function) and the tokenizer (maxlen, padding, truncating)
