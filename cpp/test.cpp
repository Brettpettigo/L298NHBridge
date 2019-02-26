#include <L298NHBridge.hpp>
#include <iostream>
#include <unistd.h>
#include <signal.h>

// pin setup
int ENA = 2;
int IN1 = 3;
int IN2 = 4;
int IN3 = 16;
int IN4 = 26;
int ENB = 21;

L298NHBridge bridge;

void cleanup(int sig) {
	bridge.cleanup();
	exit(0);
}

int main(void) {
	std::cout << "Running Motor" << std::endl;

	signal(SIGINT, cleanup);

	bridge = L298NHBridge(ENA, IN1, IN2, IN3, IN4, ENB);

	double speed = 1.0;

	while (true) {
		if (speed > 0.0) {
			std::cout << "turning forward" << std::endl;
		} else {
			std::cout << "turning backward" << std::endl;
		}

		speed *= -1.0;
		bridge.setMotors(speed, speed);
		sleep(2);
	}

	return 0;
}
