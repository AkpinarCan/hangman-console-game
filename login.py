import sqlite3
import time
import menu


def userInfo():  # kullanıcıdan değer alan ve kontrol eden foksiyon
    while True:
        Id = input("kullanıcı adınızı giriniz: ")  # kullanıcıdan id alır
        password = input("Şifrenizi giriniz: ")  # kullanıcıdan password alır

        if Id == "" or password == "":  # id veya password boş ise kullanıcıdan tekrar değer alır
            print("--- Geçerli bir değer giriniz ---")
        else:
            usersControl(Id, password)  # id ve password değeri geçerli ise kontrol için usersControl'e yollanır
            break


def usersControl(Id, password):  # sqlite3 database ile bağlantı kurması için gerek fonksiyon
    connection = sqlite3.connect("data.sqlite3")  # connect fonksiyonunu kullanarak "ogrencinonuz.sqlite3"
    # adlı SQLite veritabanına bir bağlantı oluşturmayı sağlar.
    cursor = connection.cursor()  # imleç, veritabanı üzerinde sorguları çalıştırmak ve sonuçları işlemek için
    # kullanılır
    cursor.execute("SELECT * FROM T_USERS WHERE kullanici=? AND sifre=?", (Id, password))  # database üzerinde veri
    # çekmek için kullanılan komut
    users = cursor.fetchone()  # fetchone() metodu, sorgunun sonucundan sadece bir kaydı alır ve bu kaydı bir demet (
    # tuple) olarak döndürür.
    connection.close()  # veri tabanı bağlantısını kapatır

    if users is not None:
        print("Başarılı giriş!")
        print("Merhaba " + users[-1])
        time.sleep(1)
        menu.user()
    else:
        print("--- Kullanıcı adı veya şifre hatalı. Tekrar deneyin. ---")
        userInfo()


if __name__ == "__main__":
    userInfo()