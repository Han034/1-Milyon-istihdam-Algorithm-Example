session = True
print("Çıkmak için -1 Değerini Giriniz")
while(session):
    num = int(input("Lütfen Bir Sayı Giriniz: "))
    nums = num % 2
    if(nums==0):
        print("Sayı Çift")
    elif(num==-1):
        print("Güle güle")
        session=False
    else:
        print("Sayı Tektir")

