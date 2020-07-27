benar = 'ikan'
tebak = ''
# pemain hanya bisa menabak sampai 3 kali
jumlah_tebakan = 0
batas_tebakan = 3
keluar = False

print("Hewan apa yang hidup di air?")
# while akan menjalankan terus menerus jika kodisinya True
while tebak != benar and not(keluar):
    if jumlah_tebakan < batas_tebakan:
        tebak = input("input jawaban: ")
        jumlah_tebakan +=1
    else:
        keluar = True

if keluar:
    print("anda kalah")
else:
    print("Tebakan anda benar!!")