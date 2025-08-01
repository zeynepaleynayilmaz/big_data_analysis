import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Excel dosyasını oku
df = pd.read_excel('trafikKaza.xlsx')

# Veri setini gözden geçir
print(df.head())

# Görselleştirmeleri oluşturmak için alt grafiklerin düzeni
fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(15, 20))
fig.suptitle('Trafik Kazaları Analizi', fontsize=20)

# 1. Görsel: Kaza Türü Dağılımı
sns.countplot(x='KAZA TURU', data=df, ax=axes[0, 0])
axes[0, 0].set_title('Kaza Türü Dağılımı')

# 2. Görsel: Aylık Kaza Sayısı
monthly_accidents = df.groupby('AY')['KAZA TARIHI'].count()
monthly_accidents.plot(kind='bar', ax=axes[0, 1])
axes[0, 1].set_title('Aylık Kaza Sayısı')

# 3. Görsel: Mevsime Göre Kaza Dağılımı
sns.countplot(x='MEVSİM', data=df, ax=axes[1, 0])
axes[1, 0].set_title('Mevsime Göre Kaza Dağılımı')

# 4. Görsel: Kaza Saat Dağılımı
sns.histplot(df['KAZA SAAT'], bins=24, ax=axes[1, 1])
axes[1, 1].set_title('Kaza Saat Dağılımı')

# 5. Görsel: İlçeye Göre Kaza Sayısı
sns.countplot(x='ILCE', data=df, ax=axes[2, 0])
axes[2, 0].set_title('İlçeye Göre Kaza Sayısı')
axes[2, 0].tick_params(axis='x', rotation=45)

# 6. Görsel: Olu Nedenine Göre Kaza Sayısı
sns.countplot(x='OLUS NEDENI', data=df, ax=axes[2, 1])
axes[2, 1].set_title('Olu Nedenine Göre Kaza Sayısı')
axes[2, 1].tick_params(axis='x', rotation=45)

# 7. Görsel: Yol Kaplama Türü Dağılımı
sns.countplot(x='KAPLAMA CINSI', data=df, ax=axes[3, 0])
axes[3, 0].set_title('Yol Kaplama Türü Dağılımı')
axes[3, 0].tick_params(axis='x', rotation=45)

# 8. Görsel: Araç Tipine Göre Kaza Sayısı
sns.countplot(x='ARAC CINSI', data=df, ax=axes[3, 1])
axes[3, 1].set_title('Araç Tipine Göre Kaza Sayısı')
axes[3, 1].tick_params(axis='x', rotation=45)

# 9. Görsel: Sürücü Cinsiyetine Göre Kaza Sayısı
sns.countplot(x='SURUCU CINSIYET', data=df, ax=axes[4, 0])
axes[4, 0].set_title('Sürücü Cinsiyetine Göre Kaza Sayısı')

# 10. Görsel: Sürücü Eğitim Durumuna Göre Kaza Sayısı
sns.countplot(x='SURUCU EGITIM DURUMU', data=df, ax=axes[4, 1])
axes[4, 1].set_title('Sürücü Eğitim Durumuna Göre Kaza Sayısı')
axes[4, 1].tick_params(axis='x', rotation=45)

# Görseller arasındaki boşlukları ayarla
plt.tight_layout(rect=[5, 5, 5, 5])

# Görseli göster
plt.show()

# Kaza Türü Dağılımı
plt.figure(figsize=(10, 6))
sns.countplot(x='KAZA TURU', data=df)
plt.title('Kaza Türü Dağılımı')
plt.xlabel('Kaza Türü')
plt.ylabel('Toplam Kaza Sayısı')
plt.xticks(rotation=45)
plt.show()

# Aylara Göre Kaza Sayısı
plt.figure(figsize=(12, 6))
sns.countplot(x='AY', data=df, order=df['AY'].value_counts().index)
plt.title('Aylara Göre Kaza Sayısı')
plt.xlabel('Ay')
plt.ylabel('Toplam Kaza Sayısı')
plt.show()

# Kaza Saati Dağılımı
plt.figure(figsize=(12, 6))
sns.histplot(df['KAZA SAAT'], bins=24, kde=False)
plt.title('Kaza Saati Dağılımı')
plt.xlabel('Kaza Saati')
plt.ylabel('Toplam Kaza Sayısı')
plt.show()

# Kaza Nedenlerine Göre Dağılım
plt.figure(figsize=(12, 6))
sns.countplot(x='OLUS NEDENI', data=df, order=df['OLUS NEDENI'].value_counts().index)
plt.title('Kaza Nedenlerine Göre Dağılım')
plt.xlabel('Kaza Nedeni')
plt.ylabel('Toplam Kaza Sayısı')
plt.xticks(rotation=90)
plt.show()

# Olu Sayısı ve Yaralı Sayısı İlişkisi
plt.figure(figsize=(10, 6))
sns.scatterplot(x='OLU SAYISI', y='YARALI SAYISI', data=df)
plt.title('Olu Sayısı ve Yaralı Sayısı İlişkisi')
plt.xlabel('Olu Sayısı')
plt.ylabel('Yaralı Sayısı')
plt.show()

# Mevsime Göre Kaza Sayısı
plt.figure(figsize=(10, 6))
sns.countplot(x='MEVSİM', data=df, order=df['MEVSİM'].value_counts().index)
plt.title('Mevsime Göre Kaza Sayısı')
plt.xlabel('Mevsim')
plt.ylabel('Toplam Kaza Sayısı')
plt.show()

# İlçelere Göre Kaza Sayısı
plt.figure(figsize=(16, 8))
sns.countplot(x='ILCE', data=df, order=df['ILCE'].value_counts().index)
plt.title('İlçelere Göre Kaza Sayısı')
plt.xlabel('İlçe')
plt.ylabel('Toplam Kaza Sayısı')
plt.xticks(rotation=90)
plt.show()

# Hava Durumuna Göre Kaza Sayısı
plt.figure(figsize=(10, 6))
sns.countplot(x='KAPLAMA CINSI', data=df, order=df['KAPLAMA CINSI'].value_counts().index)
plt.title('Hava Durumuna Göre Kaza Sayısı')
plt.xlabel('Hava Durumu')
plt.ylabel('Toplam Kaza Sayısı')
plt.xticks(rotation=45)
plt.show()

# Araç Cinsi Dağılımı
plt.figure(figsize=(14, 8))
sns.countplot(x='ARAC CINSI', data=df, order=df['ARAC CINSI'].value_counts().index)
plt.title('Araç Cinsi Dağılımı')
plt.xlabel('Araç Cinsi')
plt.ylabel('Toplam Kaza Sayısı')
plt.xticks(rotation=45)
plt.show()

# Kusurlu Sürücüye Göre Kaza Sayısı
plt.figure(figsize=(12, 6))
sns.countplot(x='SURUCU KUSURU', data=df, order=df['SURUCU KUSURU'].value_counts().index)
plt.title('Kusurlu Sürücüye Göre Kaza Sayısı')
plt.xlabel('Kusur Durumu')
plt.ylabel('Toplam Kaza Sayısı')
plt.xticks(rotation=45)
plt.show()

# İlçelere Göre Ölü ve Yaralı Sayısı
plt.figure(figsize=(16, 8))
sns.barplot(x='ILCE', y='OLU SAYISI', data=df, order=df.groupby('ILCE')['OLU SAYISI'].mean().sort_values(ascending=False).index)
sns.barplot(x='ILCE', y='YARALI SAYISI', data=df, order=df.groupby('ILCE')['YARALI SAYISI'].mean().sort_values(ascending=False).index)
plt.title('İlçelere Göre Ortalama Ölü ve Yaralı Sayısı')
plt.xlabel('İlçe')
plt.ylabel('Ortalama Sayı')
plt.xticks(rotation=90)
plt.legend(['Ölü Sayısı', 'Yaralı Sayısı'])
plt.show()

# Kaza Türüne Göre Olu ve Yaralı Dağılımı
plt.figure(figsize=(12, 6))
sns.boxplot(x='KAZA TURU', y='OLU SAYISI', data=df)
sns.boxplot(x='KAZA TURU', y='YARALI SAYISI', data=df)
plt.title('Kaza Türüne Göre Ölü ve Yaralı Dağılımı')
plt.xlabel('Kaza Türü')
plt.ylabel('Sayı')
plt.xticks(rotation=45)
plt.legend(['Ölü Sayısı', 'Yaralı Sayısı'])
plt.show()

# Kaza Saatine Göre Olu ve Yaralı Sayısı
plt.figure(figsize=(14, 8))
sns.lineplot(x='KAZA SAAT', y='OLU SAYISI', data=df)
sns.lineplot(x='KAZA SAAT', y='YARALI SAYISI', data=df)
plt.title('Kaza Saatine Göre Ölü ve Yaralı Sayısı')
plt.xlabel('Kaza Saati')
plt.ylabel('Sayı')
plt.legend(['Ölü Sayısı', 'Yaralı Sayısı'])
plt.show()

# Kusurlu Sürücülerin Eğitim Durumuna Göre Dağılım
plt.figure(figsize=(12, 6))
sns.countplot(x='SURUCU KUSURU', hue='SURUCU EGITIM DURUMU', data=df, order=df['SURUCU KUSURU'].value_counts().index)
plt.title('Kusurlu Sürücülerin Eğitim Durumuna Göre Dağılım')
plt.xlabel('Kusur Durumu')
plt.ylabel('Toplam Kaza Sayısı')
plt.xticks(rotation=45)
plt.legend(title='Eğitim Durumu')
plt.show()

# Pandas kütüphanesini 'pd' kısaltmasıyla içe aktar
import pandas as pd

# Seaborn kütüphanesini 'sns' kısaltmasıyla içe aktar
import seaborn as sns

# Plotly Express kütüphanesini 'px' kısaltmasıyla içe aktar
import plotly.express as px

# Matplotlib kütüphanesini 'plt' kısaltmasıyla içe aktar
import matplotlib.pyplot as plt

# WordCloud kütüphanesinden WordCloud sınıfını içe aktar
from wordcloud import WordCloud

# ZeynepAleynaYilmaz ÖğrenciNo: 221001500

# Excel dosyasını oku
df = pd.read_excel('data/trafikKaza.xlsx')

# 'OLUS NEDENI' sütunundaki değerleri birleştirerek bir metin oluştur
wordcloud_text = ' '.join(df['OLUS NEDENI'].dropna())

# WordCloud nesnesini oluştur, genişlik, yükseklik ve arka plan rengi belirle
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(wordcloud_text)

# Matplotlib figür boyutunu belirle
plt.figure(figsize=(10, 6))

# WordCloud'u görselleştir
plt.imshow(wordcloud, interpolation='bilinear')

# Eksenleri kapat
plt.axis('off')

# Görselin başlığını belirle
plt.title('Kazaya Neden Olan Unsurların Kelime Bulutu')

# Görseli göster
plt.show()

# Yorum Satırı: Excel dosyası okunuyor ve 'OLUS NEDENI' sütunundaki veriler kullanılarak bir kelime bulutu oluşturuluyor.
# 'wordcloud_text' değişkeni, WordCloud nesnesi oluşturulmadan önce 'OLUS NEDENI' sütunundaki değerleri içeriyor.
# Kelime bulutu, bu unsurların frekanslarına göre boyutlandırılmış ve görselleştirilmiştir.
# Bu görselleştirme, kazaya neden olan unsurların veri setindeki dağılımını anlamak için kullanılabilir.
