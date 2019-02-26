#include <L298NHBridge.hpp>
#include <wiringPi.h>
#include <softPwm.h>
#include <stdexcept>

#define ABS(x)    ((x) < 0 ? -(x) : (x))

L298NHBridge::L298NHBridge(int ENA, int IN1, int IN2, int IN3, int IN4, int ENB, double min_speed) {
  this->ENA = ENA;
  this->IN1 = IN1;
  this->IN2 = IN2;
  this->IN3 = IN3;
  this->IN4 = IN4;
  this->ENB = ENB;
  if (min_speed < 0.0 || min_speed > 1.0)
    throw std::range_error("min_speed out of scope");
  else
    this->min_speed = min_speed;
  setup();
}

L298NHBridge::~L298NHBridge() {
  cleanup();
}

void L298NHBridge::cleanup() const {
  digitalWrite(ENA, LOW);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  digitalWrite(ENB, LOW);
  softPwmWrite(ENA, 0);
  softPwmWrite(ENB, 0);
}

void L298NHBridge::setup() const {
  wiringPiSetupGpio();
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENB, OUTPUT);
  softPwmCreate(ENA, 0, 100);
  softPwmCreate(ENB, 0, 100);
}

void L298NHBridge::setMotorA(double speed) const {
  if (speed < -1.0 || speed > 1.0)
    throw std::range_error("speed value out of range for motor A");

  if (speed > 0.0) {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
  } else if (speed < 0.0) {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
  } else {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
  }

  if (speed != 0.0)
    softPwmWrite(ENA, (int) (ABS(speed) * (1.0 - min_speed) + min_speed) * 100);
  else
    softPwmWrite(ENA, 0);
}

void L298NHBridge::setMotorB(double speed) const {
  if (speed < -1.0 || speed > 1.0)
    throw std::range_error("speed value out of range for motor B");

  if (speed > 0.0) {
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
  } else if (speed < 0.0) {
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
  } else {
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, LOW);
  }

  if (speed != 0.0)
    softPwmWrite(ENB, (int) (ABS(speed) * (1.0 - min_speed) + min_speed) * 100);
  else
    softPwmWrite(ENB, 0);
}

void L298NHBridge::setMotors(double motor_a_speed, double motor_b_speed) const {
  setMotorA(motor_a_speed);
  setMotorB(motor_b_speed);
}

void L298NHBridge::stopMotors() const {
  setMotors(0.0, 0.0);
}
