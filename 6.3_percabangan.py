# Buat aplikasi untuk menentukan apakah 1 buah bilangan
# yang diinputkan oleh user termasuk kedalam
# bilangan ganjil atau genap

bilangan=int(input("Masukkan sebuah bilangan :"))
if bilangan != 0 :
    if bilangan%2==0:
        print(bilangan,"Merupakan bilangan genap")
    else :
        print(bilangan,"Merupakan bilangan ganjil")
else :
    print("Anda menginputkan bilangan 0")