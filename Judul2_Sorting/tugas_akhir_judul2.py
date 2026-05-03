def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah mahasiswa Teknik Elektro: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan IPK mahasiswa:")
    for i in range(n):
        while True:
            try:
                nilai = float(input(f"IPK mahasiswa ke-{i+1}: "))
                arr.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka (contoh: 3.75)!")
    
    print(f"Data IPK sebelum diurutkan: {arr}")
    bubble_sort(arr, n)
    
    print("Data IPK setelah diurutkan (Bubble Sort):", end=" ")
    for i in range(n):
        print(f"{arr[i]:.2f}", end=" ")
    print()


if __name__ == "__main__":
    main()
