# input nilai variable
a=input ("masukan nilai a : ")
b=input ("masukan nilai b : ")

# cetak nilai variable
print("Variable a = ",a)
print("Variable b = ",b)

#cetak hasil operasi kedua variable dengan string format
a=a
b=b
print(f"Hasil penggabungan {b}&{a}={b}{a}")

#konversi nilai variable
a=int(a)
b=int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b)%(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a,b)%(a/b))
