JUDUL PROGRAM: Sistem Antrian Rumah Sakit menggunakan Singly Linked List

DESKRIPSI SINGKAT:
Program ini merupakan sebuah program antrian rumah sakit yang dibuat dengan menggunakan bahasa pemrograman python yang menerapkan struktur data singly linked list. Program ini digunakan untuk menambahkan data pasien ke dalam antrian, menampilkan daftar antrian pasien, dan memanggil pasien yang berada pada posisi terdepan.

Program ini menggunakan struktur data singly linked list dikarenakan data antrian pasien bisa terus bertambah dan berkurang. Setiap pasien disimpan dalam node yang saling terhubung dengan menggunakan pointer next. Pada program antrian rumah sakit ini menggunakan fungsi insert untuk menambahkan pasien dan delete untuk menghapus pasien yang telah dipanggil.

SOURCE CODE:
class Node:
    def __init__(self, nama_pasien):
        self.data = nama_pasien
        self.next = None
        
Penjelasan:
-class node digunakan untuk membuat node pada linked list ( node merupakan tempat untuk menyimpan data pasien)
-self.data digunakan untuk menyimpan nama pasien yang diinput oleh user
-self.next sebagai penghubung ke node berikutnya
-Nilai awal pada next adalah none karena node belum terhubung ke node lain

class AntrianRumahSakit:
    def __init__(self):
        self.start = None
        self.rear  = None
        
Penjelasan:
-class AntrianRumahSakit digunakan untuk mengatur seluruh antrian pasien
-self.start digunakan untuk menunjukkan node pertama pada antrian
-self.rear digunakan untuk menunjukkan node terak

def create_new_node(self, nama):
        new_node = Node(nama)
        return new_node
        
Penjelasan:
-Fungsi create_new_node digunakan untuk membuat node baru
-Nama pasien antrian akan dimasukkan ke dalam node
-Node(nama) digunakan untuk memanggil class node
-Setelah node berhasil dibuat, maka node dikembalikan menggunakan return

def insert_at_beg(self, new_node):
        if self.start is None:
            self.start = new_node
            self.rear = new_node
        else:
            new_node.next = self.start
            self.start = new_node
            
Penjelasan:
-def insert_at_beg digunakan untuk menambah node di depan.
--if self.start is None untuk mengecek apakah antrian kosong.
-self.start = new_node  membuat node baru menjadi data pertama.
-self.rear = new_node untuk menjadikan node baru sebagai node terakhir karena baru ada satu data.
-else dapat dijalankan jika antrian sudah ada isi.
-new_node.next = self.start menghubungkan node baru ke node pertama sebelumnya.
-self.start = new_node memindahkan posisi start ke node yang baru

def insert_at_end(self, new_node):
        if self.start is None:
            self.start = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node            
            self.rear = new_node
            
Penjelasan:
-insert_at_end(self, new_node) itu dipakai buat nambahin node baru di belakang linked list.
-self.start untuk meanmbahkan node baru di depan
-self.rear untuk menambahkan node baru di belakang 
-else kan terjadi apanila berhasil menambahkan node di depan atau di belakang

def delete_node(self):
        if self.start is None:
            print("Antrian kosong!!!")
        else:
            pasien_dipanggil = self.start.data
            self.start = self.start.next
            print(f"Pasien {pasien_dipanggil} sedang dipanggil untuk berobat.")
            if self.start is None:
                self.rear = None
                
Penjelasan:
-def insert_at_end dipakai untuk menambahkan data pasien di bagian belakang antrian.
-if self.start is None digunakan untuk mengecek apakah antrian masih kosong atau belum ada pasien.
-self.start = new_node membuat node baru menjadi data pertama.
-self.rear = new_node membuat node baru menjadi data terakhir.
-else  dapat dijalankan jika antrian sudah ada isi.
-self.rear.next = new_node menghubungkan node terakhir sebelumnya ke node baru.
-self.rear = new_node memindahkan posisi rear ke node yang baru ditambahkan.

def display(self):
        if self.start is None:
            print("(antrian kosong)")
            return
        current = self.start
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Selesai")
        
Penjelasan:
-def display digunakan untuk menampilkan isi antrian.
-if self.start is None akan mengecek apakah antrian kosong.
-print("(antrian kosong)") menampilkan pesan jika kosong.
-return untuk menghentikan fungsi.
-current = self.start membuat variabel untuk membaca node pertama.
-while current is not None melakukan perulangan selama node masih ada.
-print(current.data, end=" -> ") untuk menampilkan data pasien.
-current = current.next berpindah ke node berikutnya.
-print("Selesai") untuk menampilkan tanda akhir linked list

def main():
    antrian = AntrianRumahSakit()
    choice = 'y'
Penjelasan:
-def main adalah fungsi utama program.
-antrian = AntrianRumahSakit() membuat object antrian rumah sakit.
-choice = 'y' memberi nilai awal agar perulangan berjalan.

while choice.lower() == 'y':
        nama_pasien = input("Nama pasien baru = ")
        
Penjelasan:
-Digunakan untunk mengulang program selama user menginputkan huruf y
-Input nama pasien digunakan untuk menerima input pasien dari user

print("Membuat data pasien baru")
        new_node = antrian.create_new_node(nama_pasien)
Penjelasan:
-Memanggil create new node () untuk memulai node baru

 if new_node is not None:
            print("Data pasien berhasil dibuat")
        else:
            print("Data pasien tidak dapat dibuat")
            break
            
Penjelasan:
-if new_node is not None akan mengecek apakah node berhasil dibuat
-print(“Data pasien berhasil dibuat”) menampilkan pesan berhasil
-else akan dijalankan bila node berhasil dibuat
-print(“Data Pasien tidak dapat dibuat”) menampilkan pesan gagal.

if insert_choice == 1:
            antrian.insert_at_beg(new_node)
            print("Pasien dimasukkan ke antrian prioritas")
        elif insert_choice == 2:
            antrian.insert_at_end(new_node)
            print("Pasien dimasukkan ke antrian biasa")
        else:
            print("Pilihan tidak valid, pasien dimasukkan ke antrian biasa")
            antrian.insert_at_end(new_node)
            
Penjelasan:
-Mengecek apakah user memilih antrian  depan
-Insert_at_beg untuk memanggil fungsi insert depan
-insert_choice==2 mengecek apakah user memilih antrian belakang
-insert_at_end untuk memanggil fungsi insert belakang

antrian.display()
        choice = input("Mau menambah pasien baru? (y/n) "
Penjelasan:
-antrian.display() akan menampilkan seluruh isi antrian pasien

antrian.delete_node()
        else:
            break
            
Penjelasan:
-antrian. delete_node() untuk menghapus pasien paling depan 
-break untuk menghentikan perulangan

if __name__ == "__main__":
    main()
    
Penjelasan:
-if __name__ == "__main__":  digunakan untuk menjalankan sebuah prugram utama
-main() digunakan untuk memanggil fungsi utama program

OUTPUT PROGRAM:
Nama pasien baru = RIRI
Membuat data pasien baru
Data pasien berhasil dibuat
1. Prioritas (Depan)
2. Antrian biasa (Belakang)
Masukkan ke antrian mana? 2
Pasien dimasukkan ke antrian biasa
Daftar Antrian: RIRI -> Selesai
Mau menambah pasien baru? (y/n) Y
Nama pasien baru = RARA
Membuat data pasien baru
Data pasien berhasil dibuat
1. Prioritas (Depan)
2. Antrian biasa (Belakang)
Masukkan ke antrian mana? 1
Pasien dimasukkan ke antrian prioritas
Daftar Antrian: RARA -> RIRI -> Selesai
Mau menambah pasien baru? (y/n) N
Daftar Antrian: RARA -> RIRI -> Selesai
Panggil pasien berikutnya? (y/n) Y
Pasien RARA sedang dipanggil untuk berobat.
Daftar Antrian: RIRI -> Selesai
Panggil pasien berikutnya? (y/n) Y
Pasien RIRI sedang dipanggil untuk berobat.
Daftar Antrian: (antrian kosong)
Panggil pasien berikutnya? (y/n) N
Pelayanan rumah sakit selesai.
PS C:\Users\NAFALIN FRI ANGINE\OneDrive\Documents\Tugas Study Kasus 1> 
PENJELASAN:
- user menginputkan nama pasien pertama yaitu RIRI
- kemudian memilih antrian 2
- lalu masuk ke antrian belakang
- Input pasien kedua yaitu RARA
- kemudian memilih antrian 1 (prioritas)
- RARA berada di depan RIRI karena RARA adalah pasien prioritas
- proses input pasien sudah selesai
- proses pemanggilan pasien dimana RARA diupanggil terlebih dahulu karena RARA berada di antrian depan
- pasien berikutnya yang dipanggil RIRI
- setelah RIRI dipanggil, sekarang antrian kosong
- user memilih berhenti dan program selesai

LINK YOUTUBE: https://youtu.be/hY-EcTO3Tos?si=X5XxjPxo0Qchx_FU
