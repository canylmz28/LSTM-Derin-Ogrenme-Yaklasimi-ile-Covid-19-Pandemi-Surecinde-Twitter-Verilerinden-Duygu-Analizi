# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:23:06 2021

@author: canyi
"""


# Gerekli kütüphanelerin import edilmesi
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding,LSTM
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
#%%Veri seti yüklenmesi
data = pd.read_excel("4target_etiket.xlsx")
#%%Veriler eğitim ve test olmak üzere ayrılır
x = data["tweet"].values.tolist()
y = data["target"].values.tolist()

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)
#%% Veri setinden sık kullanılan 10000 kelimelik bir sözlük oluşturulur. Kelimelere sayısal değer verilir.
tokenizer = Tokenizer(num_words= 10000)
tokenizer.fit_on_texts(x)
kelimeler = tokenizer.word_index
#%% tweetleri,yukarıda oluşturmuş olduğumuz sözlükte karşılığında hangi index’te yer alıyorsa onunla değiştiriyoruz
x_train_tokens = tokenizer.texts_to_sequences(x_train)
x_test_tokens = tokenizer.texts_to_sequences(x_test)
#%% Her bir tweetin içindeki kelime sayıları bulunur . Listeye atılır.
num_tokens = [len(tokens) for tokens in x_train_tokens + x_test_tokens]
num_tokens = np.array(num_tokens)
#%% Maxium kelime sayısını bulma
max_length = max([len(tokens) for tokens in x_train_tokens + x_test_tokens])
#%% burada token(kelime) sayısı ayarlanırken ortalama etrafındaki değişkenlik dikkate alınarak bir sayı belirlenir
#Sonra oluşturmuş olduğumuz listenin ortalamasını alıp daha sonra standart sapmasını 2 ile çarpıp bir değer elde ediyoruz.
#Bu değer bize verimizdeki cümlelerimizin dağılımı ile varsa aykırı uzunluğa sahip cümleleri ortalamaya indirgememize sağlayacak.
max_tokens = np.mean(num_tokens) + 2 * np.std(num_tokens)
max_tokens = int(max_tokens)
#%% veriler belirlenen token sayısına göre ayarlanır
x_train_pad = pad_sequences(x_train_tokens, maxlen=max_tokens)
x_test_pad = pad_sequences(x_test_tokens, maxlen=max_tokens)
#%%tokenlaştırılan kelimeler tekrar string hale geitirilmek için bir fonksiyon yazılması gerekiyor.
idx = tokenizer.word_index
inverse_map = dict(zip(idx.values(), idx.keys()))
#tokenlaştırılan cümleyi tekrar string hale getirmek
def tokens_to_string(tokens):
    words = [inverse_map[token] for token in tokens if token!=0]
    text = ' '.join(words)
    return text
#%%
#ardışık bir model
model = Sequential()

#Embedding katmanı 
#input_dim = Sözlük boyutu+1, output_dim = max uzunluk , input_length = Giriş girdi uzunluğu  
model.add(Embedding(input_dim=10001,
                    output_dim=max_length,
                    input_length=max_tokens,
                    name='embedding_layer'))
#LSTM layerlerinin eklenmesi
# 32 nöronlu LSTM (32 outputlu , return_sequences=True demek output'un tamamını ver demek)
model.add(LSTM(units=32, return_sequences=True))
# 16 nöronlu LSTM (16 outputlu , return_sequences=True demek output'un tamamını ver demek)
model.add(LSTM(units=16, return_sequences=True))
# 8 nöronlu LSTM (8 outputlu , return_sequences=True demek output'un tamamını ver demek)
model.add(LSTM(units=8, return_sequences=True))
# 4 nöronlu LSTM (4 outputlu , return_sequences=False yani default değer, tek bir output verecek)
model.add(LSTM(units=4))
## output layer'ı , görsel olarak gösterilirken dense layer kullanılır.  Tek bir nörondan oluştuğu için 1 yazılır.
model.add(Dense(1, activation='sigmoid'))
#modeli derlemek, loss fonksiyonu binary_crossentropy
#metrics -> modelin başarısını görmek için.
optimizer = Adam(lr=1e-3)
model.compile(loss='binary_crossentropy',
              optimizer= 'adam',
              metrics=['accuracy'])
#%%
model.summary()
#%% batch_size = bir seferde yapay sinir ağını eğitmek için kullanılacak örnek sayısını belirtir.
history = model.fit(x_train_pad, y_train, epochs=5, validation_split = 0.2, batch_size=256)
#%%
loss,accuracy = model.evaluate(x_test_pad, y_test)
print("Accuracy : %f" % (accuracy*100))
#%%
import matplotlib.pyplot as plt
#%%
plt.figure(figsize = (10,7))
plt.subplot(1,2,1)
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Covid-19 Veri Seti Doğruluk Değeri')
plt.ylabel('Doğruluk')
plt.xlabel('Adım Sayısı')
plt.legend(['Eğitim', 'Test'], loc='upper left')

#%%
plt.subplot(1,2,2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Covid-19 Veri Seti Kayıp Değeri')
plt.ylabel('Kayıp')
plt.xlabel('Adım Sayısı')
plt.legend(['Eğitim', 'Test'], loc='upper right')
plt.show()

