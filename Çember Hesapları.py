#Çevre Hesabı için => 2 x pi x r
#Çevre Alanı için => pi x r x r
pi = 3.14
r = int(input("r değerini giriniz: "))
def cevre(r,pi):
    sum = 2*pi*r
    sum= int(sum)
    print("Çemberin çevresi: ",sum)

def alan(r,pi):
    sum = pi*r*r
    print("Çemberin Alanı: ",sum)


cevre(r,pi)
alan(r,pi)