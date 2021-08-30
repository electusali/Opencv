import datetime

class Arac():
    def __init__(self,stok):
        self.stok = stok
        self.now=0# zaman tutacak degisken
    
    def stok_goster(self):
        print(f'{self.stok} adet arc kiralama yapilabilir')
    def gunluk_kira(self,n):
         if n<=0:
            print('arac sayisi buyuk 0 olamali')
            return None
         elif  n>self.stok:
             print(f'kiralancak arac sayisi{self.stok}')
             return None
         else:
             self.now=datetime.datetime.now()
             print(f'{self.stok} adet arac {self.now} kiranlandi ')
             self.stok-=n
             return self.now
         
    def saatlik_kira(self):
        pass
    def iade_Alma(self,tur,kira_bilgisi):
        oto_saat_ucret=10
        oto_gun_ucret=200
        
        bis_saat_ucret=5
        bis_gun_ucret=80
        
        kiraZaman,kiratur,AracSayisi=kira_bilgisi
        fatura=0
        
        if tur=='Araba':
            if kiraZaman and kiratur and AracSayisi:
                self.stok+=AracSayisi
                now=datetime.datetime.now()
                fatura_suresi=now-kiraZaman
            if kiratur==1:
                fatura=fatura_suresi/3600*oto_saat_ucret*AracSayisi
            
    


class Oto(Arac):
    pass

class bisiklet(Arac):
    pass

class  Musteri():
    pass

