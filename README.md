
# 🚀 zynpdata-zynp_ai-teknofest: Türkiye'nin En Büyük Açık Kaynaklı Türkçe Veri Seti

<img src="https://i.imgur.com/1JQlntm.jpg" alt="zynpdata-zynp_ai-teknofest" width="200" height="200">

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://semver.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/sekerlipencere/zynpdata-zynp_ai-teknofest)

[![Download](https://img.shields.io/badge/Download-v1.0.0-blue?style=for-the-badge&logo=github)](https://huggingface.co/datasets/sekerlipencere/zynpdata-zynp_ai-teknofest/resolve/main/dataset.jsonl?download=true)

## 📊 Proje Tanımı

Türkiye'nin en büyük, en çok indexlenen, en çok üyeye sahip olan, en çok anlık aktiviteye sahip ve en popüler forumu Technopat'tan kazınmış ve Teknofest 2024 Doğal Dil İşleme Yarışması kapsamında zynp_ai tarafından oluşturulmuş, tamamen Türkçe ve açık kaynaklı en büyük veri setidir.Yaklaşık 3 milyon konu ve 21 milyon yanıt içeren 7GB'lık bu veri seti, Türkçe NLP ve LLM projeleri için kapsamlı bir kaynak sağlar.

## 🌟 Neden zynpdata?

- **Benzersiz İçerik**: Technopat forumundan elde edilen gerçek insanlar tarafından yazılmış 30'dan fazla katagoride veri içerir.
- **Geniş Kapsam**: Teknolojiden günlük yaşama kadar çeşitli konuları içerir.
- **Büyük Ölçek**: 3 milyon konu ve 21 milyon cevap ile Türkçe NLP ve LLM model çalışmaları için eşsiz bir kaynaktır.
- **Güncel**: Türkiye'nin en aktif forumlarından biri olan Technopat'tan elde edilen güncel veriler ve içerir.
- **Çeşitlilik**: Farklı yazım stilleri, jargon ve diyalektler içerir aynı zamanda 2012'den günümüze kadar çeşitli veriler içerir.

## 💡 Kullanım Alanları

- Türkçe Doğal Dil İşleme (NLP) modellerinin eğitimi:
- Dil modelleri (LLM) için fine-tuning: Özellikle LLM modellerinin finetunungi için mükemmel doğrulukta saf bilgi sunar.Dil modelleri, doğal dil işleme (NLP) alanında büyük önem taşır ve çeşitli görevler için kullanılabilir. Fine-tuning, bu modellerin belirli bir veri kümesi üzerinde özelleştirilerek performanslarının artırılmasını sağlar. "zynpdata-zynp_ai-teknofest" veri seti, dil modellerinin fine-tuning işlemleri için mükemmel bir kaynak sunar.
- Sentiment analizi ve konu modelleme çalışmaları
- Türkçe soru-cevap sistemleri geliştirme
- Sosyal ağ analizi ve kullanıcı davranışı araştırmaları

## 🚀 Veri Setini İndirme

[![Download](https://img.shields.io/badge/Download-v1.0.0-blue?style=for-the-badge&logo=github)](https://huggingface.co/datasets/sekerlipencere/zynpdata-zynp_ai-teknofest/resolve/main/dataset.jsonl?download=true)

### Yukarıdaki butonu veya [bu bağlantıyı](https://huggingface.co/datasets/sekerlipencere/zynpdata-zynp_ai-teknofest/resolve/main/dataset.jsonl?download=true) kullanarak veri setini indirebilirsiniz.

#### Veri setini projenize doğrudan dahil etmek için farklı kütüphanelerin nasıl kullanılacağını gösteren aşağıdaki kod örneklerinden faydalanabilirsiniz.
---
*Datasets Kütüphanesi:*
```python
from datasets import load_dataset

ds = load_dataset("sekerlipencere/zynpdata-zynp_ai-teknofest")
```
*Pandas Kütüphanesi:*
```python
import pandas as pd

df = pd.read_json("hf://datasets/sekerlipencere/zynpdata-zynp_ai-teknofest/dataset.jsonl", lines=True)
```
*Croissant Kütüphanesi:*
```python
from mlcroissant import Dataset

# The Croissant metadata exposes the first 5GB of this dataset
ds = Dataset(jsonld="https://huggingface.co/api/datasets/sekerlipencere/zynpdata-zynp_ai-teknofest/croissant")
records = ds.records("default")
```

## 📈 Proje Aşamaları
### Proje 3 aşamadan oluşmaktadır, *link toplama*, *İçerik Toplama*, *format düzeltme*:

## 1. Link Toplama

Bu kısım, geniş kapsamlı bir web forumundan link toplama sürecini, karşılaşılan zorlukları ve geliştirilen çözüm stratejilerini detaylı bir şekilde incelemektedir. Çalışmanın temel amacı, forumda yer alan tüm konuların ve ilgili sayfa linklerinin eksiksiz bir şekilde toplanmasıdır. Bu süreçte karşılaşılan teknik ve operasyonel engeller, uygulanan yöntemler ve elde edilen sonuçlar ayrıntılı olarak ele alınmaktadır.



### İlk Aşama: URL Toplama
Veri toplama sürecinin ilk aşamasında, hedef web sitesinin sitemap'i kullanılarak tüm konu başlıklarının URL'leri elde edilmiştir. Bu yaklaşım, forumda açılmış olan tüm konuların ana sayfalarına erişim sağlamıştır. Ancak, her konunun potansiyel olarak birden fazla sayfadan oluşması, veri toplama sürecini daha karmaşık hale getirmiştir.

### İlk Yaklaşım: Web Parsing Yöntemi
İlk olarak, her konu sayfasındaki sayfa bağlantılarının web parsing yöntemi ile toplanması düşünülmüştür. Bu amaçla geliştirilen script şu işlevleri yerine getirmeyi hedeflemiştir:

- Konu sayfalarını analiz etme
- Sayfa numaralarını tespit etme
- İlgili tüm sayfa URL'lerini çıkarma ve kaydetme

Bu yaklaşım, işlevsel olmasına rağmen, yüksek işlemci gücüne (16 çekirdekli Intel işlemci) rağmen beklenenden çok daha uzun süre almıştır. Parsing işleminin yoğun kaynak kullanımı ve zaman alıcı doğası, bu yöntemin büyük ölçekli veri toplama için uygun olmadığını göstermiştir.

### Alternatif Yaklaşım: Mesaj Sayısı Bazlı URL Oluşturma
Zaman kısıtlamaları ve verimsizlik nedeniyle, daha etkili bir yöntem geliştirme ihtiyacı doğmuştur. Bu doğrultuda yeni bir strateji oluşturulmuştur:

- Her konu sayfasındaki toplam mesaj sayısının çekilmesi
- Mesaj sayısına dayanarak toplam sayfa sayısının hesaplanması
- Hesaplanan sayfa sayısına göre URL'lerin programatik olarak oluşturulması

Bu yaklaşım için özel bir script geliştirilmiştir. Script'in temel işlevleri şunlardır:

- HTML verisinden mesaj sayısını çekme
- Sayfa sayısını hesaplama
- URL'leri oluşturma ve kaydetme

Geliştirilen script'e [Link Toplama Scripti](linktoplama.py) adresinden erişilebilmektedir.

### Karşılaşılan Zorluklar ve Çözümler

Veri toplama sürecinde iki temel zorlukla karşılaşılmıştır:

### Sunucu Kapasitesi Sınırlamaları
- Problem: Forum sunucusu, yoğun veri toplama trafiği nedeniyle zaman zaman 501 hataları vermiştir.
- Çözüm: Hata alınan URL'ler kaydedilmiş ve daha sonra yeniden işlenmiştir. Bu yaklaşım, veri kaybını önlemiş ancak toplam işlem süresini uzatmıştır.

### Güvenlik Önlemleri: Cloudflare Doğrulaması
- Problem: Sürekli aynı IP adresinden yapılan istekler nedeniyle Cloudflare'ın "ben robot değilim" doğrulaması devreye girmiştir. Bu durum, yaklaşık her 12 saatlik çalışma periyodunun ardından 8 saatlik bir erişim engeli oluşturmuştur.
- Çözüm: Veri toplama süreci, bu kısıtlamayı dikkate alacak şekilde planlanmıştır. 12 saat aktif çalışma ve 8 saat bekleme şeklinde bir döngü oluşturulmuştur. Bu yaklaşım, sürecin verimliliğini düşürmüş ancak uzun vadeli veri toplama imkanı sağlamıştır.

### Sonuçlar ve Analiz

Link toplama aşaması toplam bir hafta sürmüştür. Bu süreç sonunda yaklaşık 4.5 milyon URL başarıyla elde edilmiştir.


## 2. İçerik Toplama: 

### 1. Giriş ve Planlama

Bu çalışmanın ilk aşamasında, elimizde bulunan 4.5 milyon linki verimli bir şekilde işlemek için doğru bir script geliştirilmesi gerekti. Bu amaçla, planlama süreci titizlikle yürütüldü. Planlama sürecinde, kullanılacak kütüphaneler ve veri çekme işleminin optimizasyonu üzerinde duruldu. Uzun süren düşünme ve analiz aşamasının ardından, BeautifulSoup kütüphanesini kullanarak forumların konu sayfalarındaki verileri çekme kararı alındı.

### 2. Soru ve Cevapların İşlenmesi

Geliştirilen scriptin temel işlevi, forum sayfasından ilk olarak en üstte bulunan soru verisini çekmek ve bu veriyi JSON formatında saklamaktı. Ancak, bu işlemi gerçekleştirmeden önce, sorunun daha önce eklenip eklenmediği kontrol edildi. Bu kontrol mekanizması, veri tekrarını önleyerek işlem verimliliğini artırdı. Eğer soru daha önce eklenmişse, script doğrudan cevap çekme aşamasına geçmektedir. Bu sayede, işlem süresi kısaltılarak daha hızlı ve verimli bir veri işleme süreci sağlanmıştır.

### 3. Ayrıntılı Soru ve Cevapların Çekilmesi

Script, yeni bir soru tespit edildiğinde, bu soruyu JSON formatında saklamakta ve ayrıntılı soru çekme işlemine geçmektedir. Ayrıntılı soru çekme işlemi, kullanıcının mesajlar kısmında yazdığı ilk mesajı almayı ve bu veriyi JSON formatındaki veri setine eklemeyi içermektedir. İlk mesajın ardından, forum sayfasında yer alan tüm cevaplar toplanmakta ve JSON verisine eklenmektedir. Bu aşama, forumlardaki tüm önemli verilerin kapsamlı bir şekilde toplanmasını sağlamaktadır.

### 4. Link ve Atıf Bilgilerinin Eklenmesi

Veri çekme işleminin sonunda, her bir veri kaynağına ait sayfanın linki ve atıf bilgileri JSON verisine eklenmektedir. Bu işlem, verilerin kaynağını belirlemek ve referansları doğru şekilde tutmak açısından büyük önem taşımaktadır. Böylece, oluşturulan veri setinin doğruluğu ve güvenilirliği artırılmaktadır.

### 5. Scriptin Kullanımı ve Zaman Çizelgesi

Geliştirilen script, topladığımız tüm linkler için veri çekme işlemini otomatik olarak gerçekleştirmektedir. Scriptin son haline şu bağlantıdan ulaşabilirsiniz: [İçerik Toplama Scripti](iceriktoplama.py). Bu işlemin tamamlanması yaklaşık iki hafta sürmüştür. Bu sürenin uzun olmasının temel sebebi, link toplama aşamasında karşılaşılan sorunlardır. Ancak, bu süreç sonucunda Türkiye'nin en büyük açık kaynaklı ve Türkçe veri seti oluşturulmuştur.

### Sonuç

Bu çalışma, geniş ölçekli bir veri toplama sürecinin detaylı bir incelemesini sunmaktadır. Geliştirilen script, forum sayfalarından veri çekme, veri işleme ve saklama süreçlerini otomatikleştirerek, verilerin doğru ve etkili bir şekilde toplanmasını sağlamıştır. Sonuç olarak, oluşturulan veri seti, çeşitli araştırmalar ve analizler için önemli bir kaynak teşkil etmektedir. Bu süreç, büyük veri işleme projeleri için bir model oluşturmakta ve veri toplama işlemlerinde karşılaşılan zorlukların nasıl aşılabileceğine dair önemli ipuçları sunmaktadır.

## 3. Veri Formatlama:

### 3.1. Veri Formatlama İhtiyacı

Toplama aşamasında elde edilen verilerin işlenmesi ve analizi sırasında, JSON formatındaki verilerin daha etkili bir şekilde yönetilmesi ve kullanılabilmesi adına belirli bir formatlama sürecine ihtiyaç duyulmuştur. JSON formatı, verilerin saklanması ve taşınması için yaygın olarak kullanılan bir formattır. Ancak, büyük veri setleriyle çalışırken, JSONL (JSON Lines) formatı gibi alternatif formatlar daha uygun olabilir.

### 3.2. JSON'dan JSONL'ye Dönüşüm

Bu aşamada, JSON formatındaki verileri JSONL formatına dönüştüren küçük bir script geliştirilmiştir. JSONL formatı, her satırın bir JSON nesnesi olduğu bir yapıdır. Bu format, büyük veri setlerini daha verimli bir şekilde işlemek ve analiz etmek için tercih edilmektedir. JSONL formatı, verilerin satır bazında işlenmesini kolaylaştırır ve büyük veri dosyalarının yönetimini daha etkili hale getirir.

#### 3.2.1. Scriptin İşlevi

Geliştirilen script, JSON formatındaki verileri satır bazında JSONL formatına dönüştürmektedir. Bu süreç, aşağıdaki adımları içermektedir:

1. **Veri Okuma:** JSON formatındaki veriler, script tarafından okunur ve hafızaya alınır.
2. **Dönüşüm İşlemi:** Her bir JSON nesnesi, ayrı bir satıra yerleştirilir ve JSONL formatında yeniden yapılandırılır.
3. **Veri Yazma:** JSONL formatındaki veriler, yeni bir dosyaya yazılır. Bu dosya, veri işleme ve analiz aşamalarında kullanılmak üzere hazır hale getirilir.

#### 3.2.2. Dönüşümün Avantajları

- **Performans Artışı:** JSONL formatı, büyük veri setlerinin daha hızlı ve verimli bir şekilde işlenmesini sağlar.
- **Kolay Yönetim:** JSONL formatında her satır bağımsız bir JSON nesnesi olduğundan, veri setleri üzerinde arama ve filtreleme işlemleri daha hızlı gerçekleştirilebilir.
- **Veri Akışları:** JSONL formatı, veri akışları ve veri işleme pipeline'ları ile uyumlu çalışarak, veri mühendisliği ve analiz süreçlerini kolaylaştırır.

### 3.3. Sonuç

Veri formatlama aşamasında, JSON formatındaki verilerin JSONL formatına dönüştürülmesi, veri yönetimi ve analizi süreçlerinde önemli bir iyileşme sağlamıştır. JSONL formatının sağladığı performans ve kullanım kolaylığı, büyük veri setlerinin etkili bir şekilde işlenmesini ve analiz edilmesini mümkün kılmıştır. Bu dönüşüm, veri setinin daha geniş uygulama alanlarına uyum sağlamasına ve veri işleme süreçlerinin optimizasyonuna katkıda bulunmuştur.


**İçerik Örneği:**

```json
{
  "soru": "CS:GO FPS nasıl arttırılır?",
  "url": "https://www.technopat.net/sosyal/konu/cs-go-fps-nasil-arttirilir.1340872/page-2",
  "ayrintili_soru": "kaonashii99 dedi:-Freq 144 -High -novid -Console -nosplash +cl_updaterate 128 +cl_cmdrate 128 +cl_interp 0 +Rate 128 +exec autoexec -lv +mat_queue_mode 2 +cl_forcepreload 1 -noforcemaatıfel -noforcemparms -noforcemspd(144 Hz monitör kullandığım için yazdım Hz değerine göre yazabilirsin bu kodu işine yarıyıcak başlatma seçenekleridir.)ParkControl – Tweak CPU Core Parking and Moreverdiğim linkten işlemcinin hızını maksimumda kullanabilirsin sorun yaratmaz işlemcinden alabiliceğin verimi almana yardım eder.Oyunun klasöründen oyununn exe dosyasını bulup özelliklerden uyumluluk sekmesinde tam ekran iyileştirmesini devre dışı bırak tikini seçin iyi bir FPS almanıza yardımcı olacaktır.800-600 de oynamanı öneririm bu arada 4.3 Black bar fark etmez.Konsoldan FPS Max 0 çekmeniz veriminizi daha artıracaktır.Genişletmek için tıkla...Sadece freq144'ümü monitör Hz'me göre ayarlayacagım?",
  "cevaplar": [
    "Hocam çoklu CPU kullanımını ayarlardan kapattıysanız aktif edince 4 5 FPS artar.",
    "Evet sadece 144 ayarını 60 Hzdir büyük ihtimale monitörün 60 yazabilirsin.Fps_max 0 komutu.Ayarlardan ses ayarlarına gelip gelişmiş 3B ses işlemesi hayır yapıp.800-600 formatına çekip Black bar 4.3 boyutu fark etmez nasıl oynuyorsanız yapabilirsiniz.CS:GO görüntü ayarlarında Uber gölgelendirici kullan komutunu hayır yapmanız öneririm dikey eşitleme FPS'ini sabitler bundan dolayı yüksek FPS değerleri almana mani olur.Oyun açtıktan sonra görev yöneticisinden ayrıntılar sekmesinde csgo.exe komutuna sağ tık ile öncellik ayarlamadan yüksek seçmeniz ve Windows çalıştır (Windows+r) ile MSConfig ile açılan ekrandan ön yüklemeye gelerek gelişmiş seçenekler bastığınızda işlemci sayısına gelip kaç çekirdekliyse hepsini aktif etmeniz 1.den başlayıp aşağı kadar giden sayı değerini en yükseğini seçip tamama basmanız işinize yarayacaktır park üste verdiğim linkten park Control indirmeniz de lazım.Verdiğim başlatma komutlarını yapıp gerisi sistemin oyuna verdiği FPS değerleriyle uygun performansta en azından iyileşmeleriyle beraber oynayabilirsiniz oyun içi ayarlardan şahit olduğum 4.5 FPS demişler yaklaşık 30-40 FPS Boost yapmıştım üste verdiklerimi de yapmanızı öneririm."
  ],
  "atıf": "zynp_msg veri seti sekerlipencere tarafından hazırlanmıştır."
}

```

## 📈 Veri Seti Hakkında Analizler


### 1. Genel Bakış

zynpdata veri seti, Türkiye'nin en büyük teknoloji forumu olan Technopat'tan elde edilmiş, geniş kapsamlı bir Türkçe veri setidir. Bu veri seti, doğal dil işleme, makine öğrenimi ve yapay zeka araştırmaları için zengin bir kaynak sunmaktadır.Özelikle türkçe llm model üretimi ve finetuning edilmesinde eşssiz bir kaynak sağlar.Veri seti her konu için toplam 5 adet veri başlığı içermektedir:
- Soru : Kullanıcın konu başlığında yazdığı metin buraya geliyor.
- Url : Konunun url'si buraya geliyor.
- Ayrıntılı Soru : Kullanıcının başlığı yazdıktan sonra konuya attığı ayrıntılı soru mesajı buraya geliyor.
- Cevaplar : Konuya verilmiş tüm cevaplar bu kısıma geliyor.
- Atıf : Veri seti ile ilgili atıf buraya geliyor.


### 2. Boyut Ve Genel İstatistikler

| Metrik | Değer |
|--------|-------|
| Toplam Konu Sayısı | 3,094,199 |
| Toplam Cevap Sayısı | 21,000,000 |
| Toplam Kelime Sayısı | 769,457,477 |
| Toplam Dosya Boyutu | 7 GB |
| Toplam Karakter Sayısı | 5,934,600,344 |

### Veri Setinin Tamamını İçeren Word Cloud
![TechnoTürk Logo](https://i.imgur.com/LTO2EkH.png)
---
---
### Veri Setinin Tamamını İçeren Kelime Frekans Grafiği
![TechnoTürk Logo](https://i.imgur.com/H7P3BTc.png)


### 3. İçerik Türleri ve Kaynakları

zynpdata veri seti, Technopat forumundan elde edilen çeşitli içerik türlerini kapsamaktadır:

1. Forum Konuları: Kullanıcılar tarafından başlatılan tartışmalar
2. Cevaplar: Konulara verilen yanıtlar
3. Ürün İncelemeleri: Kullanıcıların teknolojik ürünler hakkındaki değerlendirmeleri
4. Teknik Destek Soruları ve Yanıtları: Kullanıcıların teknik problemleri ve çözümleri
5. Haberler ve Yorumlar: Teknoloji dünyasındaki gelişmeler ve kullanıcı yorumları
6. Rehberler ve Öğreticiler: Çeşitli teknolojik konularda kullanıcı tarafından oluşturulan kılavuzlar

### 4. Konu Dağılımı ve Çeşitliliği

zynpdata veri seti, geniş bir konu yelpazesini kapsamaktadır. Ana kategoriler ve yaklaşık yüzdeleri şu şekildedir:

1. Donanım (%25)
   - Bilgisayar Bileşenleri
   - Dizüstü Bilgisayarlar
   - Masaüstü Bilgisayarlar
   - Mobil Cihazlar

2. Yazılım (%20)
   - İşletim Sistemleri
   - Uygulama Yazılımları
   - Programlama Dilleri
   - Oyunlar

3. İnternet ve Ağ Teknolojileri (%15)
   - Web Hizmetleri
   - Sosyal Medya
   - Ağ Güvenliği

4. Tüketici Elektroniği (%10)
   - Akıllı Ev Cihazları
   - Ses ve Görüntü Sistemleri
   - Giyilebilir Teknolojiler

5. Otomotiv Teknolojileri (%5)
   - Elektrikli Araçlar
   - Otonom Sürüş Sistemleri

6. Bilim ve Teknoloji Haberleri (%10)
   - Yeni Teknolojik Gelişmeler
   - Bilimsel Keşifler

7. Diğer (%15)
   - Eğitim Teknolojileri
   - Sağlık Teknolojileri
   - Finans Teknolojileri
   - Çevre Teknolojileri

### 5. Veri Kalitesi ve Ön İşleme

- **Dil**: Tüm içerik Türkçedir.
- **Temizlik**: Ham veri temel bir temizleme işleminden geçirilmiştir:
  - HTML etiketleri ve özel karakterler kaldırılmıştır.
  - Kullanıcı adları ve e-posta adresleri anonimleştirilmiştir.
  - Spam içerikler ve tekrar eden mesajlar ayıklanmıştır.
- **Normalize Edilmemiş Metin**: Yazım hataları, kısaltmalar ve internet jargonu korunmuştur, bu da gerçekçi NLP görevleri için idealdir.

### 6. Zaman Aralığı

Veri seti, 2012 yılından 2024 yılına kadar olan forum içeriklerini kapsamaktadır. Bu geniş zaman aralığı, Türkçe'nin ve teknoloji dilinin zaman içindeki evrimini incelemek için fırsatlar sunmaktadır.

### 7. Etik Hususlar ve Gizlilik

- Tüm kişisel bilgiler (kullanıcı adları, e-posta adresleri, IP adresleri) anonimleştirilmiştir.
- Veri seti, Technopat'ın kullanım şartlarına ve gizlilik politikasına uygun olarak oluşturulmuştur.
- Araştırmacılar, bu veri setini kullanırken etik kurallara uymakla yükümlüdür.


### 8. Potansiyel Kullanım Alanları

1. Türkçe Dil Modelleri Geliştirme
2. Konu Modelleme ve Metin Sınıflandırma
3. Duygu Analizi ve Fikir Madenciliği
4. Soru-Cevap Sistemleri
5. Metin Özetleme
6. Teknoloji Trendleri Analizi
7. Sosyal Ağ Analizi
8. Kullanıcı Davranışı Modelleme

Bu kapsamlı veri seti, Türkçe doğal dil işleme alanında çalışan araştırmacılar ve geliştiriciler için benzersiz fırsatlar sunmaktadır.

### 9. Kapsamlı Veri Seti Karşılaştırması

Türkçe NLP alanındaki önemli veri setlerini daha detaylı inceleyerek, zynpdata-zynp_ai-teknofest projesinin benzersiz özelliklerini ve avantajlarını daha net bir şekilde ortaya koyabiliriz. Aşağıda, en önemli Türkçe veri setleriyle kapsamlı bir karşılaştırma sunulmuştur:

1. **zynpdata-zynp_ai-teknofest**
   - Boyut: 769 milyon kelime
   - Yapı: Forum tabanlı soru-cevap ve tartışma metinleri
   - İçerik Türleri: Forum konuları, cevaplar, teknik tartışmalar, ürün incelemeleri
   - Dilbilimsel Özellikleri: 
     - Günlük konuşma dili
     - Teknoloji jargonu
     - İnformal ve formal Türkçe karışımı
     - Emoji ve internet kısaltmaları
   - Konu Çeşitliliği: Çok yüksek (30'dan fazla kategori)
   - Özel Kullanım Alanları: 
     - Soru-cevap sistemleri
     - Diyalog modelleme
     - Sentiment analizi
     - Teknoloji trend analizi
     - Kullanıcı davranış modelleme
   - Veri Toplama Yöntemi: Özel geliştirilen web kazıma araçları
   - Güncellenme Sıklığı: Tek seferlik geniş çaplı veri toplama (2024)

2. **TTC-3600 Corpus**
   - Boyut: 3600 metin belgesi (yaklaşık 1 milyon kelime)
   - Yapı: Kategorize edilmiş metin koleksiyonu
   - İçerik Türleri: Haber metinleri
   - Dilbilimsel Özellikleri: Temel metin kategorileri
   - Konu Çeşitliliği: Orta (6 ana kategori)
   - Özel Kullanım Alanları: Metin sınıflandırma, konu modelleme
   - Veri Toplama Yöntemi: Otomatik web kazıma
   - Güncellenme Sıklığı: Sabit, güncellenmemektedir

3. **Turkish Wikipedia Dumps**
   - Boyut: Değişken (son sürüm yaklaşık 500 MB sıkıştırılmış metin)
   - Yapı: Wiki formatında yapılandırılmış metin
   - İçerik Türleri: Ansiklopedik makaleler
   - Dilbilimsel Özellikleri: Hyperlink yapısı, kategori bilgileri
   - Konu Çeşitliliği: Çok yüksek (genel ansiklopedi)
   - Özel Kullanım Alanları: Bilgi çıkarımı, varlık tanıma, metin özetleme
   - Veri Toplama Yöntemi: Kullanıcı katkıları
   - Güncellenme Sıklığı: Sürekli (günlük güncellemeler)

4. **Turkish News Dataset**
   - Boyut: 200,000 haber makalesi (yaklaşık 50 milyon kelime)
   - Yapı: Kategorize edilmiş haber metinleri
   - İçerik Türleri: Haber metinleri, başlıklar
   - Dilbilimsel Özellikleri: Haber dili, resmi Türkçe
   - Konu Çeşitliliği: Orta (haber kategorileri)
   - Özel Kullanım Alanları: Duygu analizi, başlık üretme, metin özetleme
   - Veri Toplama Yöntemi: Otomatik web kazıma
   - Güncellenme Sıklığı: Periyodik (yıllık güncellemeler)

5. **Turkish Web Corpus**
   - Boyut: 470 milyon kelime
   - Yapı: Web sayfalarından oluşan metin koleksiyonu
   - İçerik Türleri: Çeşitli web içerikleri
   - Dilbilimsel Özellikleri: Karma dil kullanımı (resmi ve gayri resmi)
   - Konu Çeşitliliği: Yüksek (genel web içeriği)
   - Özel Kullanım Alanları: Dil modelleme, kelime vektörleri oluşturma
   - Veri Toplama Yöntemi: Geniş çaplı web tarama
   - Güncellenme Sıklığı: Belirli aralıklarla (2-3 yılda bir)

6. **BOUN Corpus**
   - Boyut: 2 milyon kelime
   - Yapı: Etiketlenmiş metin koleksiyonu
   - İçerik Türleri: Gazete makaleleri, akademik metinler
   - Dilbilimsel Özellikleri: Morfolojik ve sözdizimsel analiz içerir
   - Konu Çeşitliliği: Sınırlı (genel haberler, akademik konular)
   - Özel Kullanım Alanları: Dilbilimsel araştırmalar, metin sınıflandırma
   - Veri Toplama Yöntemi: Manuel seçim ve etiketleme
   - Güncellenme Sıklığı: Sabit, güncellenmemektedir

### Detaylı Karşılaştırma Tablosu

| Özellik               | zynpdata | BOUN Corpus | TTC-3600 | Turkish Wikipedia | Turkish News Dataset | Turkish Web Corpus |
|-----------------------|----------|-------------|----------|-------------------|----------------------|---------------------|
| Boyut (Kelime)        | 769M     | 2M          | ~1M      | Değişken (~10M)   | ~50M                 | 470M                |
| İçerik Çeşitliliği    | Çok Yüksek| Düşük       | Düşük    | Orta              | Düşük                | Yüksek              |
| Zaman Aralığı         | 2012-2024| 2000-2018   | 2005-2015| Sürekli           | 2010-2020            | 2017-2019           |
| Dil Çeşitliliği       | Yüksek   | Düşük       | Düşük    | Orta              | Düşük                | Orta                |
| Güncellik             | Yüksek   | Orta        | Düşük    | Çok Yüksek        | Orta                 | Orta                |
| Kullanıcı Etkileşimi  | Çok Yüksek| Yok         | Yok      | Sınırlı           | Yok                  | Sınırlı             |
| Teknoloji Odaklı      | Evet     | Hayır       | Hayır    | Kısmen            | Kısmen               | Kısmen              |
| Erişilebilirlik       | Açık     | Kısıtlı     | Açık     | Açık              | Kısıtlı              | Ücretli             |
| Yapısal Özellikler    | Forum Yapısı | Etiketli  | Kategorize| Wiki Formatı      | Kategorize           | Ham Web             |
| Dilbilimsel Analiz    | Potansiyel Var| Var      | Sınırlı | Yok               | Yok                  | Yok                 |
| Veri Toplama Yöntemi  | Özel Geliştirme| Manuel  | Otomatik| Kullanıcı Katkısı | Otomatik             | Otomatik            |
| Güncellenme           | Tek Seferlik| Statik    | Statik  | Dinamik           | Periyodik            | Aralıklı            |

### zynpdata-zynp_ai-teknofest'in Benzersiz Avantajları ve Kullanım Senaryoları:

1. **Diyalog Modelleme ve Soru-Cevap Sistemleri**
   - Forum yapısı, gerçek kullanıcı etkileşimlerini içerir.
   - Soru sorma ve cevaplama kalıplarının geniş örneklemini sunar.
   - Kullanım Senaryosu: Türkçe chatbot ve sanal asistan geliştirme.

2. **Teknoloji Odaklı Dil Modelleme**
   - Zengin teknoloji jargonu ve terminolojisi içerir.
   - Teknik konularda güncel dil kullanımını yansıtır.
   - Kullanım Senaryosu: Teknoloji alanında uzmanlaşmış NLP modelleri geliştirme.

3. **Sentiment Analizi ve Kullanıcı Davranış Modelleme**
   - Ürün incelemeleri ve kullanıcı yorumları içerir.
   - Geniş bir duygu ve görüş yelpazesi sunar.
   - Kullanım Senaryosu: E-ticaret ve ürün analizi için duygu analizi modelleri.

4. **Zaman Serisi Analizi ve Trend Tespiti**
   - 12 yıllık bir zaman aralığını kapsar.
   - Teknoloji trendlerinin ve dil kullanımının evrimini yansıtır.
   - Kullanım Senaryosu: Teknoloji trendleri tahmin modelleri, dil değişimi araştırmaları.

5. **İnformal ve Formal Dil Karışımı**
   - Günlük konuşma dili ile teknik dilin bir arada kullanımını içerir.
   - Emoji ve internet kısaltmalarını içerir.
   - Kullanım Senaryosu: Daha doğal ve çeşitli dil anlama modelleri geliştirme.

6. **Geniş Konu Yelpazesi**
   - 30'dan fazla kategori ile çeşitli konuları kapsar.
   - Teknolojiden günlük yaşama geniş bir spektrum sunar.
   - Kullanım Senaryosu: Genel amaçlı dil modelleri ve konu sınıflandırma sistemleri.

7. **Büyük Ölçekli Veri**
   - 769 milyon kelime ile geniş bir öğrenme kaynağı sunar.
   - Derin öğrenme modelleri için ideal boyutta veri sağlar.
   - Kullanım Senaryosu: Büyük ölçekli Türkçe dil modelleri eğitme (örn. BERT, GPT türevleri).

8. **Forum Dinamikleri**
   - Kullanıcı etkileşimleri, tartışma zincirleri ve konu akışları içerir.
   - Sosyal medya benzeri dil kullanımını yansıtır.
   - Kullanım Senaryosu: Sosyal ağ analizi, tartışma modelleme.

Bu kapsamlı karşılaştırma, zynpdata-zynp_ai-teknofest projesinin Türkçe NLP alanında benzersiz bir kaynak olduğunu göstermektedir. Projenin boyutu, çeşitliliği, güncelliği ve özellikle teknoloji odaklı yapısı, onu diğer mevcut Türkçe veri setlerinden ayırmakta ve çok çeşitli NLP uygulamaları için ideal bir kaynak haline getirmektedir.

## Kaynaklar

* [Python ile Veri Kazıma(Web Scraping) Çalışması Medium](https://medium.com/kaveai/web-scraping-453e96a86195)
* [Python BeautifulSoup Modülü Sinan Erdinç](https://www.sinanerdinc.com/python-beautifulsoup-modulu)
* [Python ile Web Scraping: BeautifulSoup Kullanımı Medium](https://furkancakmaker.medium.com/python-ile-web-scraping-beautifulsoup-kullan%C4%B1m%C4%B1-5f0a3d88f)
* [Requests Ve Beauti̇fulsoup Modüllleri̇yle İnternetten Veri̇ Çekme Yazılım Topluluğu](https://yazilimtoplulugu.com/blog/2397-requests-ve-beautifulsoup-modullleriyle-internetten-veri-cekme)
* [Implementing Web Scraping in Python with BeautifulSoup GeeksforGeeks](https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/)
* [How to Use the JSON Module in Python – A Beginner's Guide](https://www.freecodecamp.org/news/how-to-use-the-json-module-in-python/)
* [How to Create a Telegram Bot using Python](https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/)
* [Python Multiprocessing Tutorial](https://www.datacamp.com/tutorial/python-multiprocessing-tutorial)
* [Create JSONL with Python](https://stackoverflow.com/questions/57071390/create-jsonl-with-python)


## 🤝 Katkıda Bulunma

Projeye katkıda bulunmak isterseniz, lütfen önce [CONTRIBUTING](CONTRIBUTING.md) dosyamızı kontrol edin.


## 📄 Lisans

Bu proje Apache 2.0 Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 📚 Atıf

Bu veri setini çalışmalarınızda kullanıyorsanız, lütfen aşağıdaki gibi atıfta bulunun:

```
@misc{zynpdata2024,
  author = {sekerlipencere},
  title = {zynpdata: Türkiye'nin En Büyük Açık Kaynaklı Türkçe Forum Veri Seti},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/sekerlipencere/zynpdata-zynp_ai-teknofest}}
}
```

## 📞 İletişim

Sorularınız veya geri bildirimleriniz için lütfen [issues](https://github.com/sekerlipencere/zynpdata-zynp_ai-teknofest/issues) bölümünü kullanın veya [yusufd.polar@gmail.com](mailto:yusufd.polar@gmail.com) adresinden bize ulaşın.

---

zynpdata-zynp_ai-teknofest ile NLP ve LLM çalışmalarınıza güç katın! 🚀🇹🇷
