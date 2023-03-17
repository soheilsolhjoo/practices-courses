import os

from os import path
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, "Hamlet_pg1524.txt")).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)
wordcloud.to_file("Hamlet.jpg")
