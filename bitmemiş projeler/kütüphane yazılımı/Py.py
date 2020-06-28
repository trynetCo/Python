from sys import exit
import datetime
import time
from sqlite3 import *
from time import strftime
import sys

zaman = time.strftime("%d/%m/%Y")

connet = connect("database.db")
cursor = connet.cursor()
txt = open("log.txt","a")

cursor.execute("CREATE TABLE IF NOT EXISTS kütüphane (kitap TEXT,kisi TEXT,sınıf TEXT,numara INT, zaman TEXT)")
connet.commit()


while True:
    while (True):
        try:
            sec = int(input("1-kitap ekle\n2-kitap ver\n3-kitap sil\n4-Arama\n5-Çık \nseç: "))
        except(ValueError):
            print("Lütfen seçeneğin yanındaki numarayı yazın")
        break


    if sec == 1:
        ismi = input("Kitapın ismini girin: ")
        alan = input("Alan Kişinin ismini girin: ")
        sn = input("Sınıfı girin: ")
        while True:
            try:
                numara = int(input("Kitapın numarasını girin: "))
            except(ValueError):
                print("Numarayı sayı olarak girin")
                continue
            break

        zamann = time.time()
        tarih = str(datetime.datetime.fromtimestamp(zamann).strftime('%d/%m/%Y'))
        cursor.execute("INSERT INTO kütüphane (kitap,kisi,sınıf,numara,zaman)VALUES (?,?,?,?,?)", (ismi, alan,sn , numara, tarih))
        connet.commit()


        print(f"{ismi} adlı ve {numara} numaralı kitap {alan} adlı ve {sn} sınıflı kişiye {zaman} tarihinde verildi",file=txt)
        print("-----------------------------------")


    if sec == 2:
        print(2)

    if sec == 3:
        s12k = input("Kitapın Numarasını Girin: ")
        cursor.execute("DELETE from kütüphane where numara = ?", (s12k,))
        connet.commit()
        print("\nSileme işlemi başarılı\n")

    if sec == 4:
        try:
            selecta = int(input("1-kitap ismi ile arama yap\n2-Alan kişinin ismiyle\n3-Sınıfıla\n4-Numara\n5-Tarih\nseç: "))
        except(ValueError):
            print("Lütfen seçeneğin yanındaki numarayı yazın")
        seca = str("str")
        if selecta == 1:
            seca = str("kitap")
        if selecta == 2:
            seca = str("kisi")
        if selecta == 3:
            seca = str("sınıf")
        if selecta == 4:
            seca = str("numara")
        if selecta == 4:
            seca = str("zaman")

        kitap = input("arama yapmak istediğin şeyi yaz ama dikkatli ol büyük ve küçük harf uyumu var ve herşeyi tam yaz: ")

        cursor.execute("SELECT * FROM kütüphane WHERE {}=?".format(seca), (kitap,))
        tr = cursor.fetchall()
        for i in tr:
            print("Kitap ismi = ", i[0])
            print("alan = ", i[1])
            print("sınıf = ", i[2])
            print("numara = ", i[3], "\n")
            print("----------------------\n")




    if sec == 5:
        exit("uygulama kapandı")
connet.close()