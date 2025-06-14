x=10
y=20
z=40
a=5

print("Given String x is:",x)
print("Given String y is:",y)	
print("Given String z is:",z)				
print("Given String a is:",a,"\n")	

			
#input-1:not((x<a and y>z) and a<=y) or z>=x
print("We are using < OP (x<a) :",x<a) 
print("We are using > OP (y>z) :",y>z) 
print("We are using <= OP (a<=y ) :",a<=y ) 
print("We are using >= OP (z>=x) :",z>=x) 
print("We are using and OP (x<a and y>z) :",x<a and y>z)
print("We are using and OP ((x<a and y>z) and a<=y) :",(x<a and y>z) and a<=y)
print("We are using not,and OP (not((x<a and y>z) and a<=y)) :",not((x<a and y>z) and a<=y))
print("Final Output not((x<a and y>z) and a<=y) or z>=x is:",not((x<a and y>z) and a<=y) or z>=x,"\n")


#input-2:not (y>x or z<a) and (a>=z or z>=y)
print("We are using > OP (y>x) :",y>x ) 
print("We are using < OP (z<a) :",z<a) 
print("We are using >= OP (a>=z) :",a>=z) 
print("We are using >= OP (z>=y) :",z>=y) 
print("We are using or OP (y>x or z<a) :",y>x or z<a)
print("We are using or OP (a>=z or z>=y) :",a>=z or z>=y)
print("We are using not,or OP (not (y>x or z<a)) :",not (y>x or z<a))
print("Final Output  (y>x or z<a) and (a>=z or z>=y) is:",not (y>x or z<a) and (a>=z or z>=y),"\n")

#input-3:not x<a and (y>z or a<=y) and z>=x
print("We are using < OP (x<a) :",x<a) 
print("We are using > OP (y>z) :",y>z) 
print("We are using <= OP (a<=y ) :",a<=y ) 
print("We are using >= OP (z>=x) :",z>=x) 
print("We are using not OP (not x<a) :",(not x<a))
print("We are using or OP (y>z or a<=y) :",y>z or a<=y)
print("We are using not, and OP (not(not x<a and (y>z or a<=y)) :",not x<a and (y>z or a<=y))
print("We are using and, or OP  ((y>z or a<=y) and z>=x):",(y>z or a<=y) and z>=x)
print("Final Output  not x<a and (y>z or a<=y) and z>=x  is :",not x<a and (y>z or a<=y) and z>=x,"\n")

#input-4:not x==y or (z>=a and y<=z and z!=y)
print("We are using == OP (x==y) :",x==y) 
print("We are using >= OP (z>=a) :",z>=a)
print("We are using <= OP (y<=z ) :",y<=z ) 
print("We are using != OP (z!=y) :",z!=y)
print("We are using not OP (not x<a) :",(not x==y))
print("We are using and OP (z>=a and y<=z) :",z>=a and y<=z)
print("We are using and OP (y<=z and z!=y) :",(y<=z and z!=y))
print("We are using and OP (z>=a and y<=z and z!=y) :",(z>=a and y<=z and z!=y)) 
print("Final Output not x==y or (z>=a and y<=z and z!=y) is:",not x==y or (z>=a and y<=z and z!=y),"\n")

#input-5:not (y!=5 and z!=0b101000) or (x==0b1010 and a>=0b1010)

print("We are using != OP (y!=5) :",y!=5) 
print("We are using != OP (z!=0b101000) :",z!=0b101000) 
print("We are using == OP (x==0b1010 ) :",x==0b1010 ) 
print("We are using >= OP (a>=0b1010) :",a>=0b1010) 
print("We are using and OP (y!=5 and z!=0b10100) :",y!=5 and z!=0b10100)
print("We are using not,and OP not (y!=5 and z!=0b10100) :",not(y!=5 and z!=0b10100))
print("We are using and OP ((x==0b1010 and a>=0b1010) :",(x==0b1010 and a>=0b1010))
print("Final Output  not (y!=5 and z!=0b101000) or (x==0b1010 and a>=0b1010) is:",not (y!=5 and z!=0b101000) or (x==0b1010 and a>=0b1010),"\n")
			
			
			
			