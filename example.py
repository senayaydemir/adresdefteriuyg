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