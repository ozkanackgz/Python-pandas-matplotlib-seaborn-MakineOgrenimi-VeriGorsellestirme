import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px




df_yangin_sayisi = pd.read_csv("yangin_sayisi_ve_buyuklugu.csv")
df_ay_yil_bazinda = pd.read_csv("ay_yil_bazinda.csv")
df_yangin_sebepleri = pd.read_csv("yangin_sebepleri.csv")
df_ilce_bazli_mudurlukler = pd.read_csv("ilce_bazli_mudurlukler.csv", encoding="ISO-8859-9")


#ilçe bazlı yangın sayılarını gösteren grafik
plt.figure(figsize=(10, 6))
sns.barplot(data=df_yangin_sayisi, x="ilce", y="adet")
plt.xticks(rotation=45)
plt.title("İlçe Bazlı Yangın Sayıları")
plt.xlabel("İlçeler")
plt.ylabel("Yangın Sayısı")
plt.show()





#ilçe ve yanan hektar büyüklüğünü gösteren grafik
df_yangin_sayisi = pd.read_csv("yangin_sayisi_ve_buyuklugu.csv")


plt.figure(figsize=(10, 6))
plt.scatter(df_yangin_sayisi['ilce'], df_yangin_sayisi['hektar'], alpha=0.5)
plt.title('İlçe ve Yangın Alanı Scatter Plot')
plt.xlabel('İlçe')
plt.ylabel('Yangın Alanı (Hektar)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()


plt.show()





#yangınların hektar cinsinden büyüklüklerini kullanarak en sık yangın çıkan ilk 5 ilçe
df_yangin_sayisi = pd.read_csv("yangin_sayisi_ve_buyuklugu.csv")


ilce_yangin_alani = df_yangin_sayisi.groupby('ilce')['hektar'].sum()


top_5_ilceler = ilce_yangin_alani.nlargest(5)


plt.figure(figsize=(10, 6))
bar_plot = top_5_ilceler.plot(kind='bar', color='skyblue')
plt.title('En Sık Yangın Çıkan İlçeler (Hektar cinsinden)')
plt.xlabel('İlçe')
plt.ylabel('Yanan Alan (Hektar)')
plt.xticks(rotation=45)


for index, value in enumerate(top_5_ilceler):
  bar_plot.text(index, value + 0.1, f"{value:.2f}", ha='center')

plt.grid(axis='y')
plt.tight_layout()


plt.show()




#ilçelere göre yangın yoğunluğunu göstermek için bir ısı haritası
df_yangin_sayisi = pd.read_csv("yangin_sayisi_ve_buyuklugu.csv")


yangin_alani_ilceye_gore = df_yangin_sayisi.groupby('ilce')['hektar'].sum().reset_index()


pivot_table = yangin_alani_ilceye_gore.pivot_table(index='ilce', aggfunc='sum').fillna(0)


plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, cmap='YlOrRd', linewidths=0.5, linecolor='black')
plt.title('İlçelere Göre Yangın Yoğunluğu (Hektar cinsinden)')
plt.xlabel('İlçe')
plt.ylabel('')


plt.show()





#yıllara göre yangın sayısını gösteren grafik
df_ay_yil_bazinda = pd.read_csv("ay_yil_bazinda.csv")


yanginlar_yillara_gore = df_ay_yil_bazinda.groupby('yil')['adet'].sum()


plt.figure(figsize=(12, 6))
plt.plot(yanginlar_yillara_gore.index, yanginlar_yillara_gore.values, marker='o', color='b', linestyle='-')
plt.title('Yıllara Göre Yangın Sayısı')
plt.xlabel('Yıl')
plt.ylabel('Yangın Sayısı')
plt.grid(True)
plt.tight_layout()


plt.show()







#her ayın yangın sayısını gruplayıp çubuk grafiği halinde gösteren grafik
df = pd.read_csv("ay_yil_bazinda.csv")


yanginlar_aylara_gore = df.groupby('ay')['adet'].sum().reset_index()


ay_isimleri = ['ocak', 'subat', 'mart', 'nisan', 'mayis', 'haziran', 'temmuz', 'agustos', 'eylul', 'ekim', 'kasim', 'aralik']
yanginlar_aylara_gore['ay'] = pd.Categorical(yanginlar_aylara_gore['ay'], categories=ay_isimleri, ordered=True)


yanginlar_aylara_gore.sort_values('ay', inplace=True)


plt.figure(figsize=(10, 6))
plt.plot(yanginlar_aylara_gore['ay'], yanginlar_aylara_gore['adet'], marker='o', color='b', linestyle='-')
plt.title('Aylara Göre Yangın Adetleri')
plt.xlabel('Ay')
plt.ylabel('Yangın Adedi')
plt.grid(True)
plt.xticks(rotation=45)  # Ay isimlerini döndür
plt.tight_layout()


plt.show()






#her bir ayda toplam ne kadar büyüklükte yangın olduğunu gösteren çubuk grafiği
df = pd.read_csv("ay_yil_bazinda.csv")


yanginlar_aylara_gore = df.groupby('ay')['hektar'].sum().reset_index()


ay_isimleri = ['ocak', 'subat', 'mart', 'nisan', 'mayis', 'haziran', 'temmuz', 'agustos', 'eylul', 'ekim', 'kasim', 'aralik']
yanginlar_aylara_gore['ay'] = pd.Categorical(yanginlar_aylara_gore['ay'], categories=ay_isimleri, ordered=True)


yanginlar_aylara_gore.sort_values('ay', inplace=True)


plt.figure(figsize=(10, 6))
plt.bar(yanginlar_aylara_gore['ay'], yanginlar_aylara_gore['hektar'], color='orange')
plt.title('Aylara Göre Toplam Yangın Büyüklükleri')
plt.xlabel('Ay')
plt.ylabel('Yangın Büyüklüğü (Hektar)')
plt.grid(axis='y')
plt.xticks(rotation=45)  # Ay isimlerini döndür
plt.tight_layout()


plt.show()








#Aydın İşletme Müdürlüğüne bağlı işletme şefliklerinde kaçar adet yangın çıktığını gösteren grafik
df = pd.read_csv("ilce_bazli_mudurlukler.csv", encoding='ISO-8859-1')


aydin_df = df[df['isletmemudurluk'] == 'AYDIN']


yangin_adetleri = aydin_df.groupby('isletmeseflik')['adet'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(yangin_adetleri['isletmeseflik'], yangin_adetleri['adet'], color='skyblue')
plt.title('Aydın İşletme Müdürlüğüne Bağlı İşletme Şefliklerindeki Toplam Yangın Adetleri')
plt.xlabel('İşletme Şefliği')
plt.ylabel('Toplam Yangın Adeti')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()






df = pd.read_csv("ilce_bazli_mudurlukler.csv", encoding='ISO-8859-1')


fethiye_df = df[df['isletmemudurluk'] == 'FETHIYE']


yangin_adetleri = fethiye_df.groupby('isletmeseflik')['adet'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(yangin_adetleri['isletmeseflik'], yangin_adetleri['adet'], color='skyblue')
plt.title('FETHIYE İşletme Müdürlüğüne Bağlı İşletme Şefliklerindeki Toplam Yangın Adetleri')
plt.xlabel('İşletme Şefliği')
plt.ylabel('Toplam Yangın Adeti')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()







df = pd.read_csv("ilce_bazli_mudurlukler.csv", encoding='ISO-8859-1')


koycegiz_df = df[df['isletmemudurluk'] == 'KOYCEGIZ']


yangin_adetleri = koycegiz_df.groupby('isletmeseflik')['adet'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(yangin_adetleri['isletmeseflik'], yangin_adetleri['adet'], color='skyblue')
plt.title('KOYCEGIZ İşletme Müdürlüğüne Bağlı İşletme Şefliklerindeki Toplam Yangın Adetleri')
plt.xlabel('İşletme Şefliği')
plt.ylabel('Toplam Yangın Adeti')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()







df = pd.read_csv("ilce_bazli_mudurlukler.csv", encoding='ISO-8859-1')


marmaris_df = df[df['isletmemudurluk'] == 'MARMARIS']


yangin_adetleri = marmaris_df.groupby('isletmeseflik')['adet'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(yangin_adetleri['isletmeseflik'], yangin_adetleri['adet'], color='skyblue')
plt.title('MARMARIS İşletme Müdürlüğüne Bağlı İşletme Şefliklerindeki Toplam Yangın Adetleri')
plt.xlabel('İşletme Şefliği')
plt.ylabel('Toplam Yangın Adeti')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()









df = pd.read_csv("ilce_bazli_mudurlukler.csv", encoding='ISO-8859-1')


milas_df = df[df['isletmemudurluk'] == 'MILAS']


yangin_adetleri = milas_df.groupby('isletmeseflik')['adet'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(yangin_adetleri['isletmeseflik'], yangin_adetleri['adet'], color='skyblue')
plt.title('MILAS İşletme Müdürlüğüne Bağlı İşletme Şefliklerindeki Toplam Yangın Adetleri')
plt.xlabel('İşletme Şefliği')
plt.ylabel('Toplam Yangın Adeti')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()








df = pd.read_csv("ilce_bazli_mudurlukler.csv", encoding='ISO-8859-1')


mugla_df = df[df['isletmemudurluk'] == 'MUGLA']


yangin_adetleri = mugla_df.groupby('isletmeseflik')['adet'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(yangin_adetleri['isletmeseflik'], yangin_adetleri['adet'], color='skyblue')
plt.title('MUGLA İşletme Müdürlüğüne Bağlı İşletme Şefliklerindeki Toplam Yangın Adetleri')
plt.xlabel('İşletme Şefliği')
plt.ylabel('Toplam Yangın Adeti')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()






df = pd.read_csv("ilce_bazli_mudurlukler.csv", encoding='ISO-8859-1')


nazilli_df = df[df['isletmemudurluk'] == 'NAZILLI']


yangin_adetleri = nazilli_df.groupby('isletmeseflik')['adet'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(yangin_adetleri['isletmeseflik'], yangin_adetleri['adet'], color='skyblue')
plt.title('NAZILLI İşletme Müdürlüğüne Bağlı İşletme Şefliklerindeki Toplam Yangın Adetleri')
plt.xlabel('İşletme Şefliği')
plt.ylabel('Toplam Yangın Adeti')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()






df = pd.read_csv("ilce_bazli_mudurlukler.csv", encoding='ISO-8859-1')


yatagan_df = df[df['isletmemudurluk'] == 'YATAGAN']


yangin_adetleri = yatagan_df.groupby('isletmeseflik')['adet'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(yangin_adetleri['isletmeseflik'], yangin_adetleri['adet'], color='skyblue')
plt.title('YATAGAN İşletme Müdürlüğüne Bağlı İşletme Şefliklerindeki Toplam Yangın Adetleri')
plt.xlabel('İşletme Şefliği')
plt.ylabel('Toplam Yangın Adeti')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()






df = pd.read_csv("ilce_bazli_mudurlukler.csv", encoding='ISO-8859-1')


yilanli_df = df[df['isletmemudurluk'] == 'YILANLI']


yangin_adetleri = yilanli_df.groupby('isletmeseflik')['adet'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(yangin_adetleri['isletmeseflik'], yangin_adetleri['adet'], color='skyblue')
plt.title('YILANLI İşletme Müdürlüğüne Bağlı İşletme Şefliklerindeki Toplam Yangın Adetleri')
plt.xlabel('İşletme Şefliği')
plt.ylabel('Toplam Yangın Adeti')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()






df = pd.read_csv("ilce_bazli_mudurlukler.csv", encoding='ISO-8859-1')


kavaklidere_df = df[df['isletmemudurluk'] == 'KAVAKLIDERE']


yangin_adetleri = kavaklidere_df.groupby('isletmeseflik')['adet'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(yangin_adetleri['isletmeseflik'], yangin_adetleri['adet'], color='skyblue')
plt.title('KAVAKLIDERE İşletme Müdürlüğüne Bağlı İşletme Şefliklerindeki Toplam Yangın Adetleri')
plt.xlabel('İşletme Şefliği')
plt.ylabel('Toplam Yangın Adeti')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()







df = pd.read_csv("ilce_bazli_mudurlukler.csv", encoding='ISO-8859-1')


dalaman_df = df[df['isletmemudurluk'] == 'DALAMAN']


yangin_adetleri = dalaman_df.groupby('isletmeseflik')['adet'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(yangin_adetleri['isletmeseflik'], yangin_adetleri['adet'], color='skyblue')
plt.title('DALAMAN İşletme Müdürlüğüne Bağlı İşletme Şefliklerindeki Toplam Yangın Adetleri')
plt.xlabel('İşletme Şefliği')
plt.ylabel('Toplam Yangın Adeti')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()





df = pd.read_csv("ilce_bazli_mudurlukler.csv", encoding='ISO-8859-1')


seydikemer_df = df[df['isletmemudurluk'] == 'SEYDIKEMER']


yangin_adetleri = seydikemer_df.groupby('isletmeseflik')['adet'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(yangin_adetleri['isletmeseflik'], yangin_adetleri['adet'], color='skyblue')
plt.title('SEYDIKEMER İşletme Müdürlüğüne Bağlı İşletme Şefliklerindeki Toplam Yangın Adetleri')
plt.xlabel('İşletme Şefliği')
plt.ylabel('Toplam Yangın Adeti')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()








#her bir yangın sebebine göre toplam yangın adetlerini gösteren grafik
df = pd.read_csv("yangin_sebepleri.csv")


yangin_sebepleri = df.groupby('yanginsebebi')['adet'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(yangin_sebepleri['yanginsebebi'], yangin_sebepleri['adet'], color='orange')
plt.title('Yangın Sebeplerine Göre Toplam Yangın Adetleri')
plt.xlabel('Yangın Sebebi')
plt.ylabel('Toplam Yangın Adeti')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()







#her bir yangın sebebine göre toplam yangın büyüklüklerini gösteren grafik
df = pd.read_csv("yangin_sebepleri.csv")


yangin_sebepleri = df.groupby('yanginsebebi')['hektar'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(yangin_sebepleri['yanginsebebi'], yangin_sebepleri['hektar'], color='green')
plt.title('Yangın Sebeplerine Göre Toplam Yangın Büyüklükleri')
plt.xlabel('Yangın Sebebi')
plt.ylabel('Toplam Yangın Büyüklüğü (Hektar)')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()









