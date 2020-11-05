berat=int(input("Berat Badan Anda (Kg) :"))
tinggi=int(input("Tinggi Anda (Cm) :"))
tinggi2=float(tinggi/100)
BMI=berat/(tinggi2*tinggi2)
if BMI<18.5 :
    keterangan="Berat Badan Kurang"
elif BMI>=18.5 and BMI<=22.9 :
    keterangan="Berat Badan Normal"
elif BMI>=23 and BMI<=29.9 :
    keterangan="Berat Badan Berlebih"
elif BMI>30:
    keterangan="Obesitas"

print("Body Mass Index Anda =",format(BMI,'.2f'))
print(keterangan)

