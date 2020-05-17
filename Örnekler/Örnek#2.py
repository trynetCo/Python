print("Sistemde kayıtlı gözükmüyorsun kayıt ol:") #Mesajımızı Yazdırıyoruz

a = input("Kullanıcı adını yaz:") #Kullanıcıdan Girdi(input) bekliyor
b = input("Şifreni yaz: ")
print("Başarıyla kayıt oldun \nŞimdi Giriş yap:") # "\n" bir alt satıra geçmek için kullanıyoruz
c = input("Kullanıcı Adın: ") #Kullanıcıdan daha önceki bilgiyi istiyoruz
d = input("Şifren: ")
if (a != c or b != d): # "if" burda koşul anlamı ekliyor "!=" ise eşit değilse anlamına geliyor
    #"or" ise bir bağlaç türkçedeki ve, veya bağlaçları ile aynı işmende kullanılıyor ama ingilizcesi bilmiyorsanız araştıra bilirsiniz.

    print("Yanlış giriş yaplıdı lütfen tekrar deneyin")# Koşul doğru ise bu alt satıra geçiyor
else: #"else" değilse anlamına gelir ve if doğru değilse bu kısıma geçer
    print("Başarıyla giriş yapıldı")