import time
import enterWord
import game


def user():
    while True:
        print("Adam Asmaca Oyununa Hoş geldiniz")
        time.sleep(1)  # 2sn bekletme
        # menü bar
        print("- 1. Kelime Girşi")
        print("- 2. Oyun Oyna")
        print("- 3. Programı Sonlandır")
        choose = input("Seçiminizi Yapınız: ")

        if choose == "1":
            print("Kelime girişi için yönlendiriliyor...")
            enterWord.wordControl()
            break
        elif choose == "2":
            print("Oyun'a yönlendiriliyor...")
            game.datacheck(9)
            break
        elif choose == "3":
            print("Çıkış yapılıyor")
            break
        else:
            print("--- Geçersiz değer tekrar deneyiniz---")


if __name__ == "__main__":
    user()