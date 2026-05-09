JUDUL PROGRAM: Sistem Manajemen Nilai Mahasiswa

DESKRIPSI SINGKAT:
Program manajemen nilai mahasiswa adalah sistem berbasis python yang dirancang untuk membantu mempermudah proses analisis data nilai mahasiswa dalam lingkup pendidikan. Dengan memanfaatkan algoritma sequential search, sistem mampu melakukan pengecekan menyeluruh terhadap data nilai yang tersimpan untuk menghitung kemunculan suatu nilai secara akurat.
Program ini sangat efektif untuk mengetahui persebaran nilai mahasiswa tanpa harus mengurutkan data nilai yang ada terlebih dahulu, namun walaupun data nilai tidak perlu diurutkan terlebih dahulu hasilnya tetap akurat. Program ini dapat menjadi alat bantu yang simpel namun dapat diandalkan untuk mendapatkan data statistik nilai mahasiswa.

SOURCE CODE
<img width="1009" height="907" alt="Screenshot 2026-05-09 124336" src="https://github.com/user-attachments/assets/951a1285-2139-4758-9462-8b0b40f756e5" />
Fungsi sequential_search yaitu proses pencarian
- def sequential_search(data, n, target): Baris ini membuat fungsi yaitu sequential search yang membutuhkan tiga parameter yaitu data, jumlah data dan target (nilai yang dicari).
- i = 0 Baris ini menunjukkan bawah indek dimulai dari indeks nol.
- counter = 0 Baris ini menyiapkan variabel counter, jika nilai dalam indeks sesuai dengan target yang dicari maka nilai counter akan bertambah.
- while i < n:  Baris ini menunjukkan bahwa program akan terus berulang selama nilai i belum sampai ke nilai terakhir yang ada pada list.
- if data[i] == target: Baris ini akan membandingkan apakah nilai pada indeks itu sama atau tidak dengan nilai target yang dicari.
- counter += 1  Jika nilai pada indeks tersebut cocok dengan target maka nilai counter otomatis akan bertambah  satu.
- i += 1  Baris ini memerintahkan program untuk mengecek ke nilai selanjutnya.
- return counter Kode ini akan memberitahu pengguna hasil akhir dan jumlah target yang ditemukan.

Fungsi main() untuk mengatur jalannya program dari awal sampai akhir.
- print("SISTEM MANAJEMEN DATA NILAI MAHASISWA")  Kode ini akan menampilkan judul program agar user mengetahui dengan menggunakan sistem apa.
- data = [50, 70, 80, 75, 80, 77, 90] kode ini akan menampilkan daftar nilai mahasiswa yang sudah disimpan oleh sistem.
- n = len(data)  Kode ini akan memerintahkan sistem untuk menghitung jumlah nilai yang ada di dalam list tersebut.
- while True:  Merupakan sebuah perulangan yang bertujuan apabila pengguna saah memasukkan input maka program ini tidak langsung mati.
- try:  dan  except ValueError:  Da kode ini merupakan sistem pengaman, jadi jika pengguna salah memasukkan input maka kode ini akan menangkap eror tersebut dan memberikan peringatan
- target = int(input("Masukkan nilai...")) Baris ini akan meminta user untuk menginputkan nilai yang diinginkan untuk dijadikan target pencarian.
- except ValueError untuk menangkap eror dan memberikan peringatan
- print(“input salah, masukkan nilai yang benar!”) baris ini akan menampilkan peringatan kepada pengguna apabila pengguna salah menginputkan nilai.
- break Kode ini akan berjalan apabila pengguna sudah menginputkan nilai yang benar.
- counter = sequential_search(data, n, target)  Baris ini akan memanggil fungsi pencarian untuk memulai pengecekan terhadap data.
- if counter > 0:  Baris ini untuk mengecek apakah target yang dicari itu fitemukan atau tidak.
- print(f"Hasil: Nilai {target} ditemukan pada {counter} mahasiswa.")  kalau nilai target ditemukan maka program akan menampilkan output berapa kali target tersebut muncul.
- else Jika nilai counter = 0 atau target tidak ditemukan maka program akan menampilkan output yangberbeda.
- print(f"Hasil: Nilai {target} tidak ditemukan dalam database") Jika counter = 0 maka program akan menampilkan output Nilai… tidak ditemukan dalam database.

Fungsi eksekusi program
- if __name__ == "__main__":  memastikan bahwa file ini merupakan sebuah proram utama yang harus dijalankan.
- main()  Fungsi mulai untuk menjalankan semua rangkaian kode yang ada.


OUTPUT:
<img width="716" height="275" alt="Screenshot 2026-05-09 131658" src="https://github.com/user-attachments/assets/8025b2d1-de0b-4ecd-a13a-a592343ed6f3" />
Penjelasan:
- SISTEM MANAJEMEN DATA NILAI MAHASISWA  adalah judul dari program tersebut.
- List Nilai di Database: [50, 70, 80, 75, 80, 77, 90]  Program menampilkan isi dari daftar nilai yang tersimpan agar user tahu data apa saja yang dapat dicari.
- Masukkan nilai yang ingin dicari frekuensinya: 80  Pada bagian ini program meminta pengguna untuk menginputkan nilai yang ingin dicari kemudian dicek berapa kali kemunculan nilai tersebut, dan pengguna menginputkan nilai 80
- Hasil: Nilai 80 ditemukan pada 2 mahasiswa Merupakan hasil akhir dari program Sistem Manajemen Data Nilai Mahasiswa. Berdasarkan rumus yang ada program menemukan nilai 80 sebanyak 2 kali oleh karena ini output yang ditampilkan adalah sebagai berikut “Hasil: Nilai 80 ditemukan pada 2 mahasiswa. “.

LINK YOUTUBE:https://youtu.be/5KKFYo6ENqg?si=5tgIq2U3P81XSl8A
