#AÇIK KAYNAK WEB PROGRAMLAMA DERSİ ÖDEV
#DERS HOCASI : Dr.Selim ÖZDEN
#Öğrenci : 214526035 Cihat ESER

Liste1 = [ 'hitit', 2006 , 1, 'uni', 70.2 ] 
Liste2= [123, 'Corum']

#Soru1 : Liste1 de bulunan 2006 ve 1 değerli elemanları ekrana yazdıran python kodunu yazınız. (30 Puan)

print(Liste1[1])   
print(Liste1[2])  

#Soru3: Liste1 deki elemanları döngü kullanarak ekrana tersten yazdıran python kodu yazınız.  
# Çıktı şöyle olmalı: (40 Puan)
# 	70.2
# 	uni
# 	1
# 	2006
# 	hitit

for i in range(len(Liste1)-1, -1, -1):
    print(Liste1[i])

#Soru2: Liste1 ve Liste2 yi birleştirilmiş bir şekilde ekrana yazdıran python kodunu yazınız. (30 Puan)

print(Liste1 + Liste2)


    
    
  
    
    
    # 2. DENEME
    
Liste_a = [ 'hitit', 2006 , 1, 'uni', 70.2 ] 
Liste_b= [123, 'Corum']  # cihat


#soru1

ankara=[]
istanbul=[]

for x in Liste_a:
    if isinstance(x,int):
        istanbul.append(x)
    elif isinstance(x,str):
        ankara.append(x)
    else:
        pass

print(istanbul)


#Soru3

for tr in range(len(Liste_a)-1, -1, -1):
    print(Liste_a[tr])

#Soru2

Liste1.extend(Liste_b)
print(Liste_a)




