session = True
sum =0
while(session):
    num = int(input("Lütfen toplanacak sayıyı giriniz: "))
    if(num==0):
        session = False
        print("Toplam: ",sum)
    else:
        sum = sum + num
        print("Toplam: ",sum)