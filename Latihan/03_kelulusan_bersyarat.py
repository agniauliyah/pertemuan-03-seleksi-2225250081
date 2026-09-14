# Input: nilai akhir dan persentase kehadiran
# Proses: mengecek nilai minimal 60 dan kehadiran minimal 80%
# Output: menampilkan status lulus atau belum lulus

nilai = float(input("Nilai akhir: "))

kehadiran = float(input("Kehadiran (%): "))

if nilai >= 60 and kehadiran >= 80:
    print("Lulus")
else:
    print("Belum lulus")