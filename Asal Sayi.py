
num = int(input("Lütfen bir sayı giriniz: "))
if (num > 1):
    for x in range(2,num):
        if(num%x) == 0:
            print(num,"Asal Sayı Değildir.")
            break
    else :
        print("Bu sayı asal sayıdır.")
else:
    print(num,"Bu sayı asal değildir.")



