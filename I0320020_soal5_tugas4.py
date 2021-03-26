s = "Hey there! what should this string be?"
print(s, "\n")

#Panjang harusnya 20
s = s[:20]
print(s)
print("panjang dari s = %d" % len(s), "\n")

#Huruf pertama 'a' harusnya di index no 8
s = s.replace("there", "thera")
print(s)
print("Kemunculan a pertama = %d" % s.index("a"), "\n")

#Jumlah huruf a seharusnya 2
print("a muncul %d kali" % s.count("a"), "\n")

#Memotong string berdasarkan index
print("Lima karakter pertama adalah '%s'" % s[:5])  #Start to 5
print("Lima karakter berikutnya adalah '%s' " % s[5:10])  # 5 to 10
print("Karakter ketiga belas adalah '%s' " % s[12])   # 12
print("Karakter dengan indeks ganjil adalah '%s' " % s[1::2]) #(0-based indexing)
print("Lima karakter terakhir adalah '%s' " % s[-5:]) # 5th-from-last to end
print("\n")

#Konverikan ke upercase
print("String dalam huruf besar: '%s' " % s.upper())
print("\n")

#Konversi ke lowercase
print("String dalam huruf kecil: '%s' " % s.lower())
print("\n")

#Cek bagaimana string itu dimulai
s = s.replace("Hey", "Str")
print(s)
if s.startswith("Str"):
    print("String dimulai dengan 'Str'.Good!")

#Cek bagaimana string diakhiri
print("\n")
s = s.replace("shou", "ome!")
print(s)
if s.endswith("ome!"):
    print("String diakhiri dengan 'ome!'.Good!")

#Pisahkan string menjadi tiga string yang terpisah,
#masing-masing hanya berisi satu kata
print("\n")
print("Pisahkan kata-kata dari string tersebut: '%s' " % s.split(" "))