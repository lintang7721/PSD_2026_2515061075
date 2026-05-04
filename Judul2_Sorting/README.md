Program Pengurutan Data IPK Mahasiswa Teknik Elektro Menggunakan Metode Bubble Sort

DESKRIPSI SINGKAT:
Program python ini digunakan untuk menginput data IPK Mahasiswa Teknik Elektro, kemudian mengurutkannya dari nilai IPK terkecil ke terbesar menggunakan metode Bubble Sort. Pengguna akan diminta untuk memasukkan jumlah mahasiswa terlebih dahulu, Kemudian memasukkan nilai IPK dari masing-masing mahasiswa tersebut. Setelah semua data dimasukkan, program akan memproses dan mengurutkan nilai IPK dari yang terkecil sampai terbesar.
Program ini memiliki pengecekan input agar data yang dimasukkan sesuai dan tidak terjadi kesalahan. Jika input tidak valid, program akan meminta pengguna untuk memasukkan data kembali. Setelah proses selesai maka program akan menampilkan data IPK sebelum diurutkan dan hasil data setelah diurutkan.

SOURCE CODE:
<img width="994" height="332" alt="Screenshot 2026-05-04 114657" src="https://github.com/user-attachments/assets/eb21a041-68fd-4a63-9473-5e7903f9f442" />
<img width="992" height="679" alt="Screenshot 2026-05-04 114726" src="https://github.com/user-attachments/assets/dc60b6b4-9262-4ca1-b217-c9a6153a9e9f" />
PENJELASAN:
Fungsi Tukar 
def tukar(arr,  i,  j): Baris ini mendeklarasikan fungsi bernama tukar yang akan menerima tiga parameter yaitu list yang akan dimanipulasi (arr) dan dua indeks posisi yang ingin ditukar (i dan j)
 temp = arr[i] Baris ini akan menyalin nilai indeks i ke variabel sementara bernama temp untuk mencegah hilangnya data saat indeks i ditimpa nilainya.
arr[i] = arr[j] Baris ini mengisi posisi pada indeks i dengan nilai yang diambil dari posisi indeks j
arr[j] = temp Baris ini akan mengisi posisi indeks j dengan nilai yang sebelumnya disimpan di variabel temp. hasil akhirnya adalah nilai pada indeks i dan j telah bertukar posisi

Fungsi Bubble Sort 
def bubble sort(arr, n): baris ini mendeklarasikan fungsi pengurutan yang menerima list data dan jumlah elemen di dalamnya (n).
for i in range(n - 1): Baris ini adalah perintah untuk mengulang seluruh proses pengecekan. Jika kita memiliki 3 data maka program akan melakukan pengecekan maksimal 2 kali untuk memastikan semua angka sudah berada di posisi yang benar.
for j in range(n - i - 1): Baris ini adalah memerintahkan program untuk mengecek satu persatu dari depan ke belakang. Bagian -i digunakan agar program bekerja lebih cepat dengan tidak mengecek angka-angka besar yang sudah rapi di bagian belakang.
if arr[j] > arr[j + 1]: Baris ini program akan membandingkan dua angka yang letaknya bersebelahan. program akan mengecek apakah angka di posisi saat ini lebih besar daripada angka di depannya.
tukar(arr, j, j + 1) Jika angka di sebelah kiri ternyata lebih besar, maka program akan menukar posisi kedua angka tersebut. Jadi, angka yang lebih besar akan terus bergeser ke sebelah kanan.

Fungsi Main 
def main(): Merupakan titik awal dimana program utama mulai dijalankan
try: Untuk mengecek apakah ada kesalahan input dari pengguna
n = int(input("Masukkan jumlah mahasiswa Teknik Elektro: ")) Program akan meminta pengguna untuk mengetik jumlah mahasiswa, lalu meyimpannya dalam bentuk angka bulat.
except ValueError: Baris ini akan menangkap kesalahan apabila pengguna tidak menginputkan angka bulat.
print("Input tidak valid!") pada baris ini program akan menampilkan pesan peringatan bahwa input yang dimasukkan salah.
return untuk menghentikan program sampai disitu saja karena jumlah mahasiswa yang diinputkan tidak jelas
arr = [] Membuat daftar kosong untuk menampung semua nilai IPK yang akan diinputkan
print("Masukkan IPK mahasiswa:") Program akan menampilkan instruksi kepada pengguna untuk mulai memasukkan data IPK
for i in range(n): Baris ini akan memulai pengulangan sebanyak jumlah mahasiswa (n) yang sudah ditentukan diawal.
while True: Baris ini adalah pintu gerbang program supaya tidak melanjutkan ke nilai IPK mahasiswa selanjutnya kalau nilai IPK yang diinputkan masih salah.
try: Untuk mengecek apakah ada kesalahan input dari pengguna
nilai = float(input(f"IPK mahasiswa ke-{i+1}: ")) Program akan meminta nilai IPk mahasiswa satu persatu dan disimpan sebagai angka desimal
arr.append(nilai) Nilai IPK yang sudah benar akan langsung dimasukkan ke dalam daftar penyimpanan
break Jika input sudah benar program akan keluar dari pintu gerbang ini dan melanjutkan ke data mahasiswa berikutnya
except ValueError: Jika pengguna menginputkan IPK bukan angka, program akan masuk ke sini 
print("Input tidak valid, silakan masukkan angka (contoh: 3.75)!") Baris ini akan memberikan peringatan agar pengguna memasukkan format angka yang benar.
print(f"Data IPK sebelum diurutkan: {arr}") Baris ini akan menampilkan daftar IPK sesuai urutan asli saat  baru diinputkan.
bubble_sort(arr, n) Baris ini akan memanggil perintah untuk mengurutkan daftar IPK dari terkecil ke terbesar.
print("Data IPK setelah diurutkan (Bubble Sort):", end=" ") Program menampilkan teks judul untuk hasil akhir.
 for i in range(n): Program mengambil satu persatu angka yang sudah rapi dari daftar data penyimpanan
print(f"{arr[i]:.2f}", end=" ") Program akan mencetak nilai IPK dengan format dua angka dibelakang program agar seragam.
print() Untuk membuat baris baru agar tampilan pada layar tidak berantakan.
if _name_ == "_main_": Untuk memastikan kode di bawahnya hanya berjalan jika file ini dibuka secara langsung
 main() Untuk menjalankan seluruh alur fungsi utama yang sudah dijelaskan di atas

