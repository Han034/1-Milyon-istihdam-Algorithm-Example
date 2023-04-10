
numb = int(input("Lütfen ilk indeks için bir sayı giriniz: "))
nums = int(input("Lütfen son indeks için bir sayı giriniz: "))
sumt =0
sumc =0

for i in range(numb,nums):
    if(i%2==0):
        sumc+=i
    else:
        sumt+=i

print("Tek Sayıların Toplamı: ",sumt)
print("Çift Sayıların Toplamı: ",sumc)


