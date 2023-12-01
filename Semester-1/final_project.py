# import pandas as pd
# #KOPI JANJI KITA
# class Product:
#     nama = ''
#     harga = ''
#     def __init__(self, nama, harga):
#         self.nama = nama
#         self.harga = harga

# class Customer:
#     nama = ''
#     pesanan = ''
#     totalBiaya = 0

# class Makanan(Product):
#     kategori = ''
#     def __init__(self, nama, harga, kategori):
#         super().__init__(nama, harga)
#         self.kategori = kategori

# class Minuman(Product):
#     jenis = ''
#     kondisi = ''
#     def __init__(self, nama, harga, jenis):
#         super().__init__(nama, harga)
#         self.jenis = jenis

#     def setItSelf(self, nama, harga, jenis):
#         super().__init__(nama, harga)
#         self.jenis = jenis
#         self.kondisi = ''

# #LIST MENU
# #MINUMAN
# #COFFEE
# americano = Minuman('Americano       ', 18000, 'Coffee')
# latte = Minuman('Latte           ', 26000, 'Coffee')
# machiato = Minuman('Caramel Machiato', 29000, 'Coffee')
# #NON-COFFE
# susu = Minuman('Susu            ', 15000, 'Non-Coffee')
# teh = Minuman('Teh             ', 14000, 'Non-Coffee')

# #MAKANAN
# #BAKERY
# toast = Makanan('Kita Toast      ', 16000, 'Bakery')
# croissant = Makanan('Croissant       ', 18000, 'Bakery')

# #DESSERT
# gelato = Makanan('Gelato          ', 12000, 'Dessert')
# kue = Makanan('Kue Kita        ', 13000, 'Dessert')


# def pilihanMenu(no):
#     if no == 1:
#         return americano
#     elif no == 2:
#         return latte
#     elif no == 3:
#         return machiato
#     elif no == 4:
#         return susu
#     elif no == 5:
#         return teh
#     elif no == 6:
#         return toast
#     elif no == 7:
#         return croissant
#     elif no == 8:
#         return gelato
#     elif no == 9:
#         return kue

# def resetMenu():
#     global americano, latte, machiato, susu, teh
#     #MINUMAN
#     #COFFEE
#     # americano.setItSelf('Americano       ', 18000, 'Coffee')
#     # latte.setItSelf('Latte           ', 26000, 'Coffee')
#     # machiato.setItSelf('Caramel Machiato', 29000, 'Coffee')
#     # #NON-COFFE
#     # susu.setItSelf('Susu            ', 15000, 'Non-Coffee')
#     # teh.setItSelf('Teh             ', 14000, 'Non-Coffee')
#     #COFFEE
#     americano = Minuman('Americano       ', 18000, 'Coffee')
#     latte = Minuman('Latte           ', 26000, 'Coffee')
#     machiato = Minuman('Caramel Machiato', 29000, 'Coffee')
#     #NON-COFFE
#     susu = Minuman('Susu            ', 15000, 'Non-Coffee')
#     teh = Minuman('Teh             ', 14000, 'Non-Coffee')

# def resetVariable():
#     global nomorPesanan, statusInput, totalHarga, pesanan, totalPesanan, nomorPilihan, nomorPesanLagi, produk
#     nomorPesanan = 0
#     statusInput = True

#     totalHarga = 0
#     totalPesanan = 0

#     nomorPilihan = 0
#     nomorPesanLagi = 0
#     produk = Product('', '')

# #VARIABLE UTAMA
# keranjangBelanja = pd.DataFrame(columns=['Nama', 'Harga', 'Kategori', 'Jenis', 'Kondisi'])
# customer = Customer()

# nomorPesanan = 0
# statusInput = True

# mainInput = True

# totalHarga = 0
# pesanan = ''
# totalPesanan = 0

# nomorPilihan = 0
# nomorPesanLagi = 0

# nominalPembayaran = 0
# nilaiAkhir = 0


# line = '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-='
# title = """=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
#                                 KOPI JANJI KITA
#                      ----- Our Promise is for all of Us ------
#     SELAMAT DATANG 
#     Berikut Menu yang KITA miliki :
#     ----------------------------------     -----------------------------
#     | Coffee :            | Harga :  |     | Non-Coffee :   | Harga :  |
#     ----------------------------------     -----------------------------
#     | 1.Americano         | 18k      |     | 4.Susu         | 15k      |
#     | 2.Latte             | 26k      |     | 5.Teh          | 14k      |
#     | 3.Caramel Machiato  | 29k      |     -----------------------------
#     ----------------------------------
#     *note: all drinks available in ICE/HOT

#     ------------------------------         -----------------------------
#     | Bakery :      | Harga :    |         | Desert :      | Harga :   |
#     ------------------------------         -----------------------------
#     | 6.Kita Toast  | 16k        |         | 8.Gelato      | 12k       |
#     | 7.Croissant   | 18K        |         | 9.Kue         | 13k       |
#     ------------------------------         -----------------------------
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# """
# footer = """
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
#                                Terima Kasih
#                              Selamat Menikmati :)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# """

# offer = "Silahkan Masukkan Pesanan anda (masukan nomor urutan angka nya saja) : "
# reoffering = """Ingin Menambahkan Pesanan lagi?
# 1.Ya
# 2.No
# : """
# pilihanSuhu = """Ingin Panas atau Dingin?
# 1. Hot
# 2. Ice
# : """

# print(title)

# while mainInput:

#     while statusInput:
#         try:
#             nomorPesanan = int(input(offer))
#         except:
#             print("Tolong Masukan Input sesuai format yg telah di berikan!")
#             continue
#         if type(nomorPesanan) is int:
#             if nomorPesanan > 9 or nomorPesanan < 1: 
#                 print('Nomor pesanan tidak boleh lebih dari 9 atau di bawah 1')
#             else:
#                 break

#     produk = pilihanMenu(nomorPesanan)
#     if nomorPesanan < 6:
#         while statusInput:
#             try:
#                 nomorPilihan = int(input(pilihanSuhu))
#             except:
#                 print("Tolong Masukan Input sesuai format yg telah di berikan!")
#                 continue
#             if type(nomorPilihan) is int:
#                 if nomorPilihan > 2 or nomorPilihan < 1:
#                     print('Nomor pilihan tidak boleh lebih dari 2 atau di bawah 1')
#                 else:
#                     break
#         if nomorPilihan == 1:
#             produk.kondisi = 'HOT'
#         elif nomorPilihan == 2:
#             produk.kondisi = 'ICE'

#     keranjangBelanja = keranjangBelanja.append({'Nama': produk.nama, 'Harga': produk.harga, 'Kategori': produk.kategori, 'Jenis': produk.jenis, 'Kondisi': produk.kondisi}, ignore_index=True)

#     while statusInput:
#         try:
#             nomorPesanLagi = int(input(reoffering))
#         except:
#             print("Tolong Masukan Input sesuai format yg telah di berikan!")
#             continue
#         if type(nomorPesanLagi) is int:
#             if nomorPesanLagi > 2 or nomorPesanLagi < 1:
#                 print('Nomor pilihan tidak boleh lebih dari 2 atau di bawah 1')
#             else:
#                 break
#     if nomorPesanLagi == 1:
#         resetMenu()
#         resetVariable()
#         continue
#     elif nomorPesanLagi == 2:
#         for index, row in keranjangBelanja.iterrows():
#             hargaPembelian = 0

#             nota = keranjangBelanja.loc[keranjangBelanja['Nama'] == row['Nama']]

#             hargaPembelian = row['Harga'] * nota.shape[0]
            
#             totalHarga = totalHarga + row['Harga']
#             if row['Jenis'] == 'Coffee':
#                 if pesanan.find(row['Nama']+"   "+row['Kondisi']+"    "+str(nota.shape[0])) < 0:
#                     pesanan = pesanan + "{}   {}    {} Rp.{},00 \n"
#                     pesanan = pesanan.format(row['Nama'], row['Kondisi'], nota.shape[0], hargaPembelian)
#             else:
#                 if pesanan.find(row['Nama']) < 0:
#                     pesanan = pesanan + "{}          {} Rp.{},00 \n"
#                     pesanan = pesanan.format(row['Nama'], nota.shape[0], hargaPembelian)

#         totalPesanan = keranjangBelanja.shape[0]

#         print(line)
#         customer.nama = input("Pesanan atas nama Ka siapa? ")
#         print('\nPesanan Atas Nama : Ka ' + customer.nama)
#         print('Total Pesanan Anda :')
#         print(pesanan)
#         print(line)
#         txtTotalHarga = "Total Harga :               Rp.{},00"
#         print(txtTotalHarga.format(totalHarga))
#         print(line)
#         while statusInput:
#             try:
#                 nominalPembayaran = int(input("Silahkan Masukkan Nominal Pembayaran : "))
#             except:
#                 print("Tolong Masukan Input sesuai format yg telah di berikan!")
#                 continue
#             if type(nominalPembayaran) is int:
#                 if nominalPembayaran < totalHarga: 
#                     print('Nominal Pembayaran Tidak dapat kurang atau lebih kecil dari total\nharga pesanan.')
#                 else:
#                     break
#         print(line)
#         totalHargaPembayaran = "Nominal Pembayaran yang anda masukkan :               Rp.{},00\nTotal yang harus di bayarkan          :               Rp.{},00"
#         print(totalHargaPembayaran.format(nominalPembayaran, totalHarga))
#         nilaiAkhir = nominalPembayaran - totalHarga 
#         print(line)
#         if nilaiAkhir == 0:
#             print('Nominal Pembayaran Pas')
#         elif nilaiAkhir > 0:
#             noteKembalian = "Kembalian Anda Sebesar :               Rp.{},00"
#             print(noteKembalian.format(nilaiAkhir))

#         # print(totalPesanan)
#         print(footer)
#         break

