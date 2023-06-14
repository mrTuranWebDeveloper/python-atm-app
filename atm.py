
# ATM

# Yapılan İşlemler : Kullanıcı ve şifre istenilecek. Eğer 3 kere yanlış girilirse döngüyü durduracak.
# Eğer doğru girilirse işlemler devam edecek.
# Para çekme - para yatırma - bakiye sorgulama - çıkış, eğer çıkış yaparsa tekrar kullanıcı adı ve şifre isteyecek. 

def menu():
    print("""İşlemler :   
    1 - Para Çekme
    2 - Para Yatırma
    3 - Para Gönderme
    4 - Borç Yatırma
    5 - Şifre Değiştir
    6 - Bakiye Sorgulama
    7 - Çıkış
    """
    ) 

def atm():
    kullanici = "neos"
    sifrem = "1234"
    bakiye = 5000
    borc = 3000
    hak = 3
    while True:
        kullanici_adi = input("Kullanıcı adınızı giriniz = ")
        sifre = input("Şifreyi giriniz = ")
        hak -= 1
        if kullanici_adi == kullanici and sifre == sifrem:
            while True:
                menu()
                islem = int(input("Yapmak istediğiniz işlemi giriniz = "))
                if islem == 1:
                    while True:
                        cek = int(input("Çekmek istediğiniz miktarı giriniz = "))
                        if cek < bakiye:
                            bakiye -= cek
                            print(f"Çekilen miktar = {cek}TL ---- Kalan bakiye = {bakiye}TL")
                            break
                        else:
                            print("Yetersiz bakiye...")
                elif islem == 2:
                    yatir = int(input("Yatırmak istediğiniz miktarı giriniz =  "))
                    bakiye += yatir
                    print(f"""
    Yatırılan Miktar = {yatir}TL
    *************
    Güncel Bakiye = {bakiye}TL""")
                elif islem == 3:
                    while True:
                        gonder = int(input("Göndermek istediğiniz miktarı giriniz = "))
                        if gonder < bakiye:
                            hesapNo = input("Hesap numarasını giriniz = ")
                            print(f"{hesapNo} hesabına {gonder}TL miktarında para gönderme işlemini onaylıyormusunuz ? \nE/H")
                            while True:
                                onay = input()
                                if onay == 'E':
                                    print(f"{gonder}TL miktarında para {hesapNo} hesabına gönderildi.")
                                    bakiye -= gonder
                                    break
                                elif onay == 'H':
                                    print("İşlem iptal ediliyor")
                                    break
                                else:
                                    print("Geçersiz değer. E/H")
                            break
                        else:
                            print("Yetersiz bakiye")
                elif islem == 4:
                    print("Mevcat borcunuz = ", borc, "TL")
                    if borc:
                        while True:
                            yatir = int(input("Yatırmak istediğiniz borç miktarını giriniz = "))
                            if yatir <= bakiye:
                                if yatir <= borc:
                                    bakiye -= yatir
                                    borc -= yatir
                                    print(f"Yatırılan borç miktarı = {yatir}TL ----- Kalan Borç = {borc}TL")
                                    break
                                else:
                                    print("Borcunuzdan fazlasını yatıramazsınız.")
                            else:
                                print("Yetersiz Bakiye")
                    else:
                        print("Borcunuz bulunmamaktadır.")
                elif islem == 5:
                    yeniHak = 3
                    while True:
                        eski = input("Mevcut şifrenizi giriniz = ")
                        yeniHak -= 3
                        if eski == sifrem:
                            while True:
                                yeni1 = input("Yeni şifrenizi giriniz = ")
                                yeni2 = input("Şifreyi onaylayın = ")
                                if yeni1 == yeni2:
                                    if len(yeni1) < 6:
                                        print("Şifreniz en az 6 karakter olmalıdır")
                                    elif yeni1[0] != yeni1[0].upper():
                                        print("Şifreniz büyük harf ile başlamalıdır")
                                    elif '.' or '!' or '?' or '-' or '*' in yeni1:
                                        print("Şifreniz özel karakter barındırmamalıdır")
                                    elif eski.lower() in yeni1.lower():
                                        print("Yeni şifre eski şifreye benzememelidir")
                                    elif kullanici.lower() in yeni1.lower():
                                        print("Şifreniz kullanıcı adına benzer olmamalıdır")
                                    else:
                                        sifrem = yeni1
                                        print("Şifreniz güncellendi...")
                                        break
                        elif yeniHak == 0:
                            print("Hakkınız bitti.Program kapanıyor...")
                            break
                        else:
                            print("Hatalı şifre")
                    break    
                elif islem == 6:
                    print("Güncel bakiyeniz = ", bakiye, "TL")
                elif islem == 7:
                    print("Çıkış yapılıyor.")
                    break
            break
        elif hak == 0:
            print("Haklarınız bitti. Program kapanıyor.")
            break
        else:
            print("Kullanıcı adı veya şifre yanlış") 

atm()


