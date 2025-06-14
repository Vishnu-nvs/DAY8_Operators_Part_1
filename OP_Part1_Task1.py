
x=10
y=20
z=40
a=5

print("Given String x is:",x)
print("Given String y is:",y)	
print("Given String z is:",z)				
print("Given String a is:",a,"\n")	

#input-1:x<a and y>z and a<=y and z>=x
print("We are using < OP (x<a) :",x<a) #F
print("We are using > OP (y>z) :",y>z) #F
print("We are using <= OP (a<=y ) :",a<=y ) #T
print("We are using >= OP (z>=x) :",z>=x) #T
print("We are using and OP (x<a and y>z) :",x<a and y>z)
print("We are using and OP (y>z and a<=y) :",y>z and a<=y)
print("We are using and OP (a<=y and z>=x) :",a<=y and z>=x)
print("Final Output is (x<a and y>z and a<=y and z>=x):",x<a and y>z and a<=y and z>=x,"\n")

#input-2:y>x and z<a and a>=z and z>=y
print("We are using > OP (y>x) :",y>x)
print("We are using < OP (z<a) :",z<a)
print("We are using >= OP (a>=z) :",a>=z )
print("We are using >= OP (z>=y) :",z>=y) 
print("We are using and OP (y>x and z<a) :",y>x and z<a)
print("We are using and OP (z<a and a>=z) :",z<a and a>=z)
print("We are using and OP (a>=z and z>=y) :",a>=z and z>=y)
print("Final Output is (y>x and z<a and a>=z and z>=y):",y>x and z<a and a>=z and z>=y,"\n")

#input-3:x<a and y>z and a<=y and z>=x
print("We are using < OP (x<a) :",x<a) 
print("We are using > OP (y>z) :",y>z) 
print("We are using <= OP (a<=y ) :",a<=y ) 
print("We are using >= OP (z>=x) :",z>=x) 
print("We are using and OP (x<a and y>z) :",x<a and y>z)
print("We are using and OP (y>z and a<=y) :",y>z and a<=y)
print("We are using and OP (a<=y and z>=x) :",a<=y and z>=x)
print("Final Output is (x<a and y>z and a<=y and z>=x):",x<a and y>z and a<=y and z>=x,"\n")

#input-4:x==y and z>=a and y<=z and z!=y
print("We are using == OP (x==y) :",x==y) 
print("We are using >= OP (z>=a) :",z>=a) 
print("We are using <= OP (y<=z ) :",y<=z ) 
print("We are using != OP (z!=y) :",z!=y) 
print("We are using and OP (x==y and z>=a) :",x==y and z>=a)
print("We are using and OP (z>=a and y<=z) :",z>=a and y<=z)
print("We are using and OP (y<=z and z!=y) :",y<=z and z!=y)
print("Final Output is (x==y and z>=a and y<=z and z!=y):",x==y and z>=a and y<=z and z!=y,"\n")

# #input-5:y!=5 and z!=0b101000 and x==0b1010 and a>=0b1010 

print("We are using != OP (y!=5) :",y!=5) 
print("We are using != OP (z!=0b101000) :",z!=0b101000) 
print("We are using == OP (x==0b1010) :",x==0b1010) 
print("We are using >= OP (a>=0b1010) :",a>=0b1010) 
print("We are using and OP (y!=5 and z!=0b101000) :",y!=5 and z!=0b101000)
print("We are using and OP (z!=0b101000 and x==0b1010) :",z!=0b101000 and x==0b1010)
print("We are using and OP (x==0b1010 and a>=0b1010) :",x==0b1010 and a>=0b1010)
print("Final Output is (y!=5 and z!=0b101000 and x==0b1010 and a>=0b1010):",y!=5 and z!=0b101000 and x==0b1010 and a>=0b1010,"\n")

