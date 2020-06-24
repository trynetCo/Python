from urllib.request import urlretrieve
txt = open("log.txt","a")
png = input("resim formatını belirleyin ÖR png,jpg : ")
while True:
    Rurl = input("Resim url'sini yapıştır: ")
    ismi = input("Resmin ismi ne olsun: " )
    urlretrieve(Rurl,ismi + "." + str(png))
    print("{} adlı resim indirildi".format(ismi))
    print("{} adlı resim şu url den indirildi {}".format(ismi,Rurl),file=txt)
    print("---------------------------")