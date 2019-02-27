# L298NHBridge  
C++ / Python Driver for L298N Dual H-Bridge  

# C++ Usage  
cd cpp  
make && make clean  
./test  
(type Ctrl + C to end program)  
  
# Python Usage   
cd python  
./test.py  
(type Ctrl + C to end program)  

# Test Configuration  
Connect Motor A to ENA=2, IN1=3, IN2=4  
Connect Motor B to ENB=21, IN3=16, IN4=26  
Change configuration in test.cpp or test.py  
  
test or test.py let motors turn forward/backward for 2 seconds each  
until user ends program with Crtl + C.
