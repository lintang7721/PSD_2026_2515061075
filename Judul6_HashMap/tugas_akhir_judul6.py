class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("\nIsi Hash Table (Separate Chaining):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key},{current.value}) -> ", end="")
                current = current.next
            print("NULL")


def main():
    hashmap = HashMapSeparateChaining()
    
    hashmap.insert(1, "B 1234 ABC")
    hashmap.insert(11, "D 9999 XYZ")
    hashmap.insert(21, "F 5678 DEF")
    hashmap.insert(2, "L 1122 SS")
    hashmap.display()

    print("\nIsi kode tiket parkir yang ingin dicari")
    tiket_cari = int(input("Nomor Tiket : "))
    hasil = hashmap.search(tiket_cari)
    
    if hasil is not None:
        print(f"\nTiket nomor {tiket_cari} DITEMUKAN!")
        print(f"-> Plat Nomor Kendaraan: {hasil.value}")
    else:
        print(f"\nTiket nomor {tiket_cari} TIDAK DITEMUKAN di sistem!")
        
    hashmap.remove_key(11)
    print("\nSetelah tiket 11 keluar (data dihapus):")
    hashmap.display()


if __name__ == "__main__":
    main()
