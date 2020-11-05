nilaiAngka=int(input("Nilai Angka :"))

if nilaiAngka >85 and nilaiAngka <=100:
    nilaiHuruf='A'
elif nilaiAngka >75 and nilaiAngka <=85:
    nilaiHuruf='B'
elif nilaiAngka >50 and nilaiAngka <=75:
    nilaiHuruf='C'
elif nilaiAngka >40 and nilaiAngka <=50:
    nilaiHuruf='D'
else : nilaiHuruf='E'
print("\n")
print('Nilai Huruf :',nilaiHuruf)