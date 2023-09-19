# Fungsi untuk menghitung jumlah rangkaian
def calculateSeriesSum(n):
    sum = 0
    term = 2  # Suku pertama
    for i in range(n):
        sum += term
        term = term * 10 + 2  # Menghasilkan suku berikutnya
    return sum

# Jumlah Ketentuan
n = 5

# Menghitung jumlah rangkaian hingga n suku
seriesSum = calculateSeriesSum(n)

# Mencetak hasil
print(seriesSum)
