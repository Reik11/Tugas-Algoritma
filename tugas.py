# Inisialisasi dictionary untuk menyimpan stok barang
stock = {}

# Input jumlah barang
jumlah_barang = int(input("Masukkan jumlah barang: "))

# Input stok barang
for i in range(jumlah_barang):
    nama_item = input("Masukkan nama barang ke-%d: " % (i+1))
    item_stock = int(input("Masukkan stok barang untuk %s: " % nama_item))
    stock[nama_item] = item_stock

# Output stok barang
print("\nStok Barang:")
for item, quantity in stock.items():
    print("%s: %d" % (item, quantity))
