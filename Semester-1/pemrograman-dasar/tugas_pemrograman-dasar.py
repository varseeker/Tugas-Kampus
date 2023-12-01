# # #--------- 1. Contoh Operator Penugasan: -----------
# # x = 5
# # y = 10

# # x += y  # Operator penugasan +=
# # print(x)  # Output: 15
# # #---------------------------------------------------
# # #---------- 2. Contoh Operator Logika: -------------
# # a = True
# # b = False

# # print(a and b)  # Operator logika AND
# # # Output: False

# # print(a or b)  # Operator logika OR
# # # Output: True

# # print(not b)  # Operator logika NOT
# # # Output: True
# # #---------------------------------------------------
# # #-------- 3. Contoh Operator Bitwise: --------------
# # x = 5  # Representasi biner: 0101
# # y = 3  # Representasi biner: 0011

# # print(x & y)  # Operator bitwise AND
# # # Output: 1 (Representasi biner: 0001)

# # print(x | y)  # Operator bitwise OR
# # # Output: 7 (Representasi biner: 0111)

# # print(x ^ y)  # Operator bitwise XOR
# # # Output: 6 (Representasi biner: 0110)

# # print(~x)  # Operator bitwise NOT
# # # Output: -6 (Representasi biner: 11111111111111111111111111111010)

# # print(x << 1)  # Operator bitwise shift kiri
# # # Output: 10 (Representasi biner: 1010)

# # print(y >> 1)  # Operator bitwise shift kanan
# # # Output: 1 (Representasi biner: 0001)

# # #---------------------------------------------------
# # #--------- 4. Contoh Operator Identitas: -----------
# # x = 5
# # y = 5

# # print(x is y)  # Operator identitas is
# # # Output: True

# # print(x is not y)  # Operator identitas is not
# # # Output: False

# # #---------------------------------------------------
# # #--------- 5. Contoh Operator Keanggotaan: -----------
# # list = [1, 2, 3, 4, 5]

# # print(3 in list)  # Operator keanggotaan in
# # # Output: True

# # print(6 not in list)  # Operator keanggotaan not in
# # # Output: True
# # #---------------------------------------------------

# print("""                     TOKO MAINAN ANAK\n                    ********************""")
# namaPembeli = input("Masukan Nama Pembeli : ")
# kodeMainan = input("Masukan Kode Mainan : ")
# while True:
#         try:
#             harga = int(input('Masukan Harga : '))
#         except:
#             print("Tolong Masukan Input sesuai format yg telah di berikan!")
#             continue
#         if type(harga) is int:
#             break
# while True:
#         try:
#             jmlBeli = int(input('Masukan Jumlah Beli : '))
#         except:
#             print("Tolong Masukan Input sesuai format yg telah di berikan!")
#             continue
#         if type(jmlBeli) is int:
#             break
# totalHarga = jmlBeli * harga
# print("=================================================")
# print("Nama Pembeli           : "+str(namaPembeli))
# print("Kode Kue               : "+str(kodeMainan))
# print("Harga                  : "+str(harga))
# print("Jumlah Beli            : "+str(jmlBeli))
# print("Total                  : "+str(totalHarga))

print("=============================================================")
print("STUDI KASUS 5 - Algoritma Logika - Perhitungan Gaji Pegawai")
print("=============================================================")
print("""Perhitungan yang di gunakan :
Lembur per Jam = 20000
Tunjangan = 20%
Pajak = 10%""")
print("=============================================================")
#deklarasi
nama = ''
gajiPokok = 0
tunjangan = 0
lembur = 0
jamKerja = 0
pajak = 0
totalGaji = 0

#input data
nama = input("Masukkan Nama Pegawai : ")
while True:
        try:
            gajiPokok = int(input("Masukkan Gaji Pokok Pegawai : "))
        except:
            print("Tolong Masukan Input sesuai format yg telah di berikan!")
            continue
        if type(gajiPokok) is int:
            break
while True:
        try:
            jamKerja = int(input("Masukkan Jam Kerja Pegawai : "))
        except:
            print("Tolong Masukan Input sesuai format yg telah di berikan!")
            continue
        if type(jamKerja) is int:
            break
#proses data
tunjangan = gajiPokok * (20/100)
pajak = gajiPokok * (10/100)
if jamKerja > 200:
    lembur = (jamKerja - 200) * 20000
else:
    lembur = 0
totalGaji = gajiPokok + tunjangan - pajak + lembur

#output hasil
print("=============================================================")
print("Data Penggajian Pegawai Atas Nama : ",nama)
print("Gaji Pokok           : Rp. "+ str(gajiPokok))
print("Tunjangan (20%)      : Rp. "+ str(round(tunjangan)))
print("Potongan Pajak (10%) : Rp. "+ str(round(pajak)))
print("=============================================================")
print("Total Jam Kerja      : "+ str(jamKerja))
print("Jumlah Lembur        : Rp. "+ str(lembur))
print("=============================================================")
print("Total Gaji           : Rp. "+ str(round(totalGaji)))
print("=============================================================")
      