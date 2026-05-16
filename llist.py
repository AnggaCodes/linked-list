class Node:
    def __init__(self, nama, uts, uas):

        akhir = (uts + uas) / 2
        grade = "A" if akhir >= 80 else "B" if akhir >= 70 else "C" if akhir >= 60 else "D" if akhir >= 40 else "E"
        status = "Lulus" if grade in ["A", "B", "C"] else "Tidak Lulus"

        # Semua info dibungkus jadi satu di self.data [cite: 122]
        self.data = {
            "nama": nama, "uts": uts, "uas": uas,
            "akhir": akhir, "grade": grade, "status": status
        }
        self.next = None # Tangan kanan (pointer) kosong di awal [cite: 123, 124]

class LinkedList:
    def __init__(self):
        self.head = None # Papan penunjuk awal [cite: 131]

    # 1. INSERT DEPAN (Kelompok 1) [cite: 135]
    def insert_depan(self, nama, uts, uas):
        baru = Node(nama, uts, uas)
        if self.head is None: # Cek list kosong [cite: 137]
            self.head = baru 
        else:
            baru.next = self.head # Orang baru pegang orang yang ditunjuk head [cite: 140]
            self.head = baru # Head pindah nunjuk ke orang baru [cite: 141]

    # 2. INSERT BELAKANG (Kelompok 2) [cite: 149]
    def insert_belakang(self, nama, uts, uas):
        baru = Node(nama, uts, uas)
        if self.head is None: 
            self.head = baru 
            return
        temp = self.head
        while temp.next: # Traversal nyari ujung [cite: 156]
            temp = temp.next 
        temp.next = baru # Sambungin di akhir [cite: 158]

    # 3. FIND / CARI (Kelompok 2) 
    def cari_mahasiswa(self, nama_target):
        temp = self.head # Mulai dari depan [cite: 161]
        while temp: 
            if temp.data["nama"] == nama_target: # Cek kondisi target [cite: 163]
                return temp.data # Ditemukan [cite: 164]
            temp = temp.next 
        return None # Tidak ditemukan [cite: 167]

    # 4. REMOVE DEPAN (Kelompok 3) [cite: 174]
    def hapus_depan(self):
        if self.head is None: # Cek list kosong [cite: 176]
            print("Gak ada yang dihapus, list kosong!")
            return
        hapus = self.head # Simpan node yang mau dihapus [cite: 179]
        self.head = self.head.next # Geser head ke orang berikutnya 
        del hapus # Hapus dari memori [cite: 181]

    # 5. TAMPILKAN / TRAVERSAL (Kelompok 1-5 wajib bisa) [cite: 191]
    def tampilkan(self):
        temp = self.head
        if not temp: # Cek list kosong [cite: 132]
            print("List masih kosong") 
            return
        print("\n=========== Data Nilai Mahasiswa ===========")
        while temp: # Selama ada orang [cite: 193]
            d = temp.data
            print(f"Nama: {d['nama']} | Akhir: {d['akhir']} | Grade: {d['grade']} | {d['status']}") 
            temp = temp.next # Pindah ke orang berikutnya [cite: 195]

gas = LinkedList()
gas.insert_depan("Angga", 80, 80)
gas.insert_belakang("Budi", 70, 75)
gas.insert_belakang("Budi", 70, 75)
gas.tampilkan()

# Coba cari
hasil = gas.cari_mahasiswa("Angga")
print(f"\nHasil Cari: {hasil}")