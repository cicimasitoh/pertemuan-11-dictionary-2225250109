def cari_mahasiswa(data, nim):
    return data.get(nim)

def rata_rata_nilai(data):
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

# 1. Inisialisasi data mahasiswa (minimal 5 mahasiswa)
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# 2. Uji Pencarian (Tersedia & Tidak Tersedia)
nim_cari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)
if hasil is not None:
    print(f"Pencarian {nim_cari}: {hasil}")
else:
    print("Data tidak ditemukan")

# 3. Menambahkan mahasiswa baru (A006)
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

# 4. Memperbarui nilai mahasiswa tertentu (A002 menjadi 82)
data_mahasiswa["A002"]["nilai"] = 82

# 5. Menampilkan seluruh data menggunakan items() (Rekap)
print("\n--- REKAP SELURUH DATA MAHASISWA ---")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} | Data: {info}")

# 6. Menghitung dan menampilkan rata-rata nilai seluruh mahasiswa
rerata = rata_rata_nilai(data_mahasiswa)
print(f"\nRata-rata nilai kelas = {rerata:.2f}")