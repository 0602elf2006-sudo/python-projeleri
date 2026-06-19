#PROJE 1: Öğrenci Not Kontrol Sistemi
ogrenciler = ["ali", "ayşe", "elif"]
notlar = [70, 85, 40]
while True:
 ogrencı_listesi=input("öğrenci adını giriniz:")
 index=ogrenciler.index(ogrencı_listesi)
 notu=notlar[index]
 if  notu>50:
    print("gecti")
 elif  notu <=50:
    print("kaldı")
    #bu alıstırma notu eger lıstede olmayan isim yazacaksan önce if yaz sonra index yaz cunku index
    #kontrol etmez direkt hata verir o yuzden once if sonra index

 def selamla():
  print("Merhaba!")
  print("Umarım günün güzel geçiyordur.")
# 2. Çağırma (Calling)
# Fonksiyonun adını ve parantezlerini yazarak çalıştırırız.
  selamla()

 
