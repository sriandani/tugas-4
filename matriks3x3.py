def input_matrix(order):
    matrix = []
    for i in range(order):
        row = list(map(int, input(f"Masukkan elemen baris {i + 1} (pisahkan dengan spasi): ").split()))
        matrix.append(row)
    return matrix

def multiply_matrices(A, B):
    order = len(A)
    # Inisialisasi matriks hasil
    C = [[0 for _ in range(order)] for _ in range(order)]
    
    for i in range(order):
        for j in range(order):
            for k in range(order):
                C[i][j] += A[i][k] * B[k][j]
    return C

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

order = 3
print("Masukkan matriks A:")
A = input_matrix(order)
print("Masukkan matriks B:")
B = input_matrix(order)

if len(A[0]) != len(B):
    print("Matriks tidak dapat dikalikan.")
else:
    C = multiply_matrices(A, B)
    print("Hasil Perkalian Matriks:")
    print_matrix(C)
