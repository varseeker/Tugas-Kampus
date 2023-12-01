# PERTEMUAN PERTAMA
# print("=========================================")
# print("Nama    : Muhammad Ibadurrahman Al-ahsan")
# print("Kelas   : 19.1C.26")
# print("Jurusan : Sistem Informasi")
# print("=========================================")

# PERTEMUAN KE DUA
# print("Data diri mahasiswa")
# nim = input("NIM                    :")
# nama = input("Nama Lengkap           :")
# prodi = input("Program Studi          :")
# alamat = input("Alamat                 :")

# print("\nhasil cetak data diri di atas adalah")
# print("NIM                   :"+str(nim))
# print("Nama Lengkap          :"+str(nama))
# print("Program Studi         :"+str(prodi))
# print("Alamat                :"+str(alamat))

# PERTEMUAN KE TIGA
# print("===== PARKIR UBSI =====")
# totalBayar = 0
# biayaPertama = 10000
# biayaSelanjutnya = 7500

# nama = input('Nama : ')
# noPlat = input('No Plat Kendaraan : ')
# lamaParkir = int(input('Lama Parkir : '))
# totalBayar = (lamaParkir * biayaPertama) + ((lamaParkir - 3) * biayaSelanjutnya) - ((lamaParkir % 3) * biayaPertama)
# print("Total Bayr : "+str(2 % 3))

# PERTEMUAN KE EMPAT
# kode_baju = input("Masukan Kode Baju [SP/AD] : ")
# ukuran = input("Masukan Ukuran Baju [S/M] : ")

# if kode_baju == "SP" or kode_baju == "sp":
#     merk = "SuperDry"
#     if ukuran == "S" or ukuran == "s":
#         harga = 450000
#     elif ukuran == "M" or ukuran == "m":
#         harga = 500000
#     else :
#         harga = 0
# elif kode_baju == "AD" or kode_baju == "ad":
#     merk = "Adidas"
#     if ukuran == "S" or ukuran == "s":
#         harga = 650000
#     elif ukuran == "M" or ukuran == "m":
#         harga = 700000
#     else :
#         harga = 0
# else:
#     merk = "Anda Salah Input Kode Merk"
#     harga = 0

# print("------------------------------")
# print("Merk Baju : "+str(merk))
# print("Harga Baju : Rp.",harga)

#Input 
# pembeli = input("Input Nama Pembeli : ")
# no_hp = input("Input No. Handphone : ")
# jurusan = input("Input Jurusan [SBY/BL/LMP] : ")

#Proses
# if jurusan == "SBY":
#     namajurusan = "Surabaya"
#     harga = 300000
# elif jurusan == "BL":
#     namajurusan = "Bali"
#     harga = 350000
# else :
#     namajurusan = "Lampung"
#     harga = 500000

#Input Jumlah Beli 
# jumlah = int(input("Masukkan Jumlah Beli : "))

#Proses Potongan
# if jumlah >= 3:
#     potongan = (jumlah*harga)*0.1
# else:
#     potongan = 0

# total = (jumlah*harga)-potongan

#Cetak Hasil
# print("------------------------------------")
# print(" PENJUALAN TIKET BUS")
# print(" XYZ")
# print("------------------------------------")
# print("Nama Pembeli : "+str(pembeli))
# print("No. Handphone : "+str(no_hp))
# print("Kode Jurusan yang dipilih : "+str(jurusan))
# print("Nama Kota Tujuan : "+str(namajurusan))
# print("Harga : ",+(harga))
# print("Jumlah Beli : ",+(jumlah))
# print("------------------------------------")
# print("potongan yang didapat : ",+(potongan))
# print("Total Bayar : ",+(total))
# ubay = int(input("Masukkan Uang Bayar : "))
# uangkembali = ubay-total
# print("Uang Kembali : ",+uangkembali)

#TUGAS PERTEMUAN EMPAT
# nis = input("Masukkan NIS : ")
# nama = input("Masukkan Nama : ")
# jurusan = input("Masukkan Jurusan [SI/SIA] : ")

# si = "SI"
# sia = "SIA"

# if jurusan.casefold() == si.casefold() :
#     namaProdi = "Sistem Informasi"
#     harga = 2400000
# elif jurusan.casefold() == sia.casefold():
#     namaProdi = "Sistem Informasi Akuntansi"
#     harga = 20000000
# else : 
#     namaProdi = ""
#     harga = 0

# print("Nama Mahasiswa/i : ",nama)
# print("Nis Mahasiswa/i : ",nis)
# print("Nama Prodi : ",namaProdi)
# print("Harga : ",harga)

# print("PROGRAM MENGHITUNG GAJI KARYAWAN")
# namaKaryawan = input("Masukkan Nama Karyawan : ")
# golonganJabatan = int(input("Masukkan Golongan Jabatan [1/2/3] : "))
# pendidikan = input("Masukkan Pendidikan Karyawan [SMA/D1/D3/S1] : ")
# jumlahJamKerja = int(input("Masukkan Jumlah Jam Kerja Karyawan : "))

# gajiPokok = 300000

# if golonganJabatan == 1:
#     tunjanganJabatan = gajiPokok * (5/100)
# elif golonganJabatan == 2:
#     tunjanganJabatan = gajiPokok * (10/100)
# elif golonganJabatan == 3 :
#     tunjanganJabatan = gajiPokok * (15/100)
# else :
#     tunjanganJabatan = 0

# sma = "SMA"
# d1 = "D1"
# d3 = "D3"
# s1 = "S1"

# if pendidikan.casefold() == sma.casefold():
#     tunjanganPendidikan = gajiPokok * (2.5/100)
# elif pendidikan.casefold() == d1.casefold():
#     tunjanganPendidikan = gajiPokok * (5/100)
# elif pendidikan.casefold() == d3.casefold() :
#     tunjanganPendidikan = gajiPokok * (20/100)
# elif pendidikan.casefold() == s1.casefold() :
#     tunjanganPendidikan = gajiPokok * (30/100)
# else :
#     tunjanganPendidikan = 0

# if jumlahJamKerja > 8:
#     honorLembur = (jumlahJamKerja - 8) * 3500
# else :
#     honorLembur = 0

# totalGaji = gajiPokok + tunjanganJabatan + tunjanganPendidikan + honorLembur

# print("Karyawan yang Bernama        : ",namaKaryawan)
# print("Honor yang diterima")
# print("     Tunjangan Jabatan       : Rp.", tunjanganJabatan)
# print("     Tunjangan Pendidikan    : Rp.", tunjanganPendidikan)
# print("     Honor Lembur            : Rp.", honorLembur)

# print("Total Gaji (gaji pokok + tunjangan + lembur) : Rp.",totalGaji)

#PERTEMUAN KE LIMA
# ulang=2
# for i in range(ulang):
#     print ("data Ke - " + str(i+1))
#     nama=input("Masukkan Nim anda : ")
#     uts=int(input("Masukkan Nilai UTS anda :"))
#     uas=int(input("Masukkan Nilai UAS : "))
#     print("NIm anda adalah %s nilai UTS anda %i nilai UTS anda %i" % (nama,uts,uas))
#     print("-------------------------------------\n")

#TUGAS PERTEMUAN KE LIMA
# print("GEROBAK FRIED CHICKEN\n")
# print("Kode  | Jenis Potong   | Harga")
# print("----------------------------------")
# print(" D    |  DADA          | Rp. 2500")
# print(" P    |  PAHA          | Rp. 2000")
# print(" S    |  SAYAP         | Rp. 1500")
# print("----------------------------------")
# d = "D"
# p = "P"
# s = "S"

# kode =  []
# banyakPotong = []
# jenisPotong = []
# harga = []
# totalHarga = []

# while True:
#     banyakjenis = int(input("Banyak Jenis : "))
#     if type(banyakjenis) is int:
#         break
#     else: 
#         print("Tolong Masukan Input sesuai format yg telah di berikan!")

# count = 0
# while count < banyakjenis:
#     print("Jenis Ke-", count+1)
#     while True:
#         tempCode = input("kode potong [D/P/S] : ")
#         if tempCode.casefold() == d.casefold() or tempCode.casefold() == p.casefold() or tempCode.casefold() == s.casefold():
#             kode.append(tempCode)
#             break
#         else: 
#             print("Tolong Masukan Input sesuai format yg telah di berikan!")
#             continue
#     banyakPotong.append(int(input("banyak potong : ")))

#     if kode[count].casefold() == d.casefold():
#         jenisPotong.append("Dada")
#         harga.append(" 2500")
#         totalHarga.append(banyakPotong[count] * 2500)
#     elif kode[count].casefold() == p.casefold():
#         jenisPotong.append("Paha")
#         harga.append(" 2000")
#         totalHarga.append(banyakPotong[count] * 2000)
#     elif kode[count].casefold() == s.casefold():
#         jenisPotong.append("Sayap")
#         harga.append("1500")
#         totalHarga.append(banyakPotong[count] * 1500)
#     count += 1

# print("GEROBAK FRIED CHICKEN")
# print("----------------------------------------------------------------------")
# print("No   Jenis       Harga Satuan        Banyak Beli         Jumlah Harga")
# print("----------------------------------------------------------------------")
# count = 1
# jumlahBayar = 0
# for item in range(len(kode)):
#     print(count,"   ",jenisPotong[item],"       ",harga[item],"                ",banyakPotong[item],"                ",totalHarga[item])
#     jumlahBayar += totalHarga[item]
#     count += 1
# print("----------------------------------------------------------------------")
# print("                                        Jumlah Bayar : Rp. ",jumlahBayar)
# pajak = jumlahBayar * (10/100)
# print("                                        Pajak 10%    : Rp. ",round(pajak))
# print("                                        Total Bayar  : Rp. ",round(jumlahBayar + pajak))

# Latihan Pertemuan Ke 6
# list_nim = []
# list_uts = []
# list_uas = []
# list_total = [] 

# Tugas Pertemuan Ke 6




import pandas as pd

# Data menu
data = {
    'Kode Menu': ['ml', 'cl', 'rv', 'pz', 'ff'],
    'Jenis Menu': ['Matcha Latte', 'Chocolatte', 'Red Velvet', 'Pizza', 'French Frice'],
    'Harga Satuan': [20000, 17000, 17000, 50000, 18000]
}

menu_df = pd.DataFrame(data)

# Fungsi untuk menghitung total harga dengan pajak
def hitung_total(banyak_menu, kode_menu):
    try:
        harga_satuan = menu_df[menu_df['Kode Menu'] == kode_menu]['Harga Satuan'].values[0]
        total_sebelum_pajak = banyak_menu * harga_satuan
        return total_sebelum_pajak
    except IndexError:
        return None

# Input jumlah dan kode menu
belanja = []
overallTotal = 0

while True:
    kode_menu = input("Masukkan kode menu (ml, cl, rv, pz, ff) atau ketik 'selesai' untuk mengakhiri: ")
    if kode_menu.lower() == 'selesai':
        pajak = 0.1 * overallTotal
        overallTotal = overallTotal + pajak
        belanja.append(['-', '-', 'Total Pesanan', overallTotal])
        break
    if kode_menu in menu_df['Kode Menu'].values:
        banyak_menu = int(input(f"Masukkan jumlah {menu_df[menu_df['Kode Menu'] == kode_menu]['Jenis Menu'].values[0]} yang dipesan: "))
        total_harga = hitung_total(banyak_menu, kode_menu)
        overallTotal += total_harga
        belanja.append([menu_df[menu_df['Kode Menu'] == kode_menu]['Jenis Menu'].values[0], menu_df[menu_df['Kode Menu'] == kode_menu]['Harga Satuan'].values[0], banyak_menu, total_harga])
    else:
        print("kode menu tidak valid. mohon cek kembali")

#membuat dataframe untuk menampilkan tabel
tabel_belanja = pd.DataFrame(belanja, columns=['jenis menu','harga satuan', 'banyak beli', 'total harga'])
# menampilkan tabel
print("\n===== Tabel Belanja =====")
print(tabel_belanja.to_string(index=False))