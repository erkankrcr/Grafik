import matplotlib.pyplot as plt
def Xeksen():
    eksen=[]
    index=1
    deger=""
    while(True):
        deger=(input(str(index)+".X Ekseni Değerini Giriniz Çıkış İçin 'c' Tuşunu Kullanınız : "))
        if(deger=="c"):
            print(eksen)
            break
        else:
            eksen.append(deger)
            index=index+1
    return eksen
def Yeksen():
    eksen=[]
    index=1
    deger=""
    while(True):
        deger=(input(str(index)+".Y Ekseni Değerini Giriniz Çıkış İçin 'c' Tuşunu Kullanınız : "))
        if(deger=="c"):
            print(eksen)
            break
        else:
            eksen.append(deger)
            index=index+1
    return eksen
Xekseni=Xeksen()
Yekseni=Yeksen()

plt.plot(Xekseni,Yekseni)
plt.xlabel('x ekseni')
plt.ylabel('y ekseni')
plt.show()