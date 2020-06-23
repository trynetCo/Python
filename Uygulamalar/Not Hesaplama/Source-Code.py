while(True):
    txt = open("Notlar.txt", "a")
    sinif = input("Sınıfı yazınız: ")
    ogr = int(input("Öğrenci Sayısını girin: "))
    print("\n--------{}--------\n".format(sinif),file=txt)
    while ogr > 0:
        nota = "str"
        isim = input("İsim ve soyisim girin: ")
        vize = int(input("Vize puanı girin: "))
        final = int(input("Final puanı girin: "))
        if(vize > 100 or final > 100):
            print("Vize Yada Final Notunu Yanlış Girdiniz Lütfen Bilgileri En Baştan Yazın")
            continue
        if(vize < 0 or final < 0):
            print("Vize Yada Final Notunu Yanlış Girdiniz Lütfen Bilgileri En Baştan Yazın")
            continue
        vizes = float(40 * vize / 100)
        finals = float(60 * final / 100)
        print("Vize puanı {} ".format(vizes))
        print("Final Puanı {} ".format(finals))
        toplam = float(finals + vizes)
        print("Toplam Puanı {}".format(toplam))
        if(toplam >= 85):
            print("AA aldı")
            nota = "AA"
        elif(toplam >= 70):
            print("BA aldı")
            nota = "BA"
        elif(toplam >= 60):
           print("BB aldı")
           nota = "BB"
        elif(toplam >= 50):
            print("CB aldı")
            nota = "CB"
        elif(toplam >= 40):
            print("CC aldı")
            nota = "CC"
        elif(toplam <= 39):
            print("FF aldınız")
            nota = "FF"
        print("{} vize notu {}, final notu {} donem ortalamasi ise {} notu {} \n".format(isim,vize,final,toplam,nota),file=txt)

        if(ogr >= 1):
            ogr -= 1
        if(ogr < 1):
            break
    print("\n{} Sınıfı bitti".format(sinif),file=txt)
    print("{} Sınıfı bitti\n ------{} Son------".format(sinif,sinif))
