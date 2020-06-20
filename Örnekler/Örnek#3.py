isim = input("İsminizi ve Soyadınızı girin ")
vize = int(input("Vize puanınızı girin "))
final = int(input("Final puanınızı girin "))
vizes = int(vize * 0.4)
finals = int(final * 0.6)
toplam = int(vizes + finals)

if(101 < toplam > 84):
    print("AA")

elif(85 < toplam > 69):
    print("AB")

elif(70 < toplam > 59):
    print("BB")

elif(60 < toplam > 49):
    print("BC")

elif(50 < toplam > 39):
    print("CC")
    
elif(40 < toplam > 0):
    print("FF")





