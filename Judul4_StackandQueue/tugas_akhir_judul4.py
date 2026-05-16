class StackArray:
    def __init__(self, max_size=5):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Gagal: Tumpukan sudah penuh, nanti roboh.")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"Buku '{x}' berhasil ditaruh di paling atas.")

    def pop(self):
        if self.is_empty():
            print("Gagal: Tidak ada buku di meja.")
            return
        print(f"Buku '{self.st[self.top_idx]}' diambil.")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Meja kosong.")
            return
        print(f"Buku teratas saat ini: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Meja kosong.")
            return
        print("Daftar buku dari atas ke bawah:")
        for i in range(self.top_idx, -1, -1):
            print(f"- {self.st[i]}")


def main():
    stack = StackArray()
    pilih = 0
    while pilih != 5:
        print("\nMENU TUMPUKAN BUKU")
        print("1. Taruh Buku (Push)")
        print("2. Ambil Buku (Pop)")
        print("3. Intip Buku Teratas (Peek)")
        print("4. Cetak Semua Buku (Display)")
        print("5. Keluar")
        
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Error: Input harus angka!")
            continue
            
        if pilih == 1:
            val = input("Ketik judul buku: ")
            stack.push(val)
        elif pilih == 2:
            stack.pop()
        elif pilih == 3:
            stack.peek()
        elif pilih == 4:
            stack.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak ada.")


if __name__ == "__main__":
    main()
