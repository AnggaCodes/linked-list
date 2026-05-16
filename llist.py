class Node:
    def __init__(self, nama, uts, uas):

        nilai_akhir = (uts + uas) / 2
        grade = "A" if nilai_akhir >= 80 else "B" if nilai_akhir >= 70 else "C" if nilai_akhir >= 60 else "D" if nilai_akhir >= 50 else "E"
        status = "Lulus (Sangat Memuaskan)" if grade == "A" else "Lulus (Baik)" if grade == "B" else "Lulus (Cukup)" if grade == "C" else "Lulus Bersyarat / Remedial" if grade == "D" else "Tidak Lulus"

        # Semua info dibungkus jadi satu di self.data
        self.data = {
            "nama": nama, "uts": uts, "uas": uas,
            "nilai_akhir": nilai_akhir, "grade": grade, "status": status
        }
        self.next = None # Tangan kanan (pointer) kosong di awal

class LinkedList:
    def __init__(self):
        self.head = None # Papan penunjuk awal 

    # 1. INSERT DEPAN
    def insert_depan(self, nama, uts, uas):
        baru = Node(nama, uts, uas)
        if self.head is None: # Cek list kosong 
            self.head = baru 
        else:
            baru.next = self.head # Orang baru pegang orang yang ditunjuk head
            self.head = baru # Head pindah nunjuk ke orang baru

    # 2. INSERT BELAKANG 
    def insert_belakang(self, nama, uts, uas):
        baru = Node(nama, uts, uas)
        if self.head is None: 
            self.head = baru 
            return
        temp = self.head
        while temp.next: # Traversal nyari ujung
            temp = temp.next 
        temp.next = baru # Sambungin di akhir

    # 3. FIND / CARI 
    def cari_mahasiswa(self, nama_target):
        temp = self.head # Mulai dari depan
        while temp: 
            if temp.data["nama"] == nama_target: # Cek kondisi target 
                return temp.data # Ditemukan 
            temp = temp.next 
        return None # Tidak ditemukan

    # 4. REMOVE DEPAN 
    def hapus_depan(self):
        if self.head is None: # Cek list kosong
            print("Gak ada yang dihapus, list kosong!")
            return
        hapus = self.head # Simpan node yang mau dihapus 
        self.head = self.head.next # Geser head ke orang berikutnya 
        del hapus # Hapus dari memori 

    # 5. TAMPILKAN / TRAVERSAL
    def tampilkan(self):
        temp = self.head
        if not temp: # Cek list kosong
            print("List masih kosong") 
            return
        print("\n======================= Data Nilai Mahasiswa =======================")
        while temp: # Selama ada orang
            d = temp.data
            print(f"Nama: {d['nama']} | Nilai_Akhir: {d['nilai_akhir']} | Grade: {d['grade']} | {d['status']}") 
            temp = temp.next # Pindah ke orang berikutnya

gas = LinkedList()
gas.insert_depan("Angga", 80, 80)
gas.insert_belakang("Abdul", 70, 75)
gas.insert_belakang("Satria", 70, 65)

gas.tampilkan()
hapus_depan = gas.hapus_depan()
print ("\nHapus data paling depan")

# Coba cari
hasil = gas.cari_mahasiswa("Abdul")
print(f"\nCari Data : {hasil}")