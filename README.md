# DAY8_Operators_Part_1
Arithmetic and Assignment and Comparison and Logical Operators Concepts



Arithemetic_OP_Sample.py  (Output)

Given input  a is: 13
Given input  b is: 20 

Addition of A & B is : 33
Subtraction Of A & B is : -7
Multiplication of A & B is : 260
Division of A & B is : 1.5384615384615385
Division of 12 & 5 is : 2.4
division of A & B using modulus is :  7
Floor division of A & B is : 1
Exponentiation  of A & B is : 19004963774880799438801



Assignment_Op_Sample.py (Output)

we are assign the value to the X variable : 5 

we are using = OP 5
We are using += OP (x+=10) : 15
We are using -= OP  (x-=4) : 11
We are using * OP (x*=4) : 44
We are using += OP (x/=7) : 6.285714285714286
X value is : 87
We are using %= OP (x%=7) : 3
We are using **= OP (x**=3) : 27
We are using //= OP (x//=4) : 6
We are using &= OP (x&=4) : 4
We are using |= OP (x|=3) : 7
We are using ^= OP (x^=2) : 5
We are using >>= OP (x>>=2) : 1
We are using <<= OP (x<<=5) : 32



Comparsion-OP_Sample.py  (Output)

0b1010
10
True
We are using == OP (x==y) : True 
We are using != OP (x!=y) : False
We are using > OP (x>y) : False  
We are using < OP (x<y) : False  
We are using >= OP (x>=y) : True 
We are using <= OP (x<=y) : True 

---------------------------------------------------------------TASKS------------------------------
OP_Part1_Task1.py  (Output)

Given String x is: 10
Given String y is: 20
Given String z is: 40
Given String a is: 5 

We are using < OP (x<a) : False
We are using > OP (y>z) : False
We are using <= OP (a<=y ) : True
We are using >= OP (z>=x) : True
We are using and OP (x<a and y>z) : False
We are using and OP (y>z and a<=y) : False
We are using and OP (a<=y and z>=x) : True
Final Output is (x<a and y>z and a<=y and z>=x): False 

Trueth-Table
--------------
x<a :False
y>z :False
a<=y : True
z>=x :True
x<a and y>z and a<=y and z>=x = False & False &True & True = False


We are using > OP (y>x) : True
We are using < OP (z<a) : False
We are using >= OP (a>=z) : False
We are using >= OP (z>=y) : True
We are using and OP (y>x and z<a) : False
We are using and OP (z<a and a>=z) : False
We are using and OP (a>=z and z>=y) : False
Final Output is (y>x and z<a and a>=z and z>=y): False

Trueth-Table 
--------------
y>x and z<a and a>=z and z>=y
(y>x) : True
(z<a) : False
(a>=z) : False
(z>=y) : True
y>x and z<a) : False
(z<a and a>=z) : False
(a>=z and z>=y) : False
(y>x and z<a and a>=z and z>=y): True & False & False & True = False

St1     St2     St3      St4   OUTPUT
---------------------------------------
T        F       F        T       F


We are using < OP (x<a) : False
We are using > OP (y>z) : False
We are using <= OP (a<=y ) : True
We are using >= OP (z>=x) : True
We are using and OP (x<a and y>z) : False
We are using and OP (y>z and a<=y) : False
We are using and OP (a<=y and z>=x) : True
Final Output is (x<a and y>z and a<=y and z>=x): False

Trueth-Table
--------------
x<a and y>z and a<=y and z>=x
(x<a) : False
(y>z) : False
(a<=y ) : True
(z>=x) : True
(x<a and y>z) : False
(y>z and a<=y) : False
(a<=y and z>=x) : True
(x<a and y>z and a<=y and z>=x): False & False & True & True = False

St1     St2     St3      St4   OUTPUT
---------------------------------------
F       F        T       T       F



We are using == OP (x==y) : False
We are using >= OP (z>=a) : True
We are using <= OP (y<=z ) : True
We are using != OP (z!=y) : True
We are using and OP (x==y and z>=a) : False
We are using and OP (z>=a and y<=z) : True
We are using and OP (y<=z and z!=y) : True
Final Output is (x==y and z>=a and y<=z and z!=y): False

Trueth-Table
--------------
x==y and z>=a and y<=z and z!=y
(x==y) : False
(z>=a) : True
(y<=z ) : True
(z!=y) : True
(x==y and z>=a) : False
(z>=a and y<=z) : True
(y<=z and z!=y) : True
(x==y and z>=a and y<=z and z!=y): False & True & True & True= False

                 or
x==y and z>=a and y<=z and z!=y
St1      St2       St3      St4   OUTPUT
---------------------------------------
F         T        T         T      F

We are using != OP (y!=5) : True
We are using != OP (z!=0b101000) : False
We are using == OP (x==0b1010) : True
We are using >= OP (a>=0b1010) : False
We are using and OP (y!=5 and z!=0b101000) : False
We are using and OP (z!=0b101000 and x==0b1010) : False
We are using and OP (x==0b1010 and a>=0b1010) : False
Final Output is (y!=5 and z!=0b101000 and x==0b1010 and a>=0b1010): False

Trueth-Table
--------------
(y!=5) : True
(z!=0b101000) : False
(x==0b1010) : True
a>=0b1010) : False
(y!=5 and z!=0b101000) : False
z!=0b101000 and x==0b1010) : False
x==0b1010 and a>=0b1010) : False
(y!=5 and z!=0b101000 and x==0b1010 and a>=0b1010): True and False & True & False = False
                          or 
y!=5 and z!=0b101000 and x==0b1010 and a>=0b1010
St1        St2               St3          St4       OUTPUT
-----------------------------------------------------------
T           F                 T            F           F



OP_Part1_Task2.py (OUPUT)

Given String x is: 10
Given String y is: 20
Given String z is: 40
Given String a is: 5 

We are using < OP (x<a) : False
We are using > OP (y>z) : False
We are using <= OP (a<=y ) : True
We are using >= OP (z>=x) : True
We are using and OP (x<a and y>z) : False
We are using and OP ((x<a and y>z) and a<=y) : False
We are using and,or OP (((x<a and y>z) and a<=y) or z>=x : True 

Trueth-Table
--------------
(x<a and y>z) and a<=y) or z>=x
St1     St2  Output  St3  Output   St4   FinalOutput
-----------------------------------------------
F       F      F       T     F     T       T

We are using > OP (y>x) : True
We are using < OP (z<a) : False
We are using >= OP (a>=z) : False
We are using >= OP (z>=x) : True
We are using or OP (y>x or z<a) : True
We are using or OP (a>=z or z>=y) : True
We are using or,and OP (y>x or z<a) and (a>=z or z>=y) : True

Trueth-Table
--------------
(y>x or z<a) and (a>=z or z>=y)
St1     St2  Output  St3   St4   Output   FinalOutput
------------------------------------------------------
T       F      T      F     T      T             T

We are using < OP (x<a) : False
We are using > OP (y>z) : False
We are using <= OP (a<=y ) : True
We are using >= OP (z>=x) : True
We are using or OP (y>z or a<=y) : True
We are using and,or OP (x<a and (y>z or a<=y)) : False
We are using or OP (a>=z or z>=y) : True
We are using and,or OP x<a and (y>z or a<=y) and z>=x: False

Trueth-Table
--------------
x<a and (y>z or a<=y) and z>=x
St1        St2 & St3 =OUPUT     St4   FinalOUTPUT
-------------------------------------------------------
F           F     T    T         T        F

We are using == OP (x==y) : False
We are using >= OP (z>=a) : True
We are using <= OP (y<=z ) : True
We are using != OP (y<=z) : True
We are using and OP (z>=a and y<=z) : True
We are using and OP (y<=z and z!=y) : True
We are using and OP (z>=a and y<=z and z!=y) : True
We are using and,or OP (x==y or (z>=a and y<=z and z!=y) : True

Trueth-Table
--------------
(x==y or (z>=a and y<=z and z!=y)
St1        St2      St3     St4   OUTPUT    FinalOUTPUT
---------------------------------------------------------
F           T        T       T      T           T

We are using != OP (y!=5) : True
We are using != OP (z!=0b101000) : False
We are using == OP (x==0b1010 ) : True
We are using >= OP (a>=0b1010)) : False
We are using and OP (y!=5 and z!=0b10100) : True
We are using and OP ((x==0b1010 and a>=0b1010) : False
Final Output is ((y!=5 and z!=0b101000) or (x==0b1010 and a>=0b1010): False

Trueth-Table
--------------
(y!=5 and z!=0b101000) or (x==0b1010 and a>=0b1010)
St1        St2 OUTPUT       St3              St4   OUTPUT   FinalOUTPUT
------------------------------------------------------------------------
T          F     F           T                F       F        F


OP_Part1_Task3.py (OUPUT)

Given String x is: 10
Given String y is: 20
Given String z is: 40
Given String a is: 5 

We are using < OP (x<a) : False
We are using > OP (y>z) : False
We are using <= OP (a<=y ) : True
We are using >= OP (z>=x) : True
We are using and OP (x<a and y>z) : False
We are using and OP ((x<a and y>z) and a<=y) : False
We are using not,and OP (not((x<a and y>z) and a<=y)) : True   
Final Output not((x<a and y>z) and a<=y) or z>=x is: True            
 
Trueth-Table
--------------
not((x<a and y>z) and a<=y) or z>=x
     St1   St2  Output St3 S1&S2&S3-Output  n(S1&S2&S3-Output) St4   FinalOutput
----------------------------------------------------------------------------------
      F    F      F     T            F              T           T      T

We are using > OP (y>x) : True
We are using < OP (z<a) : False
We are using >= OP (a>=z) : False
We are using >= OP (z>=y) : True
We are using or OP (y>x or z<a) : True
We are using or OP (a>=z or z>=y) : True
We are using not,or OP (not (y>x or z<a)) : False
Final Output  (y>x or z<a) and (a>=z or z>=y) is: False     

Trueth-Table
--------------
not (y>x or z<a) and (a>=z or z>=y)
     St1   St2  Output  n(S1&S2-Output)   St3       S4  Output     FinalOutput
-------------------------------------------------------------------------------
      T    F      T         F              F         T     T            F

We are using < OP (x<a) : False
We are using > OP (y>z) : False
We are using <= OP (a<=y ) : True
We are using >= OP (z>=x) : True
We are using not OP (not x<a) : True
We are using or OP (y>z or a<=y) : True
We are using not, and OP (not(not x<a and (y>z or a<=y)) : True
We are using and, or OP  ((y>z or a<=y) and z>=x): True        
Final Output  not x<a and (y>z or a<=y) and z>=x  is : True

Trueth-Table
--------------
not x<a and (y>z or a<=y) and z>=x
 St1 not(S1) St2     St3 S2&S3-Output   St4   FinalOutput
----------------------------------------------------------------------------
 F     T      F       T      T           T        T          

We are using == OP (x==y) : False
We are using >= OP (z>=a) : True
We are using <= OP (y<=z ) : True
We are using != OP (z!=y) : True
We are using not OP (not x<a) : True
We are using and OP (z>=a and y<=z) : True
We are using and OP (y<=z and z!=y) : True
We are using and OP (z>=a and y<=z and z!=y) : True
Final Output not x==y or (z>=a and y<=z and z!=y) is: True
Trueth-Table
--------------
not x==y or (z>=a and y<=z and z!=y)
 St1 not(S1) St2     St3     S3 S1&S2&S3-Output     FinalOutput
----------------------------------------------------------------------------
 F     T      T       T      T           T              T      

We are using != OP (y!=5) : True
We are using != OP (z!=0b101000) : False
We are using == OP (x==0b1010 ) : True
We are using >= OP (a>=0b1010) : False
We are using and OP (y!=5 and z!=0b10100) : True
We are using not,and OP not(y!=5 and z!=0b10100) : False
We are using and OP ((x==0b1010 and a>=0b1010) : False
Final Output  not (y!=5 and z!=0b101000) or (x==0b1010 and a>=0b1010) is: True
Trueth-Table
--------------
not (y!=5 and z!=0b101000) or (x==0b1010 and a>=0b1010)
 St1  St2  S1&S2-Output n(S1&S2-Output )  St3   St4 S3&S4-Output   FinalOutput
-------------------------------------------------------------------------------
 T     F     F              T              T      F        F            T


OP_Part1_Task4.py  (OUPUT)

Given String x is: 10
Given String y is: 20
Given String z is: 40
Given String a is: 5 

We are using < OP (x<a) : False
We are using > OP (y>z) : False
We are using <= OP (a<=y ) : True
We are using >= OP (z>=x) : True
We are using not OP (not x<a ) : True
We are using not,and OP (not x<a and y>z) : False
We are using and OP (y>z and a<=y) : False
We are using and OP (a<=y and z>=x) : True
Final Output  not x<a and y>z and a<=y and z>=x  is: False 

Trueth-Table
--------------
not x<a and y>z and a<=y and z>=x
 St1 not(S1) St2     St3    S4     FinalOutput
---------------------------------------------------
 F     T      F       T      T           F     

We are using > OP (y>x) : True
We are using not OP (y>x) : False
We are using < OP (z<a) : False
We are using >= OP (a>=z) : False
We are using >= OP (z>=y) : True
We are using not,and OP (not y>x or z<a) : False
We are using and OP (z<a and a>=z)) : False
We are using and OP (a>=z and z>=y) : False
Final Output  not y>x and z<a and a>=z and z>=y is: False    

Trueth-Table
--------------
not y>x and z<a and a>=z and z>=y
 St1 not(S1) St2     St3     St4 FinalOutput
-----------------------------------------------
 T     F      F       F       T         F           

We are using < OP (x<a) : False
We are using not OP (not x<a) : True
We are using > OP (y>z) : False
We are using <= OP (a<=y ) : True
We are using >= OP (z>=x) : True
We are using not, and OP ((not x<a and y>z)) : False       
We are using and OP (y>z or a<=y) : False
We are using and, and OP  (a<=y and z>=x): True
Final Output  not x<a and y>z and a<=y and z>=x is : False 

Trueth-Table
--------------
not x<a and y>z and a<=y and z>=x
 St1 not(S1) St2     St3     S4    FinalOutput
--------------------------------------------------
 F     T      F      T      T           F                

We are using == OP (x==y) : False
We are using not OP (not x==y) : True
We are using >= OP (z>=a) : True
We are using <= OP (y<=z ) : True
We are using != OP (z!=y) : True
We are using not,and OP (not x==y and z>=a ) : True
We are using and OP (z>=a and y<=z) : True
We are using and OP (y<=z and z!=y) : True
Final Output  not x==y and z>=a and y<=z and z!=y is: True

Trueth-Table
--------------
not x==y and z>=a and y<=z and z!=y
 St1 not(S1) St2     St3     St4    FinalOutput
----------------------------------------------------
 F     T      T       T      T           T                  


We are using != OP (y!=5) : True
We are using not,!= OP (y!=5) : False
We are using != OP (z!=0b101000) : False
We are using == OP (x==0b1010 ) : True
We are using >= OP (a>=0b1010) : False
We are using not,and OP (not y!=5 and z!=0b10100) : False
We are using not,and OP (z!=0b101000 and x==0b1010) : False
We are using and OP ((x==0b1010 and a>=0b1010) : False
Final Output  not y!=5 and z!=0b101000 and x==0b1010 and a>=0b101 is: False 


Trueth-Table
--------------
not y!=5 and z!=0b101000 and x==0b1010 and a>=0b101
 St1 not(S1)   St2              St3             St4   FinalOutput
--------------------------------------------------------------------
 T     F        F                T               F           F                 