# Program Menghitung Nilai Akhir dari UTS dan UAS
print("=== Sistem Penilaian Mahasiswa ===")

nama = input("Nama Mahasiswa: ")
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))

# Menghitung Rata-rata
nilai_akhir = (uts + uas) / 2

# Logika Penentuan Grade (Skala Umum Kampus)
if nilai_akhir >= 80:
    grade = "A"
    status = "Lulus (Sangat Memuaskan)"
elif nilai_akhir >= 70:
    grade = "B"
    status = "Lulus (Baik)"
elif nilai_akhir >= 60:
    grade = "C"
    status = "Lulus (Cukup)"
elif nilai_akhir >= 50:
    grade = "D"
    status = "Lulus Bersyarat / Remedial"
else:
    grade = "E"
    status = "Tidak Lulus"

# Menampilkan Hasil
print("-" * 35)
print(f"Mahasiswa: {nama}")
print(f"Skor Akhir: {nilai_akhir}")
print(f"Grade: {grade}")
print(f"Status: {status}")
print("-" * 35)