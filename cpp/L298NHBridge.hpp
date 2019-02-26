#ifndef __L298NHBridge_HPP
#define __L298NHBridge_HPP

// Wrapper for the L298N Dual H-Bridge
// motor A in assumed to be connected to (ENB, IN3, IN4)
// motor B is assumed to be connected to (ENA, IN1, IN2)
class L298NHBridge {
public:

  L298NHBridge() = default;

  L298NHBridge(int ENA, int IN1, int IN2, int IN3, int IN4, int ENB, double min_speed=0.3);

  ~L298NHBridge();

  void setup() const;

  void cleanup() const;

  // set speed of motor A from range [-1.0..1.0]
  void setMotorA(double speed) const;

  // set speed of motor B from range [-1.0..1.0]
  void setMotorB(double speed) const;

  void setMotors(double motor_a_speed, double motor_b_speed) const;

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
