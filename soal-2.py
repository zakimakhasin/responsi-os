import os

os.system("cls")
print("\t\tOperasi Round Robin")
print("-" * 45)
print("\n")
q = int(input("Jatah Waktu (Quantum Time) : "))
n = int(input("Jumlah Program yang di Jalankan : "))
p = {}
for i in range(n):
    nama = str(input("Nama Program ke " + str(i+1) + " : "))
    besar = int(input("Besar Program : "))
    print("")
    p[nama] = besar - q

print("Antrian Program : ", p)