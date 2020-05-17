ad = input("Oyuncu adı:") #Burda kullanıcıdan girdi(input) bekliyoruz bu girdi "ad"a ekleniyor
ozellik = input("Oyuncunun özelliği:")
silahi = input("Oyuncunun silahı:")
scl = input("Oyuncunun Puanı 1:")
scl2 = input("Oyuncunun Puanı 2:")
scl3 = input("Oyuncunun Puanı 3:")

print("         Oyuncu Bilgileri")
print("Oyuncun adı:", ad) #Bu kısımda topladığımız verileri kullanarak bilgileri yazdırıyoruz
print("Oyuncun özelliği:",ozellik)
print("Oyuncun silahı:", silahi)
print("Oyuncun Toplam Puanı:", int(scl) + int(scl2) + int(scl3))
#Yukardaki kısımda oyunucunun puanını toplamak istersek String yani yazı olarak toplayacağından değerimizi int ye dönüştürdük