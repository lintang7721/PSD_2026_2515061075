JUDUL PROGRAM: Program Kamus Digital (BST)

DESKRIPSI SINGKAT:
Program ini adalah sebuah aplikasi Kamus Digital sederhana yang dibuat menggunakan struktur data Binary Search Tree (BST) atau Pohon Pencarian Biner. BST digunakan untuk menyimpan data kata secara terurut sesuai alfabet agar proses pencarian menjadi lebih cepat. Ketika pengguna menambahkan kata baru, program akan membandingkan kata tersebut dengan kata yang sudah ada di dalam pohon. Jika urutannya lebih kecil, maka data akan masuk ke cabang kiri, sedangkan jika lebih besar akan ditempatkan di cabang kanan. Dengan metode seperti ini, program tidak perlu memeriksa seluruh data satu per satu saat mencari kata karena sistem langsung mengarah ke posisi yang sesuai.
Terdapat fitur traversal seperti Inorder, Preorder, dan Postorder yang digunakan untuk menampilkan data dengan urut
an berbeda. Traversal Inorder berfungsi menampilkan kata secara berurutan dari A sampai Z. Selain itu, program juga dapat mencari kata paling awal dan paling akhir berdasarkan alfabet, menghitung jumlah seluruh kata yang tersimpan, serta menggabungkan semua kata menjadi satu teks. Semua fitur dijalankan melalui menu berbasis teks sehingga pengguna bisa menggunakan program dengan lebih mudah dan terstruktur.

SOURCE CODE:
<img width="1039" height="912" alt="Screenshot 2026-05-23 171351" src="https://github.com/user-attachments/assets/01df251d-0a50-48cd-989e-9dd35406db41" />
<img width="1030" height="877" alt="Screenshot 2026-05-23 171413" src="https://github.com/user-attachments/assets/e7434e9d-d2e3-4143-816e-ab42643fdc23" />
<img width="1010" height="868" alt="Screenshot 2026-05-23 171428" src="https://github.com/user-attachments/assets/12834d40-6e06-4cde-9004-36f3547f08c5" />
<img width="1017" height="856" alt="Screenshot 2026-05-23 171439" src="https://github.com/user-attachments/assets/7970d1a2-f52f-4f47-8606-5162bf57e792" />
<img width="1042" height="861" alt="Screenshot 2026-05-23 171453" src="https://github.com/user-attachments/assets/75e14f35-8f85-4619-8bc4-6f0d1f3538d0" />
<img width="847" height="253" alt="Screenshot 2026-05-23 171503" src="https://github.com/user-attachments/assets/74e1d74d-6fb4-4329-82b4-2ebf99b65204" />

Penjelasan:
Class node
- class Node: Baris ini membuat sebuah class bernama Node. Class ini berfungsi sebagai blueprint untuk membuat setiap node pada Binary Search Tree. Dalam BST, setiap node digunakan untuk menyimpan satu data kata dan hubungan ke node lainnya.
- def __init__(self, key): Baris ini fungsi otomatis yang dijalankan ketika sebuah object Node baru dibuat. Parameter key digunakan untuk menerima data kata yang akan disimpan di dalam node.
- self.key = key Baris ini digunakan untuk menyimpan data kata yang diterima dari parameter key ke dalam variabel milik object node tersebut.
- self.left = None Baris ini digunakan untuk membuat cabang kiri node. Nilainya diatur None karena pada awal pembuatan node belum ada node lain yang terhubung di sebelah kiri.
- self.right = None Baris ini digunakan untuk membuat cabang kanan node. Sama seperti cabang kiri, nilainya masih kosong karena belum ada hubungan ke node lain.
  
Class BST dasar
-class BSTDasar: Baris ini digunakan untuk membuat class utama bernama BSTDasar. Class ini bertugas mengatur seluruh proses pada Binary Search Tree.
- def __init__(self): Fungsi otomatis ini akan dijalankan saat object BST dibuat pertama kali.
- self.root = None Baris ini digunakan untuk membuat root atau akar pohon BST. Nilainya masih None karena BST masih kosong dan belum memiliki data.
  
Fungsi Insert
- def insert_node(self, root, key): Fungsi ini merupakan fungsi rekursif yang digunakan untuk mencari posisi yang tepat saat menambahkan kata baru ke dalam BST.
- if root is None: Baris ini untuk memeriksa apakah posisi node saat ini kosong atau belum memiliki data.
- return Node(key) Jika posisi kosong, maka program membuat node baru menggunakan class Node.
- if key < root.key: Baris ini digunakan untuk membandingkan urutan alfabet antara kata baru dengan kata pada node saat ini. Jika kata baru lebih kecil secara alfabet, maka data akan diarahkan ke kiri.
- root.left = self.insert_node(root.left, key) Program akan memanggil fungsi insert_node kembali secara rekursif untuk mencari posisi kosong di cabang kiri.
- elif key > root.key: Baris ini untuk memeriksa apakah kata baru lebih besar dibanding node saat ini.
- root.right = self.insert_node(root.right, key) Jika kata lebih besar, program akan bergerak ke cabang kanan.
- return root Baris ini digunakan untuk mengembalikan node saat ini agar hubungan antar node tetap tersimpan dengan benar.
- def insert(self, key): Fungsi utama yang dipanggil pengguna untuk menambahkan kata baru ke BST.
- self.root = self.insert_node(self.root, key) Program memulai proses insert dari root BST lalu menjalankan fungsi rekursif insert_node.
  
Fungsi Search
- def search_node(self, root, key): Fungsi rekursif yang digunakan untuk mencari apakah sebuah kata ada di dalam BST atau tidak.
- if root is None: Baris ini untuk memeriksa apakah pencarian sudah mencapai node kosong.
- return False Jika node kosong, berarti kata tidak ditemukan sehingga fungsi mengembalikan nilai False.
- if root.key == key: Baris ini akan membandingkan apakah kata pada node saat ini sama dengan kata yang dicari.
- return True Jika sama, berarti kata berhasil ditemukan sehingga fungsi mengembalikan nilai True.
- if key < root.key: Baris ini memeriksa apakah kata yang dicari lebih kecil dari node saat ini.
- return self.search_node(root.left, key) Jika lebih kecil, pencarian dilanjutkan ke cabang kiri BST.
- return self.search_node(root.right, key) Jika tidak lebih kecil, pencarian dilanjutkan ke cabang kanan BST.
- def search(self, key): Fungsi utama untuk melakukan pencarian kata.
- return self.search_node(self.root, key) Program memulai pencarian dari root BST.
  
Fungsi Traversal
Traversal Inorder
- def inorder(self, root): Fungsi ini digunakan untuk menampilkan data BST menggunakan metode Inorder.
- if root is None:Akan memeriksa apakah node kosong.
- return Jika kosong maka fungsi dihentikan.
- self.inorder(root.left) Program menelusuri seluruh cabang kiri terlebih dahulu.
- print(root.key, end=" | ") Setelah kiri selesai, program mencetak isi node saat ini.
- self.inorder(root.right)Kemudian program melanjutkan traversal ke cabang kanan.
  
Traversal Preorder
- def preorder(self, root): Fungsi traversal dengan urutan node, kiri, lalu kanan.
- if root is None: Untuk memeriksa apakah node kosong.
- return Untuk menghentikan fungsi jika node kosong.
- print(root.key, end=" | ") Program akan mencetak node saat ini terlebih dahulu.
- self.preorder(root.left) Program akan melanjutkan traversal ke kiri.
- self.preorder(root.right) Pada baris ini traversal dilanjutkan ke kanan.
  
Traversal Postorder
- def postorder(self, root): Fungsi traversal dengan urutan kiri, kanan, lalu node.
- if root is None: Untuk memeriksa apakah node kosong.
- return Untuk menghentikan fungsi jika kosong.
- self.postorder(root.left) Pada baris ini program akan enelusuri cabang kiri terlebih dahulu.
- self.postorder(root.right) Kemudian menelusuri cabang kanan.
- print(root.key, end=" | ") Node dicetak paling akhir setelah semua cabang selesai diproses.
  
Fungsi Statistik
Fungsi Find Min
- def find_min(self, root): Fungsi ini digunakan untuk mencari kata paling awal berdasarkan alfabet.
- if root is None: Untuk memeriksa apakah BST kosong.
- return -1 Jika kosong, fungsi mengembalikan nilai -1.
- current = root Untuk membuat variabel sementara untuk menelusuri BST dimulai dari root.
- while current.left is not None: Selama masih ada cabang kiri, program akan terus bergerak ke kiri.
- current = current.left Untuk memindahkan posisi penelusuran ke node kiri berikutnya.
- return current.key Mengembalikan kata paling kecil yang berada di ujung kiri BST.
  
Fungsi Find Max
- def find_max(self, root): Fungsi ini digunakan untuk mencari kata paling akhir berdasarkan alfabet.
- if root is None: Untuk memeriksa apakah BST kosong.
- return -1 Jika kosong maka mengembalikan -1.
- current = root Untuk membuat variabel sementara dimulai dari root.
- while current.right is not None: Selama masih ada cabang kanan, program terus bergerak ke kanan.
- current = current.right Memindahkan posisi penelusuran ke node kanan berikutnya.
- return current.key Mengembalikan kata paling besar yang berada di ujung kanan BST.
  
Fungsi Count Nodes
- def count_nodes(self, root): Fungsi ini digunakan untuk menghitung jumlah seluruh node dalam BST.
- if root is None: Untuk memeriksa apakah node kosong.
- return 0 Jika kosong maka nilainya 0.
- return 1 + self.count_nodes(root.left) + self.count_nodes(root.right) Untuk menghitung jumlah node dengan rumus: 1 untuk node saat ini kemudian ditambah jumlah node di kiri lalu ditambah jumlah node di kanan
  
Fungsi Sum Nodes
- def sum_nodes(self, root): Fungsi ini digunakan untuk menggabungkan semua kata menjadi satu kalimat panjang.
- if root is None: Untuk memeriksa apakah node kosong.
- return "" Jika kosong maka mengembalikan string kosong.
- return root.key + " " + self.sum_nodes(root.left) + " " + self.sum_nodes(root.right) Untuk menggabungkan kata pada node sekarang dengan seluruh kata di cabang kiri dan kanan.

Fungsi Main
- def main(): Fungsi utama sebagai pusat pengendali seluruh program.
- bst = BSTDasar() Membuat object BST baru bernama bst.
- pilih = 0 Membuat variabel untuk menyimpan pilihan menu pengguna.
- while pilih != 10: Pada baris ini program akan terus berjalan selama pengguna belum memilih menu keluar.
- print("\n=== KAMUS DIGITAL (BST) ===") Menampilkan judul program.
- print("1. Tambah Kata (Insert)") Menampilkan menu tambah kata.
- print("2. Cari Kata (Search)") Menampilkan menu pencarian kata.
- print("3. Cetak Urutan Alfabet (Inorder)") Menampilkan menu traversal inorder.
- print("4. Preorder Kamus") Menampilkan menu preorder.
- print("5. Postorder Kamus") Untuk menampilkan menu postorder.
- print("6. Kata Pertama Secara Alfabet (Min)") Menampilkan menu mencari kata pertama.
- print("7. Kata Terakhir Secara Alfabet (Max)") Menampilkan menu mencari kata terakhir.
- print("8. Hitung Total Kata (Count nodes)") Baris ini menampilkan menu menghitung jumlah kata.
- print("9. Gabungkan Semua Kata (Sum nodes)") Baris ini menampilkan menu menggabungkan kata.
- print("10. Keluar") Menampilkan menu keluar program.
- try: Digunakan untuk mengamankan program dari kesalahan input.
- pilih = int(input("Pilih: ")) Meminta pengguna memasukkan angka menu lalu mengubahnya menjadi integer.
- except ValueError: Menangkap error jika pengguna memasukkan huruf atau simbol selain angka.
- print("Input tidak valid!") Menampilkan pesan kesalahan.
- continue Mengulang kembali ke menu utama.
- if pilih == 1: Jika pengguna memilih menu tambah kata.
- x = input("Masukkan kata baru: ").strip().lower() Menerima input kata, menghapus spasi berlebih, dan mengubah huruf menjadi kecil semua.
- if x: Baris ini akan memeriksa apakah input tidak kosong.
- bst.insert(x)Memasukkan kata ke BST.
- print(f"Kata '{x}' berhasil dimasukkan ke kamus.") Baris ini menampilkan pesan sukses.
- else: Jika input kosong.
- print("Kata tidak boleh kosong!") Maka program akan menampilkan peringatan.
- elif pilih == 2: Jika pengguna memilih menu pencarian kata.
- x = input("Cari kata: ").strip().lower() Baris ini akan menerima input kata yang ingin dicari.
- if bst.search(x): Baris ini untuk menjalankan proses pencarian kata.
- print(f"Kata '{x}' Ditemukan di dalam kamus.") Untuk menampilkan pesan jika kata ditemukan.
- else: Jika kata tidak ditemukan.
- print(f"Kata '{x}' Tidak ditemukan.") Maka program akan menampilkan pesan bahwa kata tidak ada di kamus.
- elif pilih == 3: Jika pengguna memilih menu nomor 3 untuk melihat semua kata secara urut alfabet.
- print("Daftar Kata Urut Alfabet (Inorder): ", end="") Program akan menampilkan judul output inorder.
- bst.inorder(bst.root) Program menjalankan traversal inorder untuk menampilkan kata dari A sampai Z.
- print() Digunakan untuk membuat baris baru agar tampilan lebih rapi.
- elif pilih == 4: Jika pengguna memilih menu nomor 4 untuk melihat traversal preorder.
- print("Preorder Kamus: ", end="") Program akan menampilkan judul preorder.
- bst.preorder(bst.root) Program menjalankan traversal preorder dengan urutan node utama, kiri, lalu kanan.
- print() Digunakan untuk membuat baris baru setelah output selesai.
- elif pilih == 5: Jika pengguna memilih menu nomor 5 untuk melihat traversal postorder.
- print("Postorder Kamus: ", end="") Program akan  menampilkan judul postorder.
- bst.postorder(bst.root) Program menjalankan traversal postorder dengan urutan kiri, kanan, lalu node utama.
- print() Digunakan untuk membuat baris baru agar output lebih rapi.
- elif pilih == 6: Jika pengguna memilih menu nomor 6 untuk mencari kata pertama berdasarkan alfabet.
- print(f"Kata Pertama (Min): {bst.find_min(bst.root)}") Program mencari kata paling awal pada BST lalu menampilkannya ke layar.
- elif pilih == 7: Jika pengguna memilih menu nomor 7 untuk mencari kata terakhir berdasarkan alfabet.
- print(f"Kata Terakhir (Max): {bst.find_max(bst.root)}") Program mencari kata paling akhir pada BST lalu menampilkannya.
- elif pilih == 8: Jika pengguna memilih menu nomor 8 untuk menghitung jumlah kata di dalam kamus.
- print(f"Total Kata di Kamus: {bst.count_nodes(bst.root)}") Program menghitung seluruh node pada BST lalu menampilkan total katanya.
- elif pilih == 9: Jika pengguna memilih menu nomor 9 untuk menggabungkan semua kata.
- print(f"Gabungan Kata: {bst.sum_nodes(bst.root).strip()}") Program akan menggabungkan seluruh kata menjadi satu kalimat lalu menampilkannya.
- strip() Digunakan untuk menghapus spasi kosong di awal atau akhir teks.
- elif pilih == 10: Jika pengguna memilih menu keluar program.
- print("Program kamus selesai.") Program akan menampilkan pesan bahwa program telah selesai dijalankan.
- else: Jika pengguna memasukkan angka yang tidak ada di menu.
- print("Pilihan tidak valid!") Program akan menampilkan pesan bahwa pilihan menu salah.
- if __name__ == "__main__": Baris ini akan mengecek apakah file dijalankan langsung.
- main() Untuk menjalankan fungsi utama program.

OUTPUT

<img width="924" height="976" alt="Screenshot 2026-05-23 171118" src="https://github.com/user-attachments/assets/07708f53-5113-4de1-8535-1f459d6508ea" />
<img width="1088" height="978" alt="Screenshot 2026-05-23 171131" src="https://github.com/user-attachments/assets/48271931-5f58-4bab-9f6f-1a519a906200" />

Penjelasan:
Saat program dijalankan, akan muncul menu utama Kamus Digital BST yang berisi daftar pilihan fitur. Pengguna bisa memilih menu dengan memasukkan angka sesuai kebutuhan. Output ini berfungsi sebagai tampilan utama agar pengguna lebih mudah menjalankan program.
Pilih: 1 artinya pengguna memilih menu untuk menambahkan kata baru ke dalam kamus. Masukkan kata baru: apel menunjukkan bahwa pengguna memasukkan kata “apel”.Setelah itu muncul tulisan Kata 'apel' berhasil dimasukkan ke kamus yang berarti data berhasil disimpan ke dalam program. Karena kata “apel” adalah data pertama yang dimasukkan, maka kata tersebut otomatis menjadi data utama atau root pada Binary Search Tree (BST).

Pilih: 1 berikutnya berarti pengguna kembali memilih menu tambah kata. Masukkan kata baru: mangga menunjukkan bahwa pengguna memasukkan kata “mangga”. Lalu muncul output Kata 'mangga' berhasil dimasukkan ke kamus, berarti kata berhasil ditambahkan ke BST. Program kemudian akan membandingkan kata “mangga” dengan “apel”. Karena huruf “m” lebih besar dari huruf “a”, maka “mangga” diletakkan di cabang kanan dari node “apel”.

Pilih: 3 berarti pengguna memilih menu untuk melihat daftar kata secara urut alfabet menggunakan traversal inorder. Output Daftar Kata Urut Alfabet (Inorder): apel | mangga | menunjukkan bahwa program berhasil menampilkan isi BST secara terurut dari A sampai Z. Kata “apel” tampil lebih dulu karena urutan alfabetnya lebih kecil dibanding “mangga”. 

Pilih: 7 berarti pengguna memilih menu untuk mencari kata terakhir berdasarkan urutan alfabet. Output Kata Terakhir (Max): mangga menunjukkan bahwa kata dengan urutan alfabet paling besar di BST adalah “mangga”. Hal ini karena pada BST, data paling besar selalu berada di bagian paling kanan pohon. Karena “mangga” berada di kanan “apel”, maka “mangga” menjadi nilai maksimum atau kata terakhir.

LINK YOUTUBE: https://youtu.be/geHHEsrxz0k?si=cteas8UBLINYgAAH


