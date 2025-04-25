from flask import Flask
import pandas as pd
from abc import ABC, abstractmethod

class Book:
    id = ''
    judul = ''
    pengarang = ''
    stok = 0
    def __init__(self, id, judul, pengarang):
        self.id = id
        self.judul = judul
        self.pengarang = pengarang

class Customer:
    nama = ''
    item = ''
    totalBiaya = 0

class User(Customer):
    def __init__(self, nama, item, password):
        super().__init__(nama, item)
        self.password = password

class Library(ABC):
    @abstractmethod
    def tambah_buku(self, book: Book, total): pass

    @abstractmethod
    def pinjam_buku(self, id): pass

    @abstractmethod
    def hapus_buku(self, id): pass

    @abstractmethod
    def kembalikan_buku(self, id, hari_terlambat): pass

    @abstractmethod
    def display_data_buku(self): pass

class AsgardLibrary(Library):
    def __init__(self):
        self.bukuDefault = {
            'ID Buku': ['HRPT','OPM'], 
            'Judul': ['Harry Potter', 'One Punch Man'], 
            'Pengarang': ['J.K. Rowling', 'Yusuke Murata'], 
            'Status': ['Tersedia', 'Tersedia'], 
            'Stok': [5, 3]}
        self.data_buku = pd.DataFrame(self.bukuDefault, columns=['ID Buku', 'Judul', 'Pengarang', 'Status', 'Stok'])
        self.denda_per_hari = 50000

    def tambah_buku(self, book :Book, total):
        if book.id in self.data_buku['ID Buku'].values:
            self.data_buku.loc[self.data_buku['ID Buku'] == book.id, 'Status'] = 'Tersedia'
            self.data_buku.loc[self.data_buku['ID Buku'] == book.id, 'Stok'] += total
        else:
            self.data_buku = self.data_buku._append({'ID Buku':book.id, 'Judul': book.judul, 'Pengarang': book.pengarang, 'Status': 'Tersedia', 'Stok':total}, ignore_index=True)

        print(f"Buku '{book.judul}' oleh {book.pengarang} berjumlah {total} buku berhasil ditambahkan ke perpustakaan.")

    def pinjam_buku(self, id):
        if id in self.data_buku['ID Buku'].values:
            if self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Status'].values[0] == 'Tersedia' and self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Stok'].values[0] > 0:
                self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Stok'] -= 1
                if self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Stok'].values[0] == 0:
                    self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Status'] = 'Dipinjam'
                print(f"Anda berhasil meminjam buku '{self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Judul'].values[0]}' dengan tenggat waktu 7 Hari atau 1 Minggu.")
            else:
                self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Status'] = 'Dipinjam'
                print(f"Buku '{self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Judul'].values[0]}' sedang dipinjam oleh orang lain.")
        else:
            print(f"Buku '{self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Judul'].values[0]}' tidak tersedia di perpustakaan.")
    
    
    def hapus_buku(self, id):
        if id in self.data_buku['ID Buku'].values:
            print(f"Anda Berhasil Menghapus Data Buku dengan Judul '{self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Judul'].values[0]}' yang memiliki ID Buku '{self.data_buku.loc[self.data_buku['ID Buku'] == id, 'ID Buku'].values[0]}' .")
            self.data_buku = self.data_buku.drop(self.data_buku[self.data_buku['ID Buku'] == id].index)
        else:
            print(f"Buku '{self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Judul'].values[0]}' tidak tersedia di perpustakaan.")

    def kembalikan_buku(self, id, hari_terlambat):
        if id in self.data_buku['ID Buku'].values:
            self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Stok'] += 1
            self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Status'] = 'Tersedia'
            if hari_terlambat > 0:
                denda = hari_terlambat * self.denda_per_hari
                print(f"Anda telah mengembalikan buku '{self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Judul'].values[0]}' dengan keterlambatan {hari_terlambat} hari. Denda yang harus dibayar: Rp {denda}")
                while True:
                    try:
                        nominalPembayaran = int(input("Silahkan Masukkan Nominal Pembayaran : "))
                    except:
                        print("Tolong Masukan Input sesuai format yg telah di berikan!")
                        continue
                    if type(nominalPembayaran) is int:
                        if nominalPembayaran < denda: 
                            print('Nominal Pembayaran Tidak dapat kurang atau lebih kecil dari total\nharga denda.')
                        else:
                            break
                print(line)
                totalHargaPembayaran = "Nominal Pembayaran yang anda masukkan :               Rp.{},00\nTotal yang harus di bayarkan          :               Rp.{},00"
                print(totalHargaPembayaran.format(nominalPembayaran, denda))
                nilaiAkhir = nominalPembayaran - denda 
                print(line)
                if nilaiAkhir == 0:
                    print('Nominal Pembayaran Pas')
                elif nilaiAkhir > 0:
                    noteKembalian = "Kembalian Anda Sebesar :               Rp.{},00"
                    print(noteKembalian.format(nilaiAkhir))
            else : 
                print(f"Anda telah mengembalikan buku '{self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Judul'].values[0]}'")
        else:
            print(f"Buku '{self.data_buku.loc[self.data_buku['ID Buku'] == id, 'Judul'].values[0]}' tidak tersedia di perpustakaan.")

    def display_data_buku(self):
        self.data_buku.index = range(1, self.data_buku.shape[0] + 1)
        print(self.data_buku)

def get_non_empty_input(prompt):
    user_input = input(prompt)
    while not user_input:
        print("Input tidak bisa kosong. Harap Coba Kembali.")
        user_input = input(prompt)
    return user_input



app = Flask(__name__)

@app.route('/')
def hello_world():
    # Contoh penggunaan program
    perpustakaan = AsgardLibrary()

    # BUKU
    harryPotter = Book('HRP', 'Harry Potter', 'J.K. Rowling')
    lordOfTheRing = Book('LOTR', 'The Lord of the Rings', 'J.R.R. Tolkien')

    line = '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-='
    titleAdmin = """=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
                                PERPUSTAKAAN ASGARD
                        ----- Collection from the gods ------
        SELAMAT DATANG 
        Berikut Layanan yang kita miliki :
        1. Tambahkan Buku
        2. Pinjam Buku
        3. Kembalikan Buku
        4. Hapus Data Buku
        5. Tampilkan List Buku
        6. Keluar Apps
        ----------------------------------
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
    """
    titleUser = """=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
                                PERPUSTAKAAN ASGARD
                        ----- Collection from the gods ------
        SELAMAT DATANG 
        Berikut Layanan yang kita miliki :
        1. Pinjam Buku
        2. Kembalikan Buku
        3. Tampilkan List Buku
        4. Keluar Apps
        ----------------------------------
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
    """
    footer = """
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
                                Terima Kasih
                                Datang Kembali :)
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
    """
    apps = True
    loginStatus = True
    while apps:
        while loginStatus:
            userName = input("Masukkan Username : ")
            password = input("Masukkan Password : ")
            if (userName == 'user' and password == 'user') or (userName == 'admin' and password == 'admin'):
                loginStatus = False;
                break
            else:
                print("Username atau Password tidak sesuai, harap periksa kembali.")
                continue
        while True:
            if userName == 'admin':
                print(titleAdmin)
            elif userName == 'user':
                print(titleUser)
            try:
                nomorLayanan = int(input('Pilih Nomor Layanan : '))
            except:
                print("Tolong Masukan Input sesuai format yg telah di berikan!")
                continue
            if type(nomorLayanan) is int:
                if userName == 'admin':
                    if nomorLayanan > 6 or nomorLayanan < 1: 
                        print('Nomor layanan tidak boleh lebih dari 5 atau di bawah 1')
                        continue
                    else:
                        break
                elif userName == 'user':
                    if nomorLayanan > 4 or nomorLayanan < 1: 
                        print('Nomor layanan tidak boleh lebih dari 4 atau di bawah 1')
                        continue
                    else:
                        break
        if userName == 'admin':
            if nomorLayanan == 1:
                print('Masukkan Data Buku : ')
                idBuku = get_non_empty_input(" - Masukkan ID BUKU : ")
                judulBuku = get_non_empty_input(" - Masukkan JUDUL BUKU : ")
                pengarangBuku = get_non_empty_input(" - Masukkan PENGARANG BUKU : ")
                while True:
                    try:
                        stokBuku = int(input(" - Masukkan STOK BUKU : "))
                    except:
                        print("Tolong Masukan Input sesuai format yg telah di berikan!")
                        continue
                    if type(stokBuku) is int:
                        if stokBuku <= 0: 
                            print('Stok Buku tidak bisa lebih kecil dari 0.')
                        else:
                            break
                detailBuku = Book(idBuku.upper(), judulBuku, pengarangBuku)
                perpustakaan.tambah_buku(detailBuku, stokBuku)
            elif nomorLayanan == 2:
                idBuku = get_non_empty_input("Masukkan ID BUKU yang ingin di pinjam : ")
                perpustakaan.pinjam_buku(idBuku.upper())
            elif nomorLayanan == 3:
                idBuku = get_non_empty_input("Masukkan ID BUKU yang ingin di kembalikan : ")
                while True:
                    try:
                        hariDenda = int(input("Masukkan Jumlah hari telat pengembalian : "))
                    except:
                        print("Tolong Masukan Input sesuai format yg telah di berikan!")
                        continue
                    if type(hariDenda) is int:
                        if hariDenda < 0: 
                            print('Denda Buku tidak bisa lebih kecil dari 0.')
                        else:
                            break
                perpustakaan.kembalikan_buku(idBuku, hariDenda)
            elif nomorLayanan == 4:
                idBuku = get_non_empty_input('Masukan ID BUKU yang ingin di hapus : ')
                perpustakaan.hapus_buku(idBuku.upper())
            elif nomorLayanan == 5:
                print('Berikut adalah list buku di Perpustakaan Asgard : ')
                perpustakaan.display_data_buku()
        elif userName == 'user':
            if nomorLayanan == 1:
                idBuku = input("Masukkan ID BUKU yang ingin di pinjam : ")
                perpustakaan.pinjam_buku(idBuku.upper())
            elif nomorLayanan == 2:
                idBuku = input("Masukkan ID BUKU yang ingin di kembalikan : ")
                while True:
                    try:
                        hariDenda = int(input("Masukkan Jumlah hari telat pengembalian : "))
                    except:
                        print("Tolong Masukan Input sesuai format yg telah di berikan!")
                        continue
                    if type(hariDenda) is int:
                        if hariDenda < 0: 
                            print('Denda Buku tidak bisa lebih kecil dari 0.')
                        else:
                            break
                perpustakaan.kembalikan_buku(idBuku, hariDenda)
            elif nomorLayanan == 3:
                print('Berikut adalah list buku di Perpustakaan Asgard : ')
                perpustakaan.display_data_buku()

        if (nomorLayanan == 6 and userName == 'admin') or (nomorLayanan == 4 and userName == 'user'):
            print(footer)
            apps = False
        else:
            continue

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)