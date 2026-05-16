# Program Menghitung Nilai Akhir dari UTS dan UAS

# Membuat list of dictionaries
data_mahasiswa = [
    {"nama": "Angga", "uts": 80, "uas": 80},
    {"nama": "Abdul", "uts": 70, "uas": 75},
    {"nama": "Satria", "uts": 70, "uas": 65}
]

# Menghitung Nilai Akhir dan Grade untuk setiap mahasiswa
for mhs in data_mahasiswa:
    nilai_akhir = (mhs['uts'] + mhs['uas']) / 2
    mhs['nilai_akhir'] = nilai_akhir
    
    # Logika Penentuan Grade (Skala Umum Kampus)
    if nilai_akhir >= 80:
        mhs['grade'] = "A"
        mhs['status'] = "Lulus (Sangat Memuaskan)"
    elif nilai_akhir >= 70:
        mhs['grade'] = "B"
        mhs['status'] = "Lulus (Baik)"
    elif nilai_akhir >= 60:
        mhs['grade'] = "C"
        mhs['status'] = "Lulus (Cukup)"
    elif nilai_akhir >= 50:
        mhs['grade'] = "D"
        mhs['status'] = "Lulus Bersyarat / Remedial"
    else:
        mhs['grade'] = "E"
        mhs['status'] = "Tidak Lulus"

# Menampilkan Hasil
print("\n======================= Data Nilai Mahasiswa =======================")
for mhs in data_mahasiswa:
    print(f"Nama: {mhs['nama']} | Nilai_Akhir: {mhs['nilai_akhir']} | Grade: {mhs['grade']} | {mhs['status']}")
hapus_depan = data_mahasiswa.pop(0)
print(f"\nHapus data paling depan")

print(f"\nCari Data : {data_mahasiswa[0]}")
