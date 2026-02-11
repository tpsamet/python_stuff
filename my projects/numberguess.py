import random

def rastgele_sayi_oyunu():
    print("kac ile kac arasında sayı tutayım?")

    while True:
        try:
            alt = int(input("alt sınır: "))
            ust = int(input("üst sınır: "))

            if alt >= ust:
                print("alt sınır üst sınırdan kücük olmalı!")
            else:
                break
        except ValueError:
            print("iyi ki sayı gir dedim.")

    sayi = random.randint(alt, ust)

    print("\nhangi modda oynarsın?:")
    print("1 - kolay (10 hak)")
    print("2 - normal (7 hak)")
    print("3 - zor (5 hak)")

    while True:
        mod = input("secimin: ")

        if mod == "1":
            hak = 10
            break
        elif mod == "2":
            hak = 7
            break
        elif mod == "3":
            hak = 5
            break
        else:
            print(f"{mod} nası mod la")

    print(f"\n{alt} ile {ust} arasında bi sayı tuttum. {hak} hakkın var!")

    while hak > 0:
        print(f"kalan hak: {hak}")
        cevap = input("tahminin ne?: ")

        try:
            tahmin = int(cevap)

            if tahmin < alt or tahmin > ust:
                print(f"{alt}-{ust} aralıgında dedim!")
                continue

            if tahmin > sayi:
                print("tuttugum sayı daha kücük!")
            elif tahmin < sayi:
                print("tuttugum sayı daha büyük!")
            else:
                print("dogru bildin!!")
                return

            hak -= 1

        except ValueError:
            print("sayı gir dedim, roman yazma.")

    print(f"\nbaska hakkın kalmadı...")
    print(f"tuttuğum sayı: {sayi}")

rastgele_sayi_oyunu()
