**JUDUL PROGRAM**: Sistem Manajemen Tumpukan Buku di Meja 

**DESKRIPSI SINGKAT:**
Program ini adalah sebuah aplikasi sederhana di terminal komputer untuk mencontohkan cara kerja struktur data bernama Stack (Tumpukan). Program ini dibuat menggunakan bahasa pemrograman Python dengan memanfaatkan media penyimpanan berupa List. Supaya simulasinya terasa nyata, ukuran tumpukannya sengaja kita batasi (statis) agar tidak bisa menampung terlalu banyak buku.
Konsep utama yang dipakai dalam program ini adalah aturan LIFO (Last In, First Out). Sederhananya, buku yang paling terakhir kamu taruh di atas meja otomatis akan berada di posisi paling atas, dan buku paling atas itulah yang harus diambil pertama kali oleh pengguna supaya tumpukan buku di bawahnya tidak berantakan atau roboh.
SOURCE CODE
<img width="1053" height="962" alt="Screenshot 2026-05-16 200319" src="https://github.com/user-attachments/assets/c7eee62a-c581-489e-80d5-8b66af3216e8" />
<img width="1096" height="486" alt="Screenshot 2026-05-16 200338" src="https://github.com/user-attachments/assets/9da46bee-9279-4ec0-bf81-4cdb2473f739" />
<img width="1091" height="607" alt="Screenshot 2026-05-16 200349" src="https://github.com/user-attachments/assets/c3825e48-4a2a-4ce4-bd94-a192180d3b36" />
Penjelasan
Kelas StackArray
- class StackArray:Baris ini digunakan untuk membuat kelas baru bernama StackArray yang berisi semua fungsi untuk mengatur tumpukan buku.
- def __init__(self, max_size=5):Baris ini adalah fungsi awal yang otomatis berjalan saat objek dibuat. Nilai bawaan kapasitas tumpukan adalah 5.
- self.MAX = max_size Baris ini menyimpan jumlah maksimal kapasitas tumpukan ke variabel self.MAX.
- self.st = [None] * self.MAX Baris ini membuat list kosong dengan ukuran tetap sesuai kapasitas maksimum.
- self.top_idx = -1 Baris ini mengatur posisi indeks teratas menjadi -1, artinya tumpukan masih kosong.
- Fungsi is_empty() digunakan untuk mengecek apakah stack sedang kosong atau tidak. 
- def is_empty(self): Baris ini membuat fungsi untuk mengecek apakah tumpukan kosong atau tidak.
- return self.top_idx == -1 Jika indeks teratas masih -1, fungsi akan menghasilkan True yang berarti kosong.
- Fungsi is_full() digunakan untuk mengecek apakah stack sudah penuh. 
- def is_full(self): Baris ini membuat fungsi untuk mengecek apakah tumpukan sudah penuh.
- return self.top_idx == self.MAX - 1 Jika indeks teratas sudah sama dengan batas terakhir array, berarti tumpukan penuh.

Fungsi push() untuk menambahkan data baru ke dalam stack 
- def push(self, x): Baris ini membuat fungsi untuk menambahkan buku baru ke tumpukan.
- if self.is_full(): Mengecek apakah tumpukan sudah penuh.
- print("Gagal: Tumpukan sudah penuh, nanti roboh.") Menampilkan pesan bahwa buku tidak bisa ditambahkan karena penuh.
-return Untuk menghentikan proses penambahan buku.
- self.top_idx += 1 Untuk menambah posisi indeks teratas satu langkah ke atas.
- self.st[self.top_idx] = x Untuk menyimpan judul buku ke posisi teratas.
- print(f"Buku '{x}' berhasil ditaruh di paling atas.") Untuk menampilkan pesan bahwa buku berhasil ditambahkan.

Fungsi pop() untuk mengambil sekaligus menghapus data paling atas dari stack 
- def pop(self): Baris ini membuat fungsi untuk mengambil buku paling atas.
- if self.is_empty(): Untuk mengecek apakah tumpukan kosong.
- print("Gagal: Tidak ada buku di meja.") Untuk menampilkan pesan bahwa tidak ada buku yang bisa diambil.
- return Untuk menghentikan proses jika kosong.
- print(f"Buku '{self.st[self.top_idx]}' diambil.") Untuk menampilkan judul buku yang diambil.
- self.top_idx -= 1 Untuk mengurangi posisi indeks teratas satu langkah ke bawah.

Fungsi peek() untuk melihat data paling atas tanpa menghapusnya 
- def peek(self): Baris ini membuat fungsi untuk melihat buku paling atas tanpa mengambilnya.
- if self.is_empty(): Untuk mengecek apakah tumpukan kosong.
- print("Meja kosong.") Untuk menampilkan pesan bahwa tidak ada buku.
- return Untuk menghentikan proses jika kosong.
- print(f"Buku teratas saat ini: {self.st[self.top_idx]}") Untuk menampilkan judul buku paling atas.

Fungsi display() untuk menampilkan semua isi stack dari atas ke bawah 
- def display(self): Baris ini membuat fungsi untuk menampilkan semua isi tumpukan.
- if self.is_empty(): Untuk mengecek apakah tumpukan kosong.
- print("Meja kosong.") Untuk menampilkan pesan jika tidak ada buku.
- return Untuk menghentikan proses jika kosong.
- print("Daftar buku dari atas ke bawah:") Untuk menampilkan judul daftar buku.
- for i in range(self.top_idx, -1, -1):Untuk melakukan perulangan dari indeks paling atas sampai bawah.
- print(f"- {self.st[i]}") Untuk menampilkan setiap judul buku di tumpukan.

Fungsi Utama main()
- def main(): Baris ini membuat fungsi utama untuk menjalankan program.
- stack = StackArray() Baris ini membuat objek tumpukan baru bernama stack.
- pilih = 0 Untuk membuat variabel pilih dengan nilai awal 0.
- while pilih != 5: Program akan terus mengulang selama pengguna belum memilih menu 5
- print("\nMENU TUMPUKAN BUKU") Untuk menampilkan judul menu.
- print("1. Taruh Buku (Push)") Untuk menampilkan menu tambah buku.
- print("2. Ambil Buku (Pop)") Untuk menampilkan menu ambil buku.
- print("3. Intip Buku Teratas (Peek)") Untuk menampilkan menu melihat buku teratas.
- print("4. Cetak Semua Buku (Display)") Untuk menampilkan menu melihat semua buku.
- print("5. Keluar") Untuk menampilkan menu keluar program.
- try: Untuk mencoba menjalankan input dengan aman.
- pilih = int(input("Pilih menu: ")) Untuk meminta pengguna memasukkan nomor menu lalu mengubahnya menjadi angka.
- except ValueError: Baris ini akan berjalan jika pengguna salah input selain angka.
- print("Error: Input harus angka!") Untuk menampilkan pesan kesalahan input.
- continue Untuk mengulang kembali ke menu awal.
- if pilih == 1: Jika pengguna memilih menu 1.
- val = input("Ketik judul buku: ") Untuk meminta pengguna memasukkan judul buku.
- stack.push(val) Untuk menambahkan buku ke tumpukan.
- elif pilih == 2: Jika pengguna memilih menu 2.
- stack.pop() Untuk mengambil buku paling atas.
- elif pilih == 3: Jika pengguna memilih menu 3.
- stack.peek() Untuk melihat buku paling atas.
- elif pilih == 4: Jika pengguna memilih menu 4.
- stack.display() Untuk menampilkan semua buku.
- elif pilih == 5: Jika pengguna memilih menu 5.
-print("Program selesai.") Untuk menampilkan pesan bahwa program selesai.
- else: Jika pengguna memasukkan angka selain 1–5.
- print("Pilihan tidak ada.") Untuk menampilkan pesan bahwa menu tidak tersedia.
- if__name__ == "__main __":  Baris ini akan mengecek apakah file dijalankan langsung.
- main() Untuk menjalankan fungsi utama program.

**OUTPUT**
<img width="1010" height="953" alt="Screenshot 2026-05-16 194838" src="https://github.com/user-attachments/assets/9027b295-4885-4445-9719-04a21ea770c2" />
Penjelasan
Program pertama menampilkan menu tumpukan buku yang isinya pilihan untuk menambah buku, mengambil buku, melihat buku teratas, menampilkan semua buku, dan keluar program. Setelah menu muncul, pengguna memilih menu 1 untuk menambahkan buku ke dalam tumpukan. Judul buku adalah "indonesia", lalu program memberi pesan kalau buku berhasil ditaruh di paling atas. Karena sebelumnya masih kosong, buku "indonesia" jadi buku pertama yang ada di stack.
Menu kemudian muncul lagi dan pengguna kembali memilih menu 1. Kali ini pengguna memasukkan judul buku "manusia". Buku tersebut disimpan di atas buku "indonesia" sehingga sekarang posisi paling atas adalah buku "manusia".
Setelah itu pengguna memilih menu 2 untuk mengambil buku dari tumpukan. Karena stack memakai sistem LIFO (Last In First Out), buku yang terakhir dimasukkan akan keluar lebih dulu. Jadi buku "manusia" yang diambil, sedangkan buku "indonesia" masih tetap ada di dalam stack. Terakhir pengguna memilih menu 5 untuk keluar dari program. Program lalu menampilkan tulisan "Program selesai." yang menandakan program sudah berhenti dijalankan.

**LINK YOUTUBE:** https://youtu.be/EC-z7x9-6yo?si=umq8FiEiY0fVAo2-
