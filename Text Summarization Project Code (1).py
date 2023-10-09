#!/usr/bin/env python
# coding: utf-8

# # importing libraries

# In[1]:


import nltk
nltk.download('stopwords')
nltk.download('punkt')
import string
from heapq import nlargest


# In[2]:


with open("sample.txt","r", encoding="utf8") as f:
    text=f.read()


# In[3]:


print(text)


# # Generate Word Cloud Image

# In[4]:


pip install wordcloud


# In[5]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

#print(STOPWORDS)
print("there are {} words in all text.". format(len(text)))

WC=WordCloud(stopwords=STOPWORDS, background_color="beige").generate(text)

plt.figure(figsize=(10,10))
plt.imshow(WC,interpolation='bilinear')
plt.axis("on")
plt.show()


# # keyword extraction

# In[6]:


pip install rake-nltk


# In[7]:


from rake_nltk import Rake
rk=Rake()

rk.extract_keywords_from_text(text)
extract_keyword=rk.get_ranked_phrases()
extract_keyword


# # Text Summarization

# In[8]:


print(text.count("."))
print(string.punctuation)
nopuch=[char for char in text if char not in string.punctuation]
nopuch="".join(nopuch)
#print(nopuch)

process_text=[word for word in nopuch.split() if word.lower() not in nltk.corpus.stopwords.words('english')]
#print(process_text)

#create word freq
word_freq={}
for word in process_text:
    if word not in word_freq:
        word_freq[word]=1
    else:
        word_freq[word]=word_freq[word]+1

#dict(sorted(word_freq.items(),key=lambda item:item[1], reverse=True))

max_freq=max(word_freq.values())

for word in word_freq.keys():
    word_freq[word]=(word_freq[word]/max_freq)

#create sent freq
sent_list=nltk.sent_tokenize(text)

sent_score={}
for sent in sent_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_freq.keys():
            if sent not in sent_score.keys():
                sent_score[sent]=word_freq[word]
            else:
                sent_score[sent]=sent_score[sent]+word_freq[word]
                
#dict(sorted(sent_score.items(),key=lambda item:item[1], reverse=True))
       
summary_sent=nlargest(10,sent_score, key=sent_score.get)

summary=" ".join(summary_sent)

summary


# In[ ]:




