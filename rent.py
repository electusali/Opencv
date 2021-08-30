import datetime

class Arac():
    """
    Arac kiralama Parent sınıf
    """
    def __init__(self,stok):
        self.stok=stok
        self.now=0  #kiralama esnasındaki zamanı tutacagımız değişken
       
        
    
    def stokGoster(self):
        print("{} adet araç kiralanabilir".format(self.stok))
        return self.stok
    
    def gunlukKira(self,n):
        if n<=0:
            print("Araç sayısı 0 dan büyük olmalı")
            return None
        elif n>self.stok:
            print ("kiralanabilecek max araç sayısı= ",self.stok)
            return None
        else:
            self.now=datetime.datetime.now()
            print("{} adet araç {}  saatinde kiralandı".format(self.stok,self.now.hour))
            self.stok -=n
            return self.now
            
    
    def saatlikKira(self,n):
        if n<=0:
            print("Araç sayısı 0 dan büyük olmalı")
            return None
        elif n>self.stok:
            print ("kiralanabilecek max araç sayısı= ",self.stok)
            return None
        else:
            self.now=datetime.datetime.now()
            print("{} adet araç {}  saatinde kiralandı".format(self.stok,self.now.hour))
            self.stok -=n
            return self.now
            
    
    def iadeAl(self,tur,kiraOzet):
        oto_saat_ucreti=10
        oto_gun_ucreti=200
        bis_saat_ucreti=5
        bis_gün_ucreti=80
        
        kiraZamani,kiraTur,aracSayisi=kiraOzet #◘önemli *******
        fatura=0
        
        if tur=="araba":
            if kiraZamani and kiraTur and aracSayisi:
                self.stok+=aracSayisi
                now=datetime.datetime.now()
                fat_suresi=now-kiraZamani
        
            if kiraTur==1:  #saatlik kira
                fatura=fat_suresi/3600*oto_saat_ucreti*aracSayisi
                
                
        

class oto(Arac):
    """
    Otomobil Kiralama sınıfı **child
    """
    pass

class bisiklet(Arac):
    """
    Bisiklet Kiralama sınıfı **child
    """
    pass

class Musteri():
    """
    Musteri Sınıfı   **parent
    """
    pass