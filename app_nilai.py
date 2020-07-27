nilaiMhs = int(input("Masukan Nilai:"))

if 90 <= nilaiMhs <= 100:
    print("Nilai anda A")
elif 70 <= nilaiMhs <= 85:
    print("Nilai anda B")
elif 60 <= nilaiMhs <= 75:
    print("Nilai anda C")
elif 50 <= nilaiMhs <= 65:
    print("Nilai anda D, anda remedial")
elif 10 <= nilaiMhs <= 55:
    print("Nilai anda E, anda tidak lulus, silakan ikut ulang matkul")
else:
    print("Nilai tidak valid")