import random


class TasKagitMakas():

    def __init__(self, tur):
        self.tur = tur

    def Oyun(self, tur):
        bilgisayar = []
        oyuncu = []
        for i in range(int(tur)):
            deger = random.randrange(1, 4)  # 1,2,3
            if deger == 1:
                deger = "Taş"
            elif deger == 2:
                deger = "Kağıt"
            elif deger == 3:
                deger = "Makas"
            dizi = ["tas", "makas", "kagit", "Q"]
            while True:
                secim = input("""
                    Lütfen seçiminizi yazınız:
                    Taş oynamak için = tas
                    Kağıt oynamak icin = kagit
                    Makas oynamak için = makas 

                    Oyundan çıkmak Q yazınız: """)
                if secim in dizi:
                    if secim == "Q":
                        print("Oyundan çıkış yapılıyor...")
                        input("")
                        quit()
                    else:
                        break  # while döngüsünü kırıp işleyişe devam ediyor
                else:
                    print("Hatalı seçim yazdınız, lütfen tekrar deneyiniz.")
            if secim == "tas" and deger == "Taş":
                print("Bu turda berabere kaldınız. Bilgisayar da taş oynamıştı. Kimse puan kazanamadı.")
            elif secim == "tas" and deger == "Kağıt":
                print("Bu turu kaybettiniz, bilgisayar kağıt oynamıştı.")
                bilgisayar.append(1)
            elif secim == "tas" and deger == "Makas":
                print("Bu turu kazandınız, bilgisayar makas oynamıştı.")
                oyuncu.append(1)
            elif secim == "kagit" and deger == "Taş":
                print("Bu turu kazandınız, bilgisayar taş oynamıştı.")
                oyuncu.append(1)
            elif secim == "kagit" and deger == "Kağıt":
                print("Bu turda berabere kaldınız. Bilgisayar da kağıt oynamıştı. Kimse puan kazanamadı.")
            elif secim == "kagit" and deger == 3:
                print("Bu turu kaybettiniz, bilgisayar makas oynamıştı.")
                bilgisayar.append(1)
            elif secim == "makas" and deger == "Taş":
                print("Bu turu kaybettiniz, bilgisayar taş oynamıştı.")
                bilgisayar.append(1)
            elif secim == "makas" and deger == "Kağıt":
                print("Bu turu kazandınız, bilgisayar kağıt oynamıştı.")
                oyuncu.append(1)
            elif secim == "makas" and deger == 3:
                print("Bu turda berabere kaldınız. Bilgisayar da makas oynamıştı. Kimse puan kazanamadı.")
            print("""
                    < Güncel Skor >
                    Bilgisayar: {}
                    Oyuncu: {}           
                  """.format(sum(bilgisayar), sum(oyuncu)))
        print("Oyun bitti!")
        if sum(bilgisayar) > sum(oyuncu):
            print("Toplam {} tur oynadınız. Bilgisayar kazandı!".format(tur))
        elif sum(bilgisayar) == sum(oyuncu):
            print("Toplam {} tur oynadınız. Sonuç berabere!".format(tur))

        else:
            print("Toplam {} tur oynadınız. Tebrikler! Siz kazandınız.".format(tur))
        print("""
                            < Son Skor >
                            Bilgisayar: {}
                            Oyuncu: {}           
                          """.format(sum(bilgisayar), sum(oyuncu)))
        input("")


print("Taş-Kağıt-Makas oyununa hoşgeldiniz!")
while True:
    tur = input(""" Kaç tur oynamak istiyorsunuz? (Belirlediğiniz tur sayısına kadar en fazla puanı alan kazanır)""")
    if tur.isdigit() and int(tur) > 0:
        break
    else:
        print("Hatalı tercih yaptınız, lütfen tekrar deneyiniz.")
o1 = TasKagitMakas(tur)
o1.Oyun(tur)

input("")