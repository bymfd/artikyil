onceki = 0.0
aralik_toplam = 0.0
say = 0


def artik_yil_mi(yil):
    global say, aralik_toplam, onceki, simdiki_fark, ortalama
    if yil % 4 == 0 and (yil % 100 != 0 or yil % 400 == 0):
        aralik_toplam += abs(onceki - yil)
        onceki = yil
        say += 1
        return True

    else:
        return False


for yili in range(1, 2100):
    if artik_yil_mi(yili):
        print(yili)

print("Yıl sayısı: " + str(say) + " ortalama artık yıl aralığı:" + str(round(aralik_toplam / say, 2)) + " ")
