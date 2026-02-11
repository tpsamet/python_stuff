import random

print("tas kagıt makas oyununa hoşgeldiniz")
sec = print("lütfen secim yapınız\n1. tas\n2. kagıt\n3. makas")

secimler = ["tas", "kagit", "makas"]

while True:
    oyuncu_secimi = input("seciminiz: ").lower()
    if oyuncu_secimi not in secimler:
        print("geçersiz secim, lütfen tekrar deneyiniz")
        continue

    bilgisayar_secimi = random.choice(secimler)
    print(f"bilgisayarın secimi: {bilgisayar_secimi}")
    print(f"oyuncunun secimi: {oyuncu_secimi}")

    kazanma_durumu = {
        "tas": "makas",
        "kagit": "tas",
        "makas": "kagit"
    }

    if oyuncu_secimi == bilgisayar_secimi:
        print("berabere!")
    elif kazanma_durumu[oyuncu_secimi] == bilgisayar_secimi:
        print("tebrikler, kazandınız!")
    else:
        print("üzgünüm, kaybettiniz!")
