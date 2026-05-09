def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter

def main():
    print("SISTEM MANAJEMEN DATA NILAI MAHASISWA")
    
    data = [50, 70, 80, 75, 80, 77, 90]
    n = len(data)
    print(f"List Nilai di Database: {data}")
    
    while True:
        try:
            target = int(input("Masukkan nilai yang ingin dicari frekuensinya: "))
            break
        except ValueError:
            print("Input salah, silakan masukkan angka nilai yang bener!")
            
    counter = sequential_search(data, n, target)
    
    if counter > 0:
        print(f"Hasil: Nilai {target} ditemukan pada {counter} mahasiswa.")
    else:
        print(f"Hasil: Nilai {target} tidak ditemukan dalam database.")


if __name__ == "__main__":
    main()
