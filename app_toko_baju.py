namaBarang = str(input("Masukan nama barang:"))
hargaBarang = int(input("Masukan harga barang:"))
jumlahBeli = int(input("Masukan jumlah beli:"))
bayar   = int(input("Jumlah uang yang di bayar:"))


total = hargaBarang * jumlahBeli - bayar
print(25*"=")
print(
    "Nama Barang: ",namaBarang,"\n",
    "Jumlah Beli: ",jumlahBeli,"\n",
    "Total kembali: ",total
)
