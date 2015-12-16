while True:
     try:
         iTree = int(raw_input("Dwse uyos Dentrou: "))
         break
     except ValueError:
         print "Oops!  That was no valid number.  Try again..."
while True:
     try:
         platos = int(raw_input("Dwse platos kormou: "))
         break
     except ValueError:
         print "Oops!  That was no valid number.  Try again..."
while True:
     try:
         ikormou = int(raw_input("Dwse uyos kormou: "))
         break
     except ValueError:
         print "Oops!  That was no valid number.  Try again..." 
         break
print "Dimiourgia Dentrou me:"
print "Yyos Dentrou : ", iTree
print "Platos kormou: ", platos
print "Yyos Kormou  : ", ikormou
print "Sinoliko Yyos: ", iTree+ikormou

star = '*' 
keno = ' ' 

z = iTree - 1
x = 1
i=0
while i<iTree:
  print(keno*z + star * x + keno*z)
  x=x+2
  z=z-1
  i=i+1
  
i=0 
j= ikormou
x=int((x-2)/2)
while i < ikormou:
       print(keno*x +star*platos + keno*x)
       i=i+1

    
   
    
  
