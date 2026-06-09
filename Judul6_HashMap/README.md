JUDUL PROGRAM: Sistem E-Parking Menggunakan Struktur Data Hash Map Separate Chaining

DESKRIPSI SINGKAT:
Program ini adalah simulasi sistem Tempat Parkir Kendaraan Digital (E-Parking) menggunakan struktur data Hash Map Separate Chaining. Sistem ini mengelompokkan data kendaraan berdasarkan nomor tiket parkir untuk menyimpan plat nomornya. Jika terjadi benturan indeks (dua nomor tiket memiliki sisa bagi yang sama), data akan otomatis dirangkai menggunakan Linked List agar tidak saling menimpa.

Melalui sistem ini, pengguna dapat melakukan proses pencatatan kendaraan yang masuk, mencari informasi kendaraan berdasarkan nomor tiket, serta menghapus data kendaraan saat keluar dari area parkir. Dengan demikian, pengelolaan data parkir dapat dilakukan secara lebih terstruktur, cepat, dan efisien.


SOURCE CODE:
<img width="1065" height="851" alt="Screenshot 2026-06-09 192426" src="https://github.com/user-attachments/assets/be2993d9-0ff5-4ec8-b449-b57123eeb415" />
<img width="1059" height="651" alt="Screenshot 2026-06-09 192444" src="https://github.com/user-attachments/assets/5391606b-b052-4249-8c47-62cf348d5d37" />
<img width="1055" height="698" alt="Screenshot 2026-06-09 192454" src="https://github.com/user-attachments/assets/eec4c5db-18b8-47a1-89f3-e9c4c03072c3" />
Penjelasan:
Class Node yaitu Tempat penyimpanan (simpul) data untuk satu kendaraan yang berisi nomor karcis, nomor plat, dan pointer penyambung ke kendaraan berikutnya.
- Baris 1: Membuat cetakan objek simpul data kendaraan.
- Baris 2: Kasir/pembuat simpul yang menangkap data karcis dan plat nomor.
- Baris 3: Mengunci data nomor karcis di dalam simpul.
- Baris 4: Mengunci data plat nomor di dalam simpul.
- Baris 5: Menyediakan tali pengait ke simpul kendaraan di belakangnya (awal diset kosong/None).

Class HashMapseparateChainning sebagai pusat untuk mengatur semua operasi data
def init 
- Baris 6: Prosedur awal untuk mengalokasikan ruang penyimpanan utama dengan konfigurasi standar awal sebanyak 10 lajur loker.
- Baris 7: Menyimpan batasan tampung maksimal tabel (10 slot) ke dalam properti internal objek pengelola.
- Baris 8: Membuat array berisi entitas kosong sebanyak 10 slot sebagai tanda bahwa seluruh bilik server parkir masih bersih dan siap diisi.

def hash function
- Baris 9: Fungsi kalkulasi matematis yang berguna untuk mengubah nomor karcis numerik menjadi alamat indeks lokasi slot yang spesifik.
- Baris 10: Menghitung sisa hasil bagi dari nomor karcis terhadap ukuran tabel. Indeks yang keluar selalu berupa bilangan bulat positif dalam rentang 0-9.

def insert 
- Baris 11: Menyediakan metode untuk mendaftarkan dan merekam data kendaraan yang baru masuk ke area parkir.
- Baris 12: Memanggil fungsi pemetaan hash untuk mendeteksi di indeks slot mana karcis tersebut harus diletakkan.
- Baris 13: Menyiapkan variabel pelacak bernama current untuk memantau simpul pertama yang ada di posisi terdepan pada slot indeks tersebut.
- Baris 14: Menjalankan perulangan untuk menelusuri barisan rantai kendaraan pada lajur tersebut selama jalurnya mendeteksi adanya data.
- Baris 15: Menguji apakah nomor karcis yang akan didaftarkan ternyata sudah pernah disimpan sebelumnya di lajur tersebut.
- Baris 16: Jika nomor karcis terdeteksi ganda, sistem langsung memperbarui data plat nomor lama dengan data plat nomor yang baru masuk.
- Baris 17: Menghentikan fungsi penambahan secara paksa karena proses pembaruan data duplikat dianggap sudah selesai.
- Baris 18: Jika karcis pada simpul aktif saat ini tidak cocok, pelacak current digeser mundur satu langkah ke simpul di belakangnya untuk diperiksa kembali.
- Baris 19: Apabila penelusuran selesai dan membuktikan karcis belum terdaftar, sistem membuat satu objek simpul baru menggunakan cetakan Node.
- Baris 20: Menyambungkan next milik simpul baru tersebut ke objek simpul yang tadinya menempati urutan paling depan di lajur parkir.
- Baris 21: Memindahkan jangkar utama slot tabel untuk memegang simpul baru ini, sehingga data baru otomatis berada di posisi terdepan.

def search
- Baris 22: Menyediakan metode khusus untuk melacak lokasi dan mengambil data kendaraan berdasarkan nomor karcisnya saat akan keluar.
- Baris 23: Menghitung koordinat indeks slot lokasi memori tempat karcis tersebut disimpan berdasarkan nomor karcisnya.
- Baris 24: Mengarahkan penunjuk current untuk melihat simpul pembuka atau simpul terdepan di dalam indeks slot target.
- Baris 25: Menjalankan perulangan untuk memeriksa seluruh simpul kendaraan di lajur tersebut satu demi satu secara berurutan.
- Baris 26: Memvalidasi apakah nomor karcis pada simpul yang sedang ditunjuk identik dengan nomor karcis yang dicari oleh operator.
- Baris 27: Jika terbukti cocok, fungsi langsung mengembalikan seluruh objek simpul utuh kepada sistem pemanggil.
- Baris 28: Jika belum cocok, penunjuk digeser selangkah maju ke simpul berikutnya untuk dianalisis pada putaran selanjutnya.
- Baris 29: Jika pencarian sampai ke ujung rantai namun karcis tidak ditemukan, fungsi mengeluarkan sinyal kosong.

def remove key
- Baris 30: Menyediakan metode eliminasi untuk menghapus data administrasi kendaraan dari database ketika kendaraan selesai membayar dan keluar dari area parkir.
- Baris 31: Mencari koordinat indeks slot dari karcis yang hendak dihapus menggunakan kalkulasi fungsi hash.
- Baris 32: Mengarahkan pelacak current ke posisi simpul paling depan pada indeks slot yang dituju.
- Baris 33: Menyiapkan variabel bantuan bernama prev untuk merekam jejak simpul yang berada tepat di depan simpul current. Posisi awal disetel kosong.
- Baris 34: Melakukan penjelajahan berantai menyusuri satu per satu simpul yang ada di slot memori tersebut dari depan ke belakang.
- Baris 35: Memeriksa apakah nomor tiket pada objek simpul yang dipegang current saat ini adalah data kendaraan yang ingin dibuang.
- Baris 36: Mengevaluasi posisi; memeriksa apakah target yang akan dihapus kebetulan berada di urutan pertama.
- Baris 37: Jika berada di depan, sistem langsung menggeser kendali utama slot tabel ke simpul urutan kedua, sehingga simpul terdepan otomatis terlepas dan terhapus.
- Baris 38: Kondisi alternatif apabila objek yang akan dihapus berada di posisi tengah ataupun ujung belakang rantai.
- Baris 39: Mengaitkan pointer next milik simpul prev langsung melompati posisi current untuk menyambung ke simpul di belakang current, sehingga simpul current otomatis terputus dari jalur rantai.
- Baris 40: Keluar dari metode dan mengirimkan status logika True sebagai laporan bahwa penghapusan sukses dilakukan.
- Baris 41: Jika karcis belum cocok pada simpul aktif, posisi pengawas prev digeser maju menduduki posisi current saat ini sebelum perulangan berputar lagi.
- Baris 42: Menggeser pelacak utama current selangkah ke depan untuk memeriksa simpul berikutnya.
- Baris 43: Mengirimkan status logika False apabila penelusuran telah mencapai ujung baris namun karcis yang dimaksud tidak ada di sistem.

def display
- Baris 44: Fungsi kontrol visual untuk menampilkan kondisi mutakhir seluruh tangki memori server ke layar terminal hitam.
- Baris 45: Mencetak judul informasi tabel pada layar terminal.
- Baris 46: Melakukan perulangan dari angka 0 hingga 9 untuk mengabsen kondisi di tiap lajur indeks memori.
- Baris 47: Menuliskan nomor urut lajur indeks ke layar. 
- Baris 48: Menempatkan pointer current di simpul pertama pada baris indeks yang sedang diarsip.
- Baris 49: Melakukan perulangan intensif untuk memunculkan semua entri kendaraan yang saling terikat di baris indeks tersebut.
- Baris 50: Mencetak pasangan data nomor karcis beserta nomor plat kendaraan dalam tanda kurung.
- Baris 51: Menggeser pointer current ke simpul lanjutan di belakangnya agar datanya dapat diproses pada perulangan berikutnya.
- Baris 52: Apabila barisan simpul telah habis ditelusuri atau lajur memori tersebut memang kosong dari awal, program mencetak teks NULL sekaligus memerintahkan perpindahan baris baru ke bawah.

def main
- Baris 53: Fungsi induk utama yang mengendalikan seluruh skenario jalannya simulasi sistem parkir dari awal hingga akhir.
- Baris 54: Mengondisikan variabel hashmap sebagai penyimpanan parkir digital yang baru dibuat.
- Baris 55: Mendaftarkan kendaraan dengan tiket nomor 1.
- Baris 56: Mendaftarkan tiket nomor 11. Karena hasil modulo bernilai 1, terjadi collision. Tiket 11 ditautkan tepat di depan posisi tiket 1 pada lajur indeks 1.
- Baris 57: Mendaftarkan tiket nomor 21. Kembali terjadi tumpang tindih pada lajur indeks 1. Tiket 21 disisipkan pada urutan paling awal di lajur tersebut.
- Baris 58: Mendaftarkan tiket nomor 2. Karena hasil modulo bernilai 2, data ini disimpan secara mandiri pada lajur indeks 2.
- Baris 59: Memanggil fungsi visualisasi untuk memperlihatkan peta sebaran memori kendaraan awal di layar terminal.
- Baris 60: Menampilkan instruksi teks panduan bagi operator di layar terminal agar mengetahui langkah berikutnya.
- Baris 61: Menghentikan sementara alur program untuk menunggu operator mengetik nomor tiket yang dicari, lalu mengonversi input tersebut menjadi angka bulat di variabel barang.
- Baris 62: Menjalankan perintah pencarian terhadap nomor tiket di dalam variabel barang dan menampung objek simpul yang ditemukan ke variabel hasil.
- Baris 63: Menganalisis kondisi logika; jika variabel hasil terbukti memuat objek simpul yang valid
- Baris 64: Sistem langsung menggali data plat nomor dari dalam properti simpul (hasil.value) dan mencetaknya ke layar terminal berdampingan dengan variabel input.
- Baris 65: Kondisi percabangan alternatif apabila variabel hasil berstatus kosong
- Baris 66: Mencetak informasi penolakan ke terminal bahwa nomor karcis parkir tersebut tidak dikenali oleh sistem server.
- Baris 67: Mensimulasikan proses kendaraan keluar area parkir dengan memberikan instruksi penghapusan data karcis nomor 11 dari tabel memori.
- Baris 68: Menuliskan teks pemberitahuan pada terminal sebelum menampilkan rekam data kondisi memori yang paling baru.
- Baris 69: Mengeksekusi ulang fungsi cetak visualisasi untuk menunjukkan kondisi final memori server, sekaligus membuktikan bahwa identitas karcis 11 telah sepenuhnya lenyap dari tabel.
-Baris 70: Perintah pengaman khas Python untuk memastikan seluruh instruksi di dalam fungsi main() hanya diaktifkan apabila file skrip ini dieksekusi secara langsung, bukan saat dipanggil oleh file eksternal lain.
- Baris 71: Menginstruksikan Python untuk mulai memproses fungsi utama program.

OUTPUT

<img width="936" height="828" alt="Screenshot 2026-06-09 220050" src="https://github.com/user-attachments/assets/25c88b55-3114-498f-8808-bc0a319f5bc6" />

Penjelasan
Pada tampilan awal, sistem menampilkan isi hash table yang berisi data kendaraan yang telah tersimpan. Terlihat bahwa tiket nomor 1, 11, dan 21 berada pada indeks yang sama, yaitu indeks 1. Hal ini terjadi karena ketiga nomor tiket menghasilkan nilai hash yang sama sehingga terjadi collision. Untuk mengatasinya, sistem menyimpan data tersebut dalam bentuk linked list pada indeks yang sama. Sementara itu, tiket nomor 2 tersimpan pada indeks 2 karena memiliki hasil hash yang berbeda.

Ketika pengguna memasukkan nomor tiket 11, sistem langsung menuju indeks yang sesuai berdasarkan hasil perhitungan fungsi hash. Setelah melakukan penelusuran pada linked list di indeks tersebut, sistem berhasil menemukan data tiket nomor 11 dan menampilkan plat nomor kendaraan yang terkait, yaitu D 9999 XYZ.

Selanjutnya, program proses kendaraan keluar dari area parkir dengan menghapus data tiket nomor 11. Setelah proses penghapusan selesai, isi hash table ditampilkan kembali. Hasilnya menunjukkan bahwa data tiket nomor 11 sudah tidak ada lagi, sedangkan data tiket lainnya tetap tersimpan dengan baik. Hal ini membuktikan bahwa proses pencarian, penanganan collision, dan penghapusan data pada struktur Hash Map Separate Chaining telah berjalan sesuai dengan yang diharapkan.


LINK YOUTUBE: https://youtu.be/JwQDp2tI-Po?si=a4lNOGxwymGdNUa

