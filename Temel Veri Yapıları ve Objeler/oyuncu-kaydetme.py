print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun adi: ")
soyad = input("Oyuncunun soyadi: ")
takim = input("Oyuncunun takimi: ")

bilgiler = [ ad, soyad, takim]
print("bilgiler kaydediliyor...")
print("Oyuncu adı: {}\nOyuncu soyadı: {}\nOyuncu takımı: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))
print("bilgiler kaydedildi.")