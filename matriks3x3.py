matriks_a = []
matriks_b = []
matriks_hasil = []

print("Masukkan elemen matriks A (3x3):")
for i in range(3):
    baris = []
    for j in range(3):
        elemen = int(input(f"Elemen [{i+1}][{j+1}]: "))
        baris.append(elemen)
    matriks_a.append(baris)

print("Masukkan elemen matriks B (3x3):")
for i in range(3):
    baris = []
    for j in range(3):
        elemen = int(input(f"Elemen [{i+1}][{j+1}]: "))
        baris.append(elemen)
    matriks_b.append(baris)

for i in range(3):
    baris_hasil = []
    for j in range(3):
        baris_hasil.append(matriks_a[i][j] + matriks_b[i][j])
    matriks_hasil.append(baris_hasil)

print("Hasil penjumlahan matriks A dan B:")
for baris in matriks_hasil:
    print(baris)
