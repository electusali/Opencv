import time

class Hayvan:
    
     def __init__(self,yemek_durumu='Ac',enerji=3,isim='',beslenme='beslendi',barinma='barinma', hareket=["hızlı kosmak", "ucmak", "ısırmak"]):
        self.yemek_durumu=yemek_durumu
        self.beslenme=beslenme
        self.barinma=barinma
        self.hareket=hareket
        self.isim=isim
        self.enerji=enerji
     def yemek_ye(self):        
       if self.yemek_durumu=='Ac':
           a=['bekleyin..','yeniyor....','tamam doydu']
           print(f'{self.isim} yemek yiyor')
           time.sleep(2)
           for i in a:
              time.sleep(2) 
              print(i)
     def hayvan_cagirma(self):
         print('''Hangi hayvan cagirmak istiyorsun...
               1. AT
               2.KOPEK
               3.KEDI                                            
               ''')
         hayvan_getir=input('bir tane hayvan  seciniz..:')
         
         if hayvan_getir=='AT':
             at_komutlari=['at kisniyor...','ve engelleren atliyor.']
             self.hareket=['hızlı kosmak']
             print(f'{self.isim} hizli bir sekilde geliyor')
             print(f'{self.isim} mevcut enerji {self.enerji}')
             time.sleep(2)
             for liste in at_komutlari:
                 print(liste)
                 time.sleep(2)
                 print(f'mevcut enerji {self.enerji-1}')              
                 
class At(Hayvan):
    
      def __init__(self):    
          super().__init__()
          self.ses='Kisnedi'
          self.ayaklari='nal gosterdi'
          print(f'at  {self.ses} ve direk {self.ayaklari} gosterdi ')
                              
class kopek(Hayvan):
    
    def __init__(self):
      super().__init__()
      self.ses='Havladi'
      self.ayaklari='patileri '
      print(f'at  {self.ses} ve direk {self.ayaklari} gosterdi ')

class kedi(Hayvan):
    
      def __init__(self):
        super().__init__()
        self.ses='Miyavladi'
        self.ayaklari='patileri '
        print(f'at  {self.ses} ve direk {self.ayaklari} gosterdi ')                    

while True:
    print('''
          
Hangi hayvan  istiyorsun...
               1. AT
               2.KOPEK
               3.KEDI 
          
  
    ''')
    hayvan_ismi=input('Bir Hayvan ismi giriniz..:')   
    
    if hayvan_ismi=='AT':
        a=At()
        print(f' {a.isim}cagriliyor..')
        time.sleep(2)
        a.yurume='at yurudu'  
        a.barinma='ciflik'
        a.ses
        a.ayaklari
        a.yemek_ye()
        a.hayvan_cagirma()
        print(a.ayaklari)
        print(a.yurume)
        print(f'at barinak {a.barinma}')
        
    if hayvan_ismi=='KOPEK':
        print('hayvna cagri;')
    




    