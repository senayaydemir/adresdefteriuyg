adres_defteri =[]
def secenekler():
    print("\nAdres Defteri Uygulaması")
    print("1-Kişi Ekle")
    print("2-Kişi Sil")
    print("3-Kişileri Göster")
    print("4-Çıkış")

def kisi_ekle():
        isim=input("İsim:")
        telefon=input("Telefon:")
        email=input("Email:")
        adres_defteri.append({"İsim":isim,"Telefon":telefon,"Email":email})
        print(f"{isim} kişisi Adres Defterine eklendi")



def kisi_sil():
        kisi_no=int(input("Silmek istediğiniz kişinin numarasını giriniz:"))
        if 0<=kisi_no <len(adres_defteri):
         silinen_kisi=adres_defteri.pop(kisi_no)
         print(f"{silinen_kisi['isim']}Adres defterindeen silindi")

def kisileri_goster():
       if not adres_defteri: 
          print("Adres defteri boş")
       else:
          print("\nAdres Defteri")
          for i,kisi in enumerate(adres_defteri,1):
             print(f"{i}. İsim:{kisi['isim']},Telefon:{kisi['Telefon']},Email:{kisi['isim']}")
while True:
    secenekler()
    secim=int(input("Lütfen yapmak istediğiniz işlemi seçiniz:"))

    if secim == 1:
      kisi_ekle()
    elif secim ==2:
      kisi_sil()
    elif secim ==3:
      kisileri_goster()
    elif secim ==4:
      print("Programdan Çıkılıyor...")
      break
    
    else:
      print("Geçersiz seçim.Lütfen tekrar deneyiniz...")      