CC=g++

all: test

test: test.o L298NHBridge.o
	$(CC) test.o L298NHBridge.o -o test -lwiringPi -lpthread

test.o: test.cpp L298NHBridge.hpp
	$(CC) -c -std=c++11 -Wall test.cpp -I./

L298NHBridge.o: L298NHBridge.cpp L298NHBridge.hpp
	$(CC) -c -std=c++11 -Wall L298NHBridge.cpp -I./

clean:
	rm -r *.o
