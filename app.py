import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from monkeylearn import MonkeyLearn
from newsapi import NewsApiClient
import json

##############################################################################
#Take out filler words and clean header data

text = 'Tesla Batteries Investigated for Possible Defects'
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(text)
filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
	if w not in stop_words:
		filtered_sentence.append(w)

filtered_sentence_join = [' '.join(filtered_sentence)]

##############################################################################
#Use ML Sentimental Analysis Library to Determine if header is pos, neg, neut

# ml = MonkeyLearn('842553b10d9cbfc3fc2e50289881a342ba935155')
# data = filtered_sentence_join
# model_id = 'cl_pi3C7JiL'
# result = ml.classifiers.classify(model_id, data)

# print(result.body[0]['classifications'][0]['tag_name'])

##############################################################################

newsapi = NewsApiClient(api_key='3a634fccd268490d9843bd89ae6c1c8d')

all_articles = newsapi.get_everything(q='tesla',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2019-10-23',
                                      to='2019-11-23',
                                      language='en',
                                      page_size=100,
                                      page=1)

result = all_articles['articles']

# f= open("articles.txt","w+")
# f.write(result)

for article in result:
    text = article['title']
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    filtered_sentence_join = [' '.join(filtered_sentence)]

    ml = MonkeyLearn('842553b10d9cbfc3fc2e50289881a342ba935155')
    data = filtered_sentence_join
    model_id = 'cl_pi3C7JiL'
    result = ml.classifiers.classify(model_id, data)

    print(article["publishedAt"],result.body[0]['classifications'][0]['tag_name'])




# print(result[0]['title'])

##############################################################################