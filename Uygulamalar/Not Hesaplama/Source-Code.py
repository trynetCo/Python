while(True):
    txt = open("Notlar.txt", "a")
    sinif = input("Sınıfı yazınız: ")
    ogr = int(input("Öğrenci Sayısını girin"))
    print("\n--------{}--------\n".format(sinif),file=txt)
    while ogr > 0:
        nota = "str"
        isim = input("İsminizi ve Soyadınızı girin: ")
        vize = int(input("Vize puanınızı girin: "))
        final = int(input("Final puanınızı girin: "))
        if(vize > 100 or final > 100):
            print("Vize Yada Final Notunu Yanlış Girdiniz Lütfen Bilgileri En Baştan Yazın")
            continue
        vizes = float(40 * vize / 100)
        finals = float(60 * final / 100)
        print("Vize puanın {} ".format(vizes))
        print("Final Puanın {} ".format(finals))
        toplam = float(finals + vizes)
        print("Toplam Puanın {}".format(toplam))
        if(toplam >= 85):
            print("AA aldınız")
            nota = "AA"
        elif(toplam >= 70):
            print("BA aldınız")
            nota = "BA"
        elif(toplam >= 60):
           print("BB aldınız")
           nota = "BB"
        elif(toplam >= 50):
            print("CB aldınız")
            nota = "CB"
        elif(toplam >= 40):
            print("CC aldınız")
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