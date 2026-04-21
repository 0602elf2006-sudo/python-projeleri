veri=input("veri gir:")
temiz_veri=veri
if len(temiz_veri) ==0:
    print("bu veri eksik")
elif "@" in  temiz_veri:
    print("bu veri geçerli")
else:
    print("hatalı veri")
 