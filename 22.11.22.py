import math

d=input("uzraksti finiera malas garumu:")
def materialuAprekins(garums, platums, augstums, skaits):
        return garums*platums
    
x = float(input("garums (cm): "))
y = float(input("platums (cm): "))
z = float(input("augstums (cm):"))
e = int(input("skaits: "))
print("materiala aprekins",(x,y,z,e))

liste=x
print("liste daudzums",12*e,"pa",x,"cm")

sture=e*8
print("stures daudzums", sture)

finieris=e*6*x*y
print("finiera nepieciesams",finieris,"cm^2")



    
