# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:50:16 2021

@author: canyi
"""

import pandas as pd
import numpy as np

data = pd.read_excel("3covid19_temiz.xlsx")
#%%

olumsuz_list = ["ölüm", "değil", "pozitif", "karantina", "yükseldi", "vefat", "artış", "kaybetti", "ölü", "kaybı", "kötü",
               "yasak", "kaybedenlerin", "ölen", "kaybeden", "yanlış", "yazık", "maalesef", "artıyor", "artarak" "yalan", "öldü",
               "kriz", "tehlikeli", "krizi", "ateş", "iptal", "zarar", "ölümler", "berbat", "zam", "zarar", "yükseliyor",
               "iflas", "gelmedi", "maskesiz", "gelmiyor", "yasaklandı", "alamıyoruz", "yazık", "kalmadı", "sıkıntı", "vermiyor",
               "bulamıyoruz", "olmuyor", "alamadım", "alamadık", "gelmemiş", "mağdur", "alamıyorum", "bulamıyor", "kavga",
               "öldürür", "öldürecek", "istifa", "kaos", "gerizekalı", "yayılacak", "aptal", "bulaştı", "üzülüyorum",
               "anlamıyorum", "rezillik", "korku", "isyan", "yayıldı", "yakalandı", "üzücü", "eyvah", "mağduruz", "gasp",
               "perişan", "saçmalık", "ağlıyor", "hata"]
#%%
olumlu_list = ["iyi", "güzel", "doğru", "iyileşen", "ücretsiz", "teşekkür", "sağlıklı", "teşekkürler", "mutlu", "umut", 
              "düştü", "negatif", "başarılı", "düşüş", "iyileşme", "doğru", "keyifli", "tebrikler", "indirim", "düştü",
              "düşüşle", "düşürdü", "ucuz", "bedava", "coşkuyla"]
#%%
import nltk
import re
from nltk.tokenize import word_tokenize
data['tokenized_text'] = data['tweet'].apply(word_tokenize) 
#%%
for i in range(len(data)):
    for j in data["tokenized_text"][i]:
        if j in olumsuz_list:
            data["target"][i] = 0
#%%
x = data[data["target"] == 0].reset_index(drop = True)

filter_ = data[data.target == 0]
data = data.drop(filter_.index).reset_index(drop = True)
#%%
for i in range(len(data)):
    for j in data["tokenized_text"][i]:
        if j in olumlu_list:
            data["target"][i] = 1
#%%
y = data[data["target"] == 1].reset_index(drop = True)
#%%
data_son = pd.concat([x,y])
#%%
data_son.drop(["tokenized_text"], axis = 1, inplace = True)
#%%







