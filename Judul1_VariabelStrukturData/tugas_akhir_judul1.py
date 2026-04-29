class Node:
    def __init__(self, nama_pasien):
        self.data = nama_pasien
        self.next = None

class AntrianRumahSakit:
    def __init__(self):
        self.start = None
        self.rear  = None

    def create_new_node(self, nama):
        new_node = Node(nama)
        return new_node

    def insert_at_beg(self, new_node):
        if self.start is None:
            self.start = new_node
            self.rear = new_node
        else:
            new_node.next = self.start
            self.start = new_node

    def insert_at_end(self, new_node):
        if self.start is None:
            self.start = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def delete_node(self):
        if self.start is None:
            print("Antrian kosong!!!")
        else:
            pasien_dipanggil = self.start.data
            self.start = self.start.next
            print(f"Pasien {pasien_dipanggil} sedang dipanggil untuk berobat.")
            if self.start is None:
                self.rear = None

    def display(self):
        if self.start is None:
            print("(antrian kosong)")
            return
        current = self.start
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Selesai")


def main():
    antrian = AntrianRumahSakit()
    choice = 'y'

    while choice.lower() == 'y':
        nama_pasien = input("Nama pasien baru = ")

        print("Membuat data pasien baru")
        new_node = antrian.create_new_node(nama_pasien)

        if new_node is not None:
            print("Data pasien berhasil dibuat")
        else:
            print("Data pasien tidak dapat dibuat")
            break

        print("1. Prioritas (Depan)")
        print("2. Antrian biasa (Belakang)")

        try:
            insert_choice = int(input("Masukkan ke antrian mana? "))
        except ValueError:
            insert_choice = 2

        if insert_choice == 1:
            antrian.insert_at_beg(new_node)
            print("Pasien dimasukkan ke antrian prioritas")
        elif insert_choice == 2:
            antrian.insert_at_end(new_node)
            print("Pasien dimasukkan ke antrian biasa")
        else:
            print("Pilihan tidak valid, pasien dimasukkan ke antrian biasa")
            antrian.insert_at_end(new_node)

        print("Daftar Antrian: ", end="")
        antrian.display()

        choice = input("Mau menambah pasien baru? (y/n) ")

    while True:
        print("Daftar Antrian: ", end="")
        antrian.display()

        choice = input("Panggil pasien berikutnya? (y/n) ")

        if choice.lower() == 'y':
            antrian.delete_node()
        else:
            break

    print("Pelayanan rumah sakit selesai.")


if __name__ == "__main__":
    main()
