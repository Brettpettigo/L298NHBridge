# module L298N_HBridge

import RPi.GPIO as GPIO

### SETUP ###
GPIO.setmode(GPIO.BCM)

class L298NHBridge:
    """Wrapper class for the L298N Dual H-Bridge"""

    def __init__(self):
        self.ENA = 0
        self.IN1 = 0
        self.IN2 = 0
        self.IN3 = 0
        self.IN4 = 0
        self.ENB = 0
        self.freq = 0
        self.min_speed = 0
        self.pwm_left = None
        self.pwm_right = None

    def __init__(self, ENA, IN1, IN2, IN3, IN4, ENB, freq=1000, min_speed=0.3):
        self.ENA = ENA
        self.IN1 = IN1
        self.IN2 = IN2
        self.IN3 = IN3
        self.IN4 = IN4
        self.ENB = ENB
        self.freq = freq
        if min_speed < 0.0 or min_speed > 1.0:
            raise ValueError("min_speed out of range")
        else:
            self.min_speed = min_speed
        self.pwm_left = None
        self.pwm_right = None
        self.setup()

    def __del__(self):
        self.pwm_left.stop()
        self.pwm_right.stop()
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)

    def setup(self);
        # initialize pins as outputs
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)

        # initialize pwm signals
        self.pwm_left = GPIO.PWM(self.ENA, self.freq)
        self.pwm_right = GPIO.PWM(self.ENB, self.freq)

        self.pwm_left.start(0)
        self.pwm_left.ChangeDutyCycle(0)

        self.pwm_right.start(0)
        self.pwm_right.ChangeDutyCycle(0)

    def setLeftMotor(self, speed):
        if speed < -1.0 or speed > 1.0:
            raise ValueError("speed value out of range for left motor")

        if speed > 0.0:
            GPIO.output(self.IN3, GPIO.HIGH)
            GPIO.output(self.IN4, GPIO.LOW)
        elif speed < 0.0:
            GPIO.output(self.IN3, GPIO.LOW)
            GPIO.output(self.IN4, GPIO.HIGH)
        else:
            GPIO.output(self.IN3, GPIO.LOW)
            GPIO.output(self.IN4, GPIO.LOW)

        # set left motor speed
        if speed != 0.0:
            pwm_left.ChangeDutyCycle((abs(speed) * (1.0 - self.min_speed) + self.min_speed) * 100.0)
        else:
            pwm_left.ChangeDutyCycle(0)

    def setRightMotor(self, speed):
        if speed < -1.0 or speed > 1.0:
            raise ValueError("speed value out of range for right motor")

        if speed > 0.0:
            GPIO.output(self.IN1, GPIO.HIGH)
            GPIO.output(self.IN2, GPIO.LOW)
        elif speed < 0.0:
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
        else:
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.LOW)

        # set left motor speed
        if speed != 0.0:
            pwm_right.ChangeDutyCycle((abs(speed) * (1.0 - self.min_speed) + self.min_speed) * 100.0)
        else:
            pwm_right.ChangeDutyCycle(0)

    def setMotors(self, left_motor_speed, right_motor_speed):
        self.setLeftMotor(left_motor_speed)
        self.setRightMotor(right_motor_speed)

    def stopMotors(self):
        self.setMotors(0.0, 0.0)
