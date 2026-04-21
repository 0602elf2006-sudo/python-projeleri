sehirler = ["ankara", "istanbul", "izmir", "antalya"]
for i in sehirler:
   print("SEHİR:",i)



sayilar = [10, 20, 30, 40, 50]
sayı_listesi=int(input("bir sayı giriniz:"))
if sayı_listesi in sayilar:
   sayilar.index(sayı_listesi)
   print("index:",sayilar.index(sayı_listesi))
   
elif sayı_listesi  not in sayilar:
   print("bu sayı lıstede yok")


urunler = ["kalem", "defter", "silgi"]
fiyatlar = [10, 20, 5]
urun_listesi=input("bir ürün giriniz:") 
index=urunler.index(urun_listesi)
fiyat=fiyatlar[index]
print(fiyat)





