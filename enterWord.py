import sqlite3
import time
import menu


def wordControl():
    print("3 adet kelime girişi yapınız")
    counter = 1

    while counter <= 3:  # 3 adet kelime girşi boyunca döner
        wordInput = input(f"{counter}. Kelime girişi ").upper()  # alınan değeri büyük harfler halinde wordInput'a atar
        if not wordInput.isalpha():  # wordInput harf hariç başka bir şey içeriyorsa geçeriz kabul eder
            print("--- Geçerli bir değer giriniz ---")
        elif len(wordInput) < 5:  # kural gereği kelime 5 harften küçük olamaz
            print("--- Kelime en az 5 harf olmalıdır ---")
        else:
            counter += 1  # sayaç görevi görür
            wordAdd(wordInput)  # alınan değeri database göndermek için 'wordAdd' fonksiyonuna gönderir

    print("Ana Menüye Yönlendiriliyorsunuz")
    time.sleep(2)  # 2sn bekleme yapar
    menu.user()


def wordAdd(dataSender):  # sqlite3 database ile bağlantı kurma VE veri eklemek için gereken fonksiyon
    connection = sqlite3.connect(
        "data.sqlite3")  # connect fonksiyonunu kullanarak "ogrencinonuz.sqlite3" adlı SQLite veritabanına
    # bir bağlantı oluşturmayı sağlar.
    cursor = connection.cursor()  # imleç, veritabanı üzerinde sorguları çalıştırmak ve sonuçları işlemek için
    # kullanılır
    cursor.execute('INSERT INTO T_KELIME (KELIME) VALUES (?)', (dataSender,))  # SQL komutu ile alınan kelimeyi
    # database kaydetmeye yarar
    users = cursor.fetchone()  # fetchone() metodu, sorgunun sonucundan sadece bir kaydı alır ve bu kaydı bir demet (
    # tuple) olarak döndürür.
    connection.commit()  # veri tabanında kalıcı olarak uygulanmasını sağlar
    connection.close()  # veri tabanı bağlantısını kapatır


if __name__ == "__main__":
    wordControl()