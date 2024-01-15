import sqlite3
import random
from collections import Counter
import menu

known = []
erChar = []


def charNum(array):
    charNumber = Counter(array)  # Dizideki harf sayısını hesapla
    return charNumber  # geri döndürülen değer


def datacheck(hak):
    conn = sqlite3.connect('data.sqlite3')  # SQLite3 veritabanına bağlanma
    cursor = conn.cursor()  # imleç oluşturma

    cursor.execute('SELECT KELIME FROM T_KELIME ORDER BY RANDOM() LIMIT 1')  # random kelime seçiliyor db'den
    withdrawnWord = cursor.fetchone()  # çekilen kelimeyi değişkene atandı

    # Çekilen kelime
    if withdrawnWord:
        word = withdrawnWord[0]  # fetchone() bir tuple döndüğü için, kelimeyi almak için indeks 0 kullanılır
        #  print("Çekilen Kelime:", word)  # !!! bilgi için program yapılırken !!!
        game(withdrawnWord, hak)
    else:
        print("Veritabanında kelime bulunamadı. Lütfen kelime girişi yapınız")

    conn.close()  # Veritabanı bağlantısını kapatma


def game(withdrawnWord,
         hak):  # parametre olarak veri tabanından random seçilen kelime ve önceden tanımlı hak sayısını alır
    joker = 1  # joker hakkının tanımlaması yapıldı
    print("- Oyun Başladı Kolay Gelsin :) -")
    counts = withdrawnWord[
        0]  # veri tabanından seçilen kelime list öğesi olarak geldiği için withdrawnWord[0] yaparak kelimeye
    # ulaşıyoruz ki kelimedeki harflere rahat ulaşabilmek için
    _line = "_" * len(counts)  # kelimedeki harf sayısı kadar '_' eklemek için kelime uzunluğunu '_' ile çarpıldı
    # _line tanımlandı

    print(
        "(i)Joker hakkı için harf yerine joker yazınız")  # kullanıcı bilgilendirmesi yapıldı joker hakkının nasıl
    # kullanılacağı ile ilgili

    conclusion(hak)  # hak sayısı bilgisi conclusion(sonuç) içinde yollanır çünkü adam asmaca görseli almak için

    print(_line + f"    {len(counts)} karakter uzunluğunda")  # seçilen kelimenin uzunluğunda '_' ve  kullanıcıya
    # sayı(karakter sayısı)olarak bilgi olarak verir

    while hak > 1 and set(withdrawnWord[0]) != set(known):  # hak 1'den büyük ve kelime tahmin edilmedisye çalışır

        ask = input("Harf tahmini: ").upper()  # ask(sormak) değişkenine kullanıcıdan alınan harf değişkeni büyük
        # harf olarak atanır
        print("""




            """)  # oyun arasında console karışık olmaması için önceki kodları üst satıra atıp daha temiz bir çıktı için
        if ask == "JOKER" and joker == 1:  # kullanıcının joker kullanması halinde çalışacak şart bloğu
            joker -= 1  # joker kullanılınca joker hakkı 1 düşer
            randomJoker = random.choice(list(set(counts) - set(known)))  # random.choice(random seç) içinde deki list
            # işlem yapılan 'counts' ve 'known' küme olduğundan, list sonucu tekrar list haline getirir ayrıca set
            # ise benzersiz(burada aynı harften bir kere olması için kullanılmıştır) elemanların bir koleksiyonunu
            # tutan sırasız bir veri tipidir ve sonda randomJoker'e atanır print(randomJoker)
            known.append(randomJoker)  # joker harf ise bilinen list öğesine eklenir
            conclusion(hak)  # adam asmaca resmi tekrar görünmesi için
            openChar(counts, randomJoker)  # joker harfin '_' yerinde görünmesi için openChar'a gönerilir
            print("\nJoker harf " + randomJoker)  # joker harf ekrana yazdırılır
        elif ask.isalpha() and len(ask) == 1:  # girilen değerin (ask) sadece alfabetik karakterden oluşmasına bakar
            # ve 1 karakter uzunluğunda olmasını yani harf olmasını denetler
            if ask in known:  # girilen değerin önceden girilmiş olmasını denetler
                conclusion(hak)  # adam asmaca resmi tekrar görünmesi için
                openChar(counts, ask)
                print("\n(i)Bu harfi daha önce tahmin ettiniz. Lütfen başka bir harf deneyin.")
                print("yanlış tahminedilen harflar: " + str(erChar))
            elif ask in counts:  # girilen değerin kelime içinde olmasını denetler
                known.append(ask)  # bilinenlere(known) ekler tekar girile durumu olduğundan bilgi çıktısı vermek ve
                # kontoller için
                print(f"{ask} harfi var. böyle devam...")
                conclusion(hak)  # adam asmaca resmi tekrar görünmesi için
                openChar(counts, ask)
                print(f"    {len(counts)} karakter uzunluğunda")
                print("yanlış tahminedilen harflar: " + str(erChar))
            else:

                print("Maalesef Bu Harf Yok!!!")
                hak -= 1  # hak 1 düşürülür hem görsel ilerlemesi hemde hakkın bitmesi durumu için
                conclusion(hak)  # adam asmaca resmi tekrar görünmesi için
                openChar(counts, ask)
                print(f"    {len(counts)} karakter uzunluğunda")
                erChar.append(ask)  # tahmin edilen ve yanlış olan harfleri birdaha tahmin edilmemesi bilgisi için
                # 'erChar' eklenir çıktı için tutulur
                for char, numb in charNum(erChar).items():  # karakter ve sayı, yanlış tahmin edilen harfler
                    # listesinde(erChar) içinde döner kaç kere ve hangi harf olduğu bilgisi için
                    print(f"{char}: {numb} kez denedin olmadı :)")
                    # print("yanlış tahminedilen harflar: " + str(erChar))
        elif ask == "JOKER" and joker != 1:  # joker hakkı bitmiş olan kullanıcı için şart bloğu
            print("Joker Hakkınız Yok!")  # bilgilendirme
        else:
            print("Lütfen Harf Giriniz!")  # harf harici değer girişi yapılması halinde
    if set(counts) == set(known):  # (list benzersiz harf için) kelimenin ve tahmin edilen harflerin aynı olamsı
        # halinde kelime bulunmuş sayılır
        print(f"TEBRİKLER 🥳 kelimeyi doğru tahmin ettiniz kelime ----> {counts} ")  # DOĞRU tahmminler sonucu
        # bilgilendirme
    else:
        #  print("yanlış tahminedilen harflar: " + str(erChar))
        print("🏳️ KAZANAMADINIZ 🏳️")  # hak sayısının bitmesi durumudur KAYBETTİNİZ bilgisidir

    while hak <= 1 or set(withdrawnWord[0]) == set(known):
        known.clear()
        erChar.clear()
        rMenu = input("Menüye dönmek için 1'e\nBitirmek için Q giriniz: ").upper()

        if rMenu == "1":
            print("Menu'ye gidiliyor...")
            menu.user()
            break  # Burada döngüden çıkarak mevcut döngüyü sonlandırabilirsiniz
        elif rMenu == "Q":
            print("Çıkış yapılıyor...")
            break
        else:
            print("- Yanlış tuşlama tekrar deneyin -")


def openChar(word, inchar):  # kelime ve girilen harf tahminini parametre alarak işlem yapar amacı '_' şeklinde olan
    # gizli harflerin bilinme veya joker kullanılması halinde açılma durumunu yapar
    for chars in word:  # chars ile word içinde dönenen for döngüsü
        if chars in inchar:  # chars girilen harf içinde olma durumunda harfi açar
            print(chars, end=' ')
        elif chars in known:  # chars bilinen harfler içinde ise harfi açar
            print(chars, end=' ')
        else:
            print('_', end=' ')  # eğer bunlar yoksa harf bilinememiştir yani '_' olarak yazdırılır


"""def controlW(word, known, inchar):
    timer = 1
    if len(word[0]) == len(known):        
        for known in word:
            if known == word:
                timer += 1
        if timer == len(known):
            print("Kazandınız!!!")
        else:
            openChar(inchar)
"""


def conclusion(hak):  # adam asmaca resmi görünmesi için gerekli ASCII düzen list şeklinde yazılır
    deadLevel = [
        """
                  Let's Go  
                |=========|||
                |          
                |
                |                        
                |
                |
                """,
        """
                     X  
                |=========|||
                |          |
                |
                |                        
                |
                |
                """,
        """
                     XX  
                |=========|||
                |          |
                |          O
                |             
                | 
                |
                """,
        """
                    XXX  
                |=========|||
                |          |
                |          O
                |          |             
                | 
                |
                """,
        """
                    XXXX  
                |=========|||
                |          |
                |          O
                |          |             
                |          |
                |
                """,
        """
                   XXXXX  
                |=========|||
                |          |
                |          O
                |         /|             
                |          | 
                |
                """,
        """
                   XXXXXX 
                |=========|||
                |          |
                |          O
                |         /|\              
                |          | 
                |
                """,
        """
                  XXXXXXX
                |=========|||
                |          |
                |          O
                |         /|\              
                |          | 
                |         / 
                """,
        """
                  GAME OVER
                  XXXXXXXX
                |=========|||
                |          |
                |          O
                |         /|\     ...DEAD...         
                |          | 
                |         / \\

                """
    ]
    # 9 resim olma sebebi 1. resmin karşılama resmi olmasıdır bu yüzden hak 1 oldupunda 0 mış gibi işle görür ve
    # hakkınız kalmamıştır diye çıktı verir
    print(deadLevel[9 - hak])


if __name__ == "__main__":
    datacheck(9)