# LSTM-Derin-Ogrenme-Yaklasimi-ile-Covid-19-Pandemi-Surecinde-Twitter-Verilerinden-Duygu-Analizi

Dünyada yaşanan toplumsal olaylarda insanların düşüncelerini öğrenmek ve bunları analiz etmek oldukça önemlidir. Bu analizlerle beraber çeşitli çıkarımlar, projeler ve karar verme süreçleri oluşur. Bir metnin çeşitli bilgisayar algoritmaları ile sınıflandırılmasıyla duygu analizi işlemi gerçekleştirilir. Duygu analizini gerçekleştirmek için çeşitli algoritmalar ve yöntemler vardır. Bu yöntemler genel olarak sözlük tabanlı yaklaşım ve makine öğrenmesi yaklaşımı olarak ikiye ayrılır. Bu çalışmada dünyayı etkisi altına alan ve devam eden koronavirüs pansemisi (Covid-19) sürecinde Türkiye’de sık konuşulan bazı terimlerden duygu analizi çalışması gerçekleştirilmiştir. 11 Mart 2020 tarihinden itibaren insanların bu konu hakkında düşüncelerini paylaştığı bir platform olan Twitter sosyal medya aracından Covid-19 virüsü ile ilgili bazı başlıklar toplanmıştır. Toplanan bu başlıklar olumlu ve olumsuz şeklinde sınıflandırılarak duygu analizi yapılmıştır. Bu analiz için derin öğrenme yöntemlerinden Uzun Kısa Süreli Hafıza (LSTM) yapısı kullanan bir sistem önerilmiştir. Önerilen sistem ele alınan Covid-19 veri setinde uygulanmış ve %97 doğruluk başarısı elde edilmiştir.

# Proje Adımları

## 1) Veri Seti
Bu çalışmada Covid-19 sürecinde Twitter üzerinden atılan Türkçe tweetler kullanılmıştır. Bu konuyla ilgili hazır bir veri seti olmadığı için Twitter API aracılığıyla, python dilinde yazılmış bir scrape methoduyla tweetler toplanmıştır. 11 Mart 2020 tarihinden normalleşme adımlarının atıldığı 1 Haziran 2020 tarihine kadar 5 başlık altında yaklaşık 485.000 adet Türkçe tweet toplanmıştır. Şekil 5’te veri seti içindeki bazı tweetler gösterilmiştir.

![image](https://user-images.githubusercontent.com/71662622/127620604-cd4b0fd4-4a4c-4394-8b38-22322ed682d4.png)
