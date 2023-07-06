import sys
import numpy as np
from PIL import Image
import wikipedia  # To extract information
from wordcloud import WordCloud,STOPWORDS

# We will import STOPWORDS because to remove common wordds like "the, a, then, here, after"

a = str(input(" Enter the name of which you want to make word cloud: "))
title = wikipedia.search(a)[0]  # It will search the title from the wikipedia
page = wikipedia.page(title)  #It will search the page related to given topic in wikipedia
text = page.content  # To extract the content of that topic
print(text)

bg = np.array(Image.open("abcd.jpg"))  
unwanted_words = set(STOPWORDS)
wordclo = WordCloud(background_color="yellow", max_words= 200, mask= bg, stopwords=unwanted_words)
wordclo.generate(text)
wordclo.to_file("sample.png")