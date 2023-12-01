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
                totalHargaPembayaran = "Nominal Pembayaran yang anda masukkan :               Rp.{},00\nTotal yang harus di bayarkan          :               Rp.{},00"
                print(totalHargaPembayaran.format(nominalPembayaran, denda))
                nilaiAkhir = nominalPembayaran - denda 
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



# Contoh penggunaan program
perpustakaan = AsgardLibrary()

# BUKU
harryPotter = Book('HRP', 'Harry Potter', 'J.K. Rowling')
lordOfTheRing = Book('LOTR', 'The Lord of the Rings', 'J.R.R. Tolkien')

admin = User('Admin Perpus', '', 'admin')
user = User('User Perpus', '', 'user')
