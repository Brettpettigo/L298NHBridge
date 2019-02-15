#ifndef __L298NHBridge_HPP
#define __L298NHBridge_HPP

// Wrapper for the L298N Dual H-Bridge
// left motor in assumed to be connected to (ENB, IN3, IN4)
// right motor is assumed to be connected to (ENA, IN1, IN2)
class L298NHBridge {
public:

  L298NHBridge() = default;

  L298NHBridge(int ENA, int IN1, int IN2, int IN3, int IN4, int ENB, double min_speed=0.3);

  ~L298NHBridge();

  void setup() const;

  // set left motor speed [-1.0..1.0]
  void setLeftMotor(double speed) const;

  // set right moto speed [-1.0..1.0]
  void setRightMotor(double speed) const;

  void setMotors(double left_motor_speed, double right_motor_speed) const;

  void stopMotors() const;

  int ENA = 0;

  int IN1 = 0;

  int IN2 = 0;

  int IN3 = 0;

  int IN4 = 0;

  int ENB = 0;

  double min_speed = 0.0;

};

#endif // __L298NHBridge_HPP
