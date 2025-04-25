# statusInput = True;

# while statusInput:
#         try:
#             brt = int(input('Masukkan Berat Telur : '))
#         except:
#             print("Tolong Masukan Input sesuai format yg telah di berikan!")
#             continue
#         if type(brt) is int:
#             break

# while statusInput:
#         try:
#             hrg = int(input('Masukkan Harga Telur : '))
#         except:
#             print("Tolong Masukan Input sesuai format yg telah di berikan!")
#             continue
#         if type(hrg) is int:
#             break

# while statusInput:
#         try:
#             ongkos = int(input('Masukkan Transport : '))
#         except:
#             print("Tolong Masukan Input sesuai format yg telah di berikan!")
#             continue
#         if type(ongkos) is int:
#             break

# while statusInput:
#         try:
#             uangIbu = int(input('Masukkan Uang Ibu : '))
#         except:
#             print("Tolong Masukan Input sesuai format yg telah di berikan!")
#             continue
#         if type(uangIbu) is int:
#             sisaUang = uangIbu - (brt * hrg) - ongkos
#             if sisaUang < 0: 
#                 print('Nominal Pembayaran Tidak dapat kurang atau lebih kecil dari total.')
#             else:
#                 break
# txtTotalHarga = "Total Kembalian :               Rp.{},00"
# print(txtTotalHarga.format(sisaUang));

# name = ""
# name = input("Masukkan Nama : ")
# length = len(name)
# for i in range(length):
#     print(name[i:])

#Fungsi Pangkat secara Rekursif
# def pangkat(x,y):
#     if y == 0:
#         return 1
#     else:
#         return x * pangkat(x,y-1)

# x = 0
# while True:
#     x = int(input("Masukan Tanggal Lahir : "))
#     if x < 0 or x > 31:
#         continue
#     else:
#         break
# y = 0
# while True:
#     y = int(input("Masukan Bulan Lahir : "))
#     if y < 0 or y > 12:
#         continue
#     else:
#         break

# print("%d dipangkatkan %d = %d" % (x,y,pangkat(x,y)))

#Fungsi Faktorial secara Rekursif
# def faktorial(a):
#     if a == 1:
#         return (a)
#     else:
#         return (a*faktorial(a-1))
# bil = 0
# while True:
#     bil = int(input("Masukan Tanggal Lahir : "))
#     if bil < 0 or bil > 31:
#         continue
#     else:
#         break
# print("%d! = %d" % (bil, faktorial(bil)))

# Fibonacci Secara Rekursif
# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return (fibonacci(n-1) + fibonacci(n-2))
# x = 0
# while True:
#     x = int(input("Masukan Batas Deret Bilangan Fibonacci : "))
#     if x < 0 or x > 31:
#         continue
#     else:
#         break
# print("Deret Fibonacci")
# for i in range(x):
#     print(fibonacci(i),end=' ')

# Menara Hanoi Secara Rekursif
# def menaraHanoi(n , asal, tujuan, bantu):
#     if n==1:
#         print ("Pindahkan Piringan 1 dari menara",asal,"to tujuan",tujuan)
#         return
#     menaraHanoi(n-1, asal, bantu, tujuan)
#     print ("Pindahkan Piringan",n,"dari menara",asal,"to tujuan",tujuan)
#     menaraHanoi(n-1, bantu, tujuan, asal)
# def menaraHanoi(n):
#     if n == 0:
#         return 1
#     else:
#         return (2 * (n-1)) - 1
# n = 0
# while True:
#     n = int(input("Masukan Tanggal Lahir : "))
#     if n < 0 or n > 31:
#         continue
#     else:
#         break
# menaraHanoi(n) 

# A
# p = 0
# q = 5
# r = 10

# p = q
# q = r

# print("Nilai :", p)
# print("Nilai :", q)
# print("Nilai :", r)

# B
# p = 10
# p = p + 1
# q = p

# print ("Nilai P : ", p)
# print ("Nilai Q : ", q)

# C
# P = 5
# Q = 6
# R = 7

# S=P
# P=Q
# Q=R
# R=S

# print("Nilai P sekarang adalah", P)
# print("Nilai Q sekarang adalah", Q)
# print("Nilai R sekarang adalah", R)

# D
# bil = 1
# while bil < 10:
#     if bil < 5 or bil > 5:
#         print(bil)
#     bil += 1
    
# E
# name = ""
# name = input("Masukkan Nama : ")
# length = len(name)
# for i in range(length, 0, -1):
#     print(name[:i])

# F
# n = 5 
# tiangA = "Tiang A"
# tiangB = "Tiang B"
# tiangC = "Tiang C"

# def tiangHanoi(n, tiangA, tiangB, tiangC):
#     if n == 1:
#         print(f"piring 1 dari {tiangA} ke {tiangB}")
#         return
    
#     tiangHanoi(n-1, tiangA, tiangC, tiangB)
#     print(f"piring {n} dari {tiangA} ke {tiangB}")
#     tiangHanoi(n-1, tiangC, tiangB, tiangA)

# tiangHanoi(n, tiangA, tiangB, tiangC)

# mahasiswa = []

# nim = input("Masukkan NIM: ")
# nama = input("Masukkan Nama: ")

# mahasiswa.append(nim)
# mahasiswa.append(nama)

# # Menampilkan NIM dan Nama
# print("NIM:", mahasiswa[0])
# print("Nama:", mahasiswa[1])

# n = 4
# A = []

# for i in range(n):
#     row = []
#     for j in range(n):
#         if j <= i:
#             row.append(i + 1)
#         else:
#             row.append(0)
#     A.append(row)

# for row in A:
#     print(row)

# nilai = [1, 2, 3, 4]

# for i in range(len(nilai)):
#     nilai[i] = 2*i + 1

# print(nilai)

# n = int(input("Masukkan banyaknya elemen array = "))
# total = 0

# for i in range(n):
#     num = float(input("Masukkan nilai ke-{} = ".format(i+1)))
#     total += num

# average = total / n

# print("Hasil nilai total adalah = ", total)
# print("Hasil rata-rata adalah = ", average)

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1
#     return arr

# nim_list = []
# n = int(input("Masukkan jumlah NIM yang akan diurutkan: "))
# for i in range(n):
#     nim = int(input("Masukkan NIM ke-{}: ".format(i+1)))
#     nim_list.append(nim)

# print("NIM sebelum diurutkan:", nim_list)
# sorted_nim_selection = selection_sort(nim_list)
# print("NIM setelah diurutkan dengan selection sort:", sorted_nim_selection)
# sorted_nim_merge = merge_sort(nim_list)
# print("NIM setelah diurutkan dengan merge sort:", sorted_nim_merge)

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# input_data = []
# n = int(input("Masukkan jumlah data yang akan diurutkan: "))
# for i in range(n):
#     nim = input("Masukkan NIM ke-{}: ".format(i+1))
#     tanggal_lahir = input("Masukkan tanggal lahir (DDMM): ")
#     tahun_lahir = input("Masukkan tahun lahir: ")
#     input_data.append(nim + tanggal_lahir + tahun_lahir)

# print("Data sebelum diurutkan:", input_data)

# selection_sort(input_data)
# print("Hasil selection sort:", input_data)

# insertion_sort(input_data)
# print("Hasil insertion sort:", input_data)

# bubble_sort(input_data)
# print("Hasil bubble sort:", input_data)

#  Linear/Sequential Search
# def seqSearch(data, key):
#     i=0 
#     pos = i + 1
#     while(i<len(data)):
#         if data[i] == key:
#             break
#         i+=1
#         pos=i+1
#     if pos <= len(data):
#         print('data', key, 'ditemukan di posisi', pos)
#     else:
#         print('data tidak ditemukan')
#         return pos
# data=[19, 23, 17, 85, 8]
# seqSearch(data,85)

# # Strait Max Min biasa
# def max_min(data):
#     i = data[0]
#     s = data[0]
#     for num in data :
#         if num > i :
#             i = num
#         elif num < s:
#             s = num
#     return i, s
# print (max_min([19,23,17,85,9]))

# # Strait Max Min best case
# def straitmaxmin(arr):
#     n = len(arr)
#     if n % 2 == 0:
#         mx = max(arr[0], arr[1])
#         mn = min(arr[0], arr[1])
#         i = 2
#     else:
#         mx = mn = arr[0]
#         i = 1
#     while i < n - 1:
#         if arr[i] < arr[i + 1]:
#             mx = max(mx, arr[i + 1])
#             mn = min(mn, arr[i])
#         else:
#             mx = max(mx, arr[i])
#             mn = min(mn, arr[i + 1])
#         i += 2
#     return (mx, mn)

# arr = [9, 17, 19, 23, 85]
# mx, mn = straitmaxmin(arr)
# print("Nilai Maksimum : ", mx)
# print("Nilai Minimum : ", mn)

# # Strait Max Min worst case
# def straitmaxmin(arr):
#     n = len(arr)
#     if n % 2 == 0:
#         mx = max(arr[0], arr[1])
#         mn = min(arr[0], arr[1])
#         i = 2
#     else:
#         mx = mn = arr[0]
#         i = 1
#     while i < n - 1:
#         if arr[i] < arr[i + 1]:
#             mx = max(mx, arr[i + 1])
#             mn = min(mn, arr[i])
#         else:
#             mx = max(mx, arr[i])
#             mn = min(mn, arr[i + 1])
#         i += 2
#     return (mx, mn)

# arr = [85, 23, 19, 17, 9]
# mx, mn = straitmaxmin(arr)
# print("Nilai Maksimum : ", mx)
# print("Nilai Minimum : ", mn)

# # Strait Max Min average case
# def straitmaxmin(arr):
#     n = len(arr)
#     if n % 2 == 0:
#         mx = max(arr[0], arr[1])
#         mn = min(arr[0], arr[1])
#         i = 2
#     else:
#         mx = mn = arr[0]
#         i = 1
#     while i < n - 1:
#         if arr[i] < arr[i + 1]:
#             mx = max(mx, arr[i + 1])
#             mn = min(mn, arr[i])
#         else:
#             mx = max(mx, arr[i])
#             mn = min(mn, arr[i + 1])
#         i += 2
#     return (mx, mn)

# arr = [19, 23, 17, 85]
# mx, mn = straitmaxmin(arr)
# print("Nilai Maksimum : ", mx)
# print("Nilai Minimum : ", mn)
# Data barang
# barang = [
#     {"nama": "beras", "berat": 14, "profit": 28},
#     {"nama": "gula", "berat": 10, "profit": 40},
#     {"nama": "kentang", "berat": 20, "profit": 70},
#     {"nama": "bawang", "berat": 12, "profit": 36},
#     {"nama": "emping", "berat": 16, "profit": 24}
# ]

# # Mengurutkan barang berdasarkan profit/berat (Pi/Wi)
# barang.sort(key=lambda x: x["profit"]/x["berat"], reverse=True)

# # a. Pola urutan data yang baru untuk Pi
# print("Pola urutan data yang baru untuk Pi:")
# for item in barang:
#     print(item["nama"])

# # b. Pola urutan data yang baru untuk Wi
# barang.sort(key=lambda x: x["berat"], reverse=True)
# print("\nPola urutan data yang baru untuk Wi:")
# for item in barang:
#     print(item["nama"])

# # Mengisi truk dengan menggunakan kriteria greedy
# kapasitas_truk = 40
# total_berat = 0
# total_profit = 0
# barang_diangkut = []

# for item in barang:
#     if total_berat + item["berat"] <= kapasitas_truk:
#         total_berat += item["berat"]
#         total_profit += item["profit"]
#         barang_diangkut.append(item["nama"])

# # c. Profit nilai maksimal yang didapat
# print("\nProfit nilai maksimal yang didapat:", total_profit, "Juta")

# import threading
# import time

# class TrafficLight:
#     def __init__(self):
#         self.color = "Merah"
#         self.running = True

#     def change_light(self):
#         while self.running:
#             if self.color == "merah":
#                 print("Lampu Warna Merah Menyala")
#                 time.sleep(5)
#                 self.color = "hijau"
#             elif self.color == "hijau":
#                 print("Lampu Warna Hijau Menyala")
#                 time.sleep(5)
#                 self.color = "kuning"
#             else:
#                 print("Lampu Warna Kuning Menyala")
#                 time.sleep(2)
#                 self.color = "merah"

#     def stop(self):
#         self.running = False

# traffic_light = TrafficLight()
# light_thread = threading.Thread(target=traffic_light.change_light)
# light_thread.start()

# # Untuk menghentikan program setelah beberapa saat
# time.sleep(20)
# traffic_light.stop()
# light_thread.join()

import turtle

# Create a playground for turtles
wn = turtle.Screen()
wn.bgcolor('skyblue')

# Create turtles
tess = turtle.Turtle()
alex = turtle.Turtle()
henry = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color('black', 'white')
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(157)
    tess.circle(40, 180)
    tess.forward(157)
    tess.left(90)
    tess.end_fill()

draw_housing()

def circle(t, ht, colr):
    """Position turtle onto the place where the lights should be, and
    turn turtle into a big circle"""
    t.penup()
    t.forward(40)
    t.left(90)
    t.forward(ht)
    t.shape('circle')
    t.fillcolor(colr)

circle(tess, 40, 'green')
circle(alex, 100, 'orange')
circle(henry, 160, 'red')

# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num  # The global keyword tells Python not to create a new local variable for state_num
    if state_num == 0:  # Transition from state 0 to state 1
        henry.color('darkgrey')
        alex.color('darkgrey')
        tess.color('green')
        wn.ontimer(advance_state_machine, 3000)  # set the timer to expire in 3000 milliseconds (3 seconds)
        state_num = 1
    elif state_num == 1:  # Transition from state 1 to state 2
        henry.color('darkgrey')
        alex.color('orange')
        wn.ontimer(advance_state_machine, 1000)
        state_num = 2
    elif state_num == 2:  # Transition from state 2 to state 3
        tess.color('darkgrey')
        wn.ontimer(advance_state_machine, 1000)
        state_num = 3
    else:  # Transition from state 3 to state 0
        henry.color('red')
        alex.color('darkgrey')
        wn.ontimer(advance_state_machine, 2000)
        state_num = 0

# Start the state machine
advance_state_machine()

wn.listen()  # Listen for events
wn.mainloop()  # Wait for the user to close the window
