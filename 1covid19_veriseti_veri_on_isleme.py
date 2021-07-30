# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 19:10:20 2021

@author: canyi
"""



import pandas as pd
data=pd.read_csv("2covid19.csv")
#%%
import re
import nltk
import nltk as nlp
nltk.download('punkt')
WPT = nltk.WordPunctTokenizer()
stop_word_list = nltk.corpus.stopwords.words('turkish')
#%%
data.dropna(inplace=True)
#%% yeni temizleme
def kucult(text):
    
    str      = text
    liste   = ''
    krktr = [('İ','i'), ('Ğ','ğ'),('Ü','ü'), ('Ş','ş'),
            ('Ö','ö'),('Ç','ç'), ('I','ı')]
    for liste, harf in krktr:
        str  = str.replace(liste, harf)
        str = str.lower()
        
    return str

list_ = ["a", "mi", "dan", "e", "abd", "nin", "in", "den", "ye", "dr", "ın",
        "un", "nın", "bi" ,"i" ,"ta", "an", "n" ,"u" ,"d", "m" ,"la", "te",
        "r", "s", "t", "ı", "h", "li", "l" ,"k" ,"nun", "v", "na", "ü", "ün",
        "c", "b", "yı", "si", "nda", "nden", "deki", "nde", "yi", "ten", "et",
        "vs", "g", "to", "ndan", "ler", "via", "ım", "vb", "f", "y"]

description_list=[]
for tweet in data.tweet:    
    tweet=re.sub(r'@[A-Za-z0-9]+','', tweet)
    tweet = re.sub(r'(.)\1+', r'\1\1', tweet)
    tweet=re.sub(r'https?:\/\/\S+','', tweet)
    tweet=re.sub(r'http?:\/\/\S+','', tweet)
    tweet=re.sub(r'RT[\s]+','', tweet)
    tweet=re.sub(r'\n','', tweet)
    tweet = re.sub(r"#(\w+)", ' ', tweet)
    tweet=re.sub(r'^\x00-\x7F]+','', tweet)
    tweet=re.sub(r'[^A-Za-zığüşöçİĞÜŞÖÇ]+',' ', tweet)
    tweet=re.sub(r'((https://[^\s]+))','', tweet)  
    tweet=kucult(tweet)
    tweet=nltk.word_tokenize(tweet) #kelimeleri ayır
    tweet=[word for word in tweet if not word in stop_word_list]
    tweet=[word for word in tweet if not word in list_]
    tweet=" ".join(tweet)
    description_list.append(tweet)

#%%
tweets=["tweet"]
for word in description_list:  # iterating on a copy since removing will mess things up
    if word in tweets:
        description_list.remove(word)
#%%
description_list = list(dict.fromkeys(description_list))
#%%
data_son=pd.DataFrame(description_list)
data_son.columns=["tweet"]
#%%
list_ = []
for i in range(len(data_son)):
    x = len(re.findall(r'\w+', data_son["tweet"][i]))
    if x > 3:
        list_.append(data_son["tweet"][i])

#%%
data_son_1 = pd.DataFrame(list_, columns = ["tweet"])







