b =0
liste = []

anum = int(input("Kaç adet sayı girilecek? "))
for x in range(anum):
    num = int(input("Lütfen Sayı Giriniz: "))
    liste.append(num)

min_num = min(liste)
max_num = max(liste)


print("Min Değer: ",min_num)
print("Max Değer: ",max_num)






