import os

os.system("cls")
print("-"*65)
ram = int(input("Kapasitas RAM (MBps) \t\t\t\t\t : "))
petabit = int(input("Total petabit \t\t\t\t\t\t : "))
kso = int(input("Kapasitas RAM yang di gunakan oleh Sistem Operasi (MBps) : "))
kp1 = int(input("Kapasitas RAM yang di gunakan oleh Program 1 (MBps) \t : "))
kp2 = int(input("Kapasitas RAM yang di gunakan oleh Program 2 (MBps) \t : "))


konversi = 1024
kapasitas_petabit = (ram/petabit)

jmlblok = ram/kapasitas_petabit
jmlblok1 = (kso+kp1+kp2)/kapasitas_petabit
jmlblok0 = jmlblok-jmlblok1

useram = kso + kp1 + kp2
avaram = ram - useram

print("-"*65)
print("\n")
print("-"*65)
print("\nKapasitas RAM\t\t\t : ",ram,"MBps")
print("Total Petabit\t\t\t : ",petabit)
print("Kapasitas per pertabit\t\t : ",kapasitas_petabit,"KBps")
print("Total RAM yang terpakai\t\t : ",useram,"MBps")
print("Total RAM yang tidak terpakai\t : ",avaram,"MBps")
print("\n")
print("Informasi kondisi peta bit")
print("Jumlah blok bernilai 1 : ",jmlblok1)
print("Jumlah blok bernilai 0 : ",jmlblok0)
print("-"*65)