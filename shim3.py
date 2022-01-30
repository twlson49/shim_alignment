#!/usr/bin python3
print("""a=front ind, b=back ind, c=distance a to b, d=distance a to ff
e=distance ff to back foot """)

     
a = float(input('a '))
b = float(input('b '))
c = float(input('c '))
d = float(input('d '))
e = float(input('e '))
fs=((a+b)/c*d-a)/2
bs=((a+b)/c*(d+e)-a)/2
print('front shims = ', fs)
print('back shims = ', bs)


    
   
      

