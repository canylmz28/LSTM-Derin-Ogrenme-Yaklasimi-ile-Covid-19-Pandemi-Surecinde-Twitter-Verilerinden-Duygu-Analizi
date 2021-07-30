# LSTM-Derin-Ogrenme-Yaklasimi-ile-Covid-19-Pandemi-Surecinde-Twitter-Verilerinden-Duygu-Analizi

Dünyada yaşanan toplumsal olaylarda insanların düşüncelerini öğrenmek ve bunları analiz etmek oldukça önemlidir. Bu analizlerle beraber çeşitli çıkarımlar, projeler ve karar verme süreçleri oluşur. Bir metnin çeşitli bilgisayar algoritmaları ile sınıflandırılmasıyla duygu analizi işlemi gerçekleştirilir. Duygu analizini gerçekleştirmek için çeşitli algoritmalar ve yöntemler vardır. Bu yöntemler genel olarak sözlük tabanlı yaklaşım ve makine öğrenmesi yaklaşımı olarak ikiye ayrılır. Bu çalışmada dünyayı etkisi altına alan ve devam eden koronavirüs pansemisi (Covid-19) sürecinde Türkiye’de sık konuşulan bazı terimlerden duygu analizi çalışması gerçekleştirilmiştir. 11 Mart 2020 tarihinden itibaren insanların bu konu hakkında düşüncelerini paylaştığı bir platform olan Twitter sosyal medya aracından Covid-19 virüsü ile ilgili bazı başlıklar toplanmıştır. Toplanan bu başlıklar olumlu ve olumsuz şeklinde sınıflandırılarak duygu analizi yapılmıştır. Bu analiz için derin öğrenme yöntemlerinden Uzun Kısa Süreli Hafıza (LSTM) yapısı kullanan bir sistem önerilmiştir. Önerilen sistem ele alınan Covid-19 veri setinde uygulanmış ve %97 doğruluk başarısı elde edilmiştir.

# Proje Adımları

## 1) Veri Seti
Bu çalışmada Covid-19 sürecinde Twitter üzerinden atılan Türkçe tweetler kullanılmıştır. Bu konuyla ilgili hazır bir veri seti olmadığı için Twitter API aracılığıyla, python dilinde yazılmış bir scrape methoduyla tweetler toplanmıştır. 11 Mart 2020 tarihinden normalleşme adımlarının atıldığı 1 Haziran 2020 tarihine kadar 5 başlık altında yaklaşık 485.000 adet Türkçe tweet toplanmıştır. Şekilde veri seti içindeki bazı tweetler gösterilmiştir.

![image](https://user-images.githubusercontent.com/71662622/127620604-cd4b0fd4-4a4c-4394-8b38-22322ed682d4.png)

## 2) Veri Ön İşleme
Çalışmada kullanılacak veri seti, gerekli sınıflandırma algoritmalarına girmeden önce veri ön işleme aşamalarına sokulur. Bunu yapma sebebimiz daha başarılı bir model oluşturmaktır. Şekilde veri ön işleme adımları gösterilmiştir.

![image](https://user-images.githubusercontent.com/71662622/127620689-d2756155-d475-424a-b361-7993bba4f4b9.png)

Veri temizleme aşamasında ilk olarak veri setinde bulunan http, simge, hashtag, noktalama işaretleri gibi gereksiz ifadeler temizlenmiştir. Ayrıca aynı tweetleri içeren satırlar silinmiştir. Temizlenen veri setinde bulunan kelimeler küçük harfe çevrilmiştir. Bu işlemlerden sonra Türkçede sık kıllanılan durak kelimeler veri setinden kaldırılmıştır. Son olarak da 4 kelimeden az olan tweetler metin analizinde anlamlı bir sonuç üretemeyeceği için veri setinden çıkarılmıştır. Bu işlemleri gerçekleştirmek için python programlama dili ve kütüphaneleri kullanılmıştır. Şekilde temizlenmiş veri seti gösterilmiştir

![image](https://user-images.githubusercontent.com/71662622/127620722-b70286ae-49d7-40d2-bc6f-6917702ed111.png)

## 3) Sınıflandırma

Sınıflandırma, kategorisi bilinmeyen verilere en uygun kategorinin atanmasıdır. Sınıflandırma işlemi için genellikle makine öğrenmesi algoritmaları kullanılır. Bu çalışmada makine öğrenmesinin alt sınıfı olan derin öğrenme algoritmalarından LSTM algoritması kullanılanılmıştır. Şekilde LSTM model adımlarını gösterilmiştir. 

![image](https://user-images.githubusercontent.com/71662622/127620779-ff12bc92-17d6-40b0-b1ef-dd617a761c60.png)


İlk olarak verideki etiketler ve tweetler birer değişkene atılır. Eğitim ve test veri seti oluşturulur. Daha sonra veri setinin içinde en çok kullanılan 10.000 kelimeye göre bir sözlük oluşturulur ve kelimelere sayısal değerler atanır. Veri setindeki her bir kelime oluşturulan sözlükteki sayısal karşılığı ile değiştirilir. Her bir tweetin içindeki kelime sayıları bulunur. Daha sonra her bir tweetin kelime sayılarının genel ortalamasına bakılır ve bir değer elde edilir. Bu değer verimizdeki aykırı uzunluğa sahip cümleleri ortalamaya indirgememizi sağlar. Bu işlemden sonra veri içindeki tüm tweetler aynı uzunluğa dönüştürülür. Verimiz LSTM modelinde kullanılacak hale getirilmiştir. Şekil 9’da görüldüğü gibi model içerisinde bir embedding katmanı, 4 adet LSTM katmanı ve bir çıkış katmanı eklenmiştir. LSTM katmanlarında sırasıyla 32, 16, 8 ve 4 nöron bulunmaktadır. Dense katmanında ise bir nöron bulunmaktadır. Model katmanları oluşturulduktan sonra model eğitilmiştir. 

![image](https://user-images.githubusercontent.com/71662622/127620812-22c6a8d2-c34b-4700-8e38-ac01c290a172.png)


# Bulgular
Tweetler veri ön işleme aşamalarından geçirilmeden önce 484.002, sonrasında 392.060 adete düşmüştür. Şekilde anahtar kelimelerin veri ön işleme öncesi ve sonrasına ait rakamlar verilmiştir. 

![image](https://user-images.githubusercontent.com/71662622/127621041-d19b2595-0f52-4ea4-814d-2c73ba319086.png)

Çalışma için python programlama dilinde pandas, numpy, tensorflow, keras kütüphaneleri kullanılmıştır. Twitter API aracılığıyla çekilen tweetler sırasıyla veri ön işleme ve model oluşturma aşamalarından geçirilmiştir. 

Veri ön işleme aşamasından sonra verilerin duygu sınıfı her bir tweet için rastgele olarak belirlenmiştir. Fakat rastgele duygu sınıfı atanıp model eğitildiği zaman başarı oranının çok düşük olduğu görülmüştür. Bu yüzden her bir veri setinin içinde en çok kullanılan olumlu ve olumsuz kelimeler tespit edilmiştir. Bu kelimelerin geçtiği tweetlere duygu sınıfı atanmıştır. Belirlenen kelimelere göre duygu sınıfı belirlendikten sonra oluşan veri seti ve olumlu olumsuz tweet sayıları Şekilde gösterilmiştir.

![image](https://user-images.githubusercontent.com/71662622/127621090-b06c7cfa-f528-49e6-8c3b-0792d40ff177.png)

Son aşamada ise oluşturulan LSTM modelinin her bir veri seti için doğruluk değeri Şekilde verilmiştir.

![image](https://user-images.githubusercontent.com/71662622/127621111-2f9f527f-49d6-4116-a508-d09c107053a8.png)

Aşağıdaki şekilde Covid19 veri setinin doğruluk ve kayıp değer grafiği gösterilmiştir.

![image](https://user-images.githubusercontent.com/71662622/127622546-a91a5108-6199-4535-bd15-12005570e967.png)


# Sonuç

Bu çalışmada Covid-19 sürecinde Twitter sosyal medya aracından atılan Türkçe tweetlerden duygu analizi çalışması yapılmıştır. Twitter’dan çekilen tweetler gerekli veri temizleme adımlarından geçirilip veri setinde en çok kullanılan kelimelere göre duygu sözlüğü oluşturulmuştur. Bu sözlükle beraber veri setindeki her bir satırın duygu sınıfı belirlenmiştir. Duygu sınıfları belirlendikten sonra veri setimiz hazır hale gelmiştir. Bu işlemlerden sonra LSTM modeli oluşturulmuştur. 5 farklı veri seti için model başarı çıktıları incelenmiş olup doğruluk oranları tablolarda gösterilmiştir.

Sonuçlar incelendiği zaman oluşturduğumuz modelin genel olarak başarı yüzdesinin yüksek olduğunu söyleyebiliriz. Başarı oranları incelendiği zaman covid19 ve sokağa çıkma yasağı veri setlerinin diğer üç veri setine göre daha iyi bir başarı gösterdiği görülür. Bunun en büyük sebebi bu iki veri setinin boyutunun diğer veri setlerinin boyutuna göre daha fazla olmasıdır. 

Modelin daha başarılı ve daha objektif bir sonuç vermesi için özellikle duygu sınıfı belirleme aşamasının titizlikle yapılması gerekmektedir. Bu çalışmada büyük bir duygu sözlüğü kullanılmamıştır. Ayrıca duygu sözlüğündeki kelimelerden birine sahip olmayan tweetler veri setinden çıkarılmıştır. Bu durum ise veri kaybına sebep olmaktadır. Duygu sınıfı etiketleme işlemleri daha titiz yapılırsa, daha fazla veri toplanırsa ve LSTM modelindeki katmanlar ve parametreler daha detaylı ayarlanırsa modelimiz daha yüksek başarı sağlayacaktır.

  



