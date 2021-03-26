#Input Data Usia
print("Berapa usia kamu?")
usia = float(input("usiaku (tahun) ="))
#Batas Usia
min_usia = 21

gagal = "Maaf kamu belum bisa mendaftar karena usia belum mencukupi"
#Prosesseleksi
if usia <= min_usia:
    print(" ", gagal)
else:
    print("Apakah kamu dinyatakan lulus ujian kualifikasi? (Y/T)")
    hasil = input(" ")
    if hasil != "Y":
        print("Kamu tidak dapat mendaftar di kursus")
    else:
        print("Kamu dapat mendaftar kursus")
