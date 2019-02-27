# module L298N_HBridge

import RPi.GPIO as GPIO

### SETUP ###
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Driver for the L298N Dual H-Bridge
# motor A in assumed to be connected to (ENA, IN1, IN2)
# motor B is assumed to be connected to (ENB, IN3, IN4)
class L298NHBridge:
    """Driver class for L298N Dual H-Bridge"""

    def __init__(self):
        self.ENA = 0
        self.IN1 = 0
        self.IN2 = 0
        self.IN3 = 0
        self.IN4 = 0
        self.ENB = 0
        self.freq = 0
        self.min_speed = 0
        self.pwm_a = None
        self.pwm_b = None

    def __init__(self, ENA, IN1, IN2, IN3, IN4, ENB, min_speed=0.3, freq=1000):
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
        self.pwm_a = None
        self.pwm_b = None
        self.setup()

    def __del__(self):
        cleanup()

    def setup(self):
        # initialize pins as outputs
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)

        # initialize pwm signals
        self.pwm_a = GPIO.PWM(self.ENA, self.freq)
        self.pwm_b = GPIO.PWM(self.ENB, self.freq)

        self.pwm_a.start(0)
        self.pwm_a.ChangeDutyCycle(0)

        self.pwm_b.start(0)
        self.pwm_b.ChangeDutyCycle(0)
        
    def cleanup():
        self.pwm_a.stop()
        self.pwm_b.stop()
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)

    def setMotorA(self, speed):
        if speed < -1.0 or speed > 1.0:
            raise ValueError("speed value out of range for motor A")

        if speed > 0.0:
            GPIO.output(self.IN1, GPIO.HIGH)
            GPIO.output(self.IN2, GPIO.LOW)
        elif speed < 0.0:
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
        else:
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.LOW)

        # set motor speed
        if speed != 0.0:
            self.pwm_a.ChangeDutyCycle((abs(speed) * (1.0 - self.min_speed) + self.min_speed) * 100.0)
        else:
            self.pwm_a.ChangeDutyCycle(0)

    def setMotorB(self, speed):
        if speed < -1.0 or speed > 1.0:
            raise ValueError("speed value out of range for motor B")

        if speed > 0.0:
            GPIO.output(self.IN3, GPIO.HIGH)
            GPIO.output(self.IN4, GPIO.LOW)
        elif speed < 0.0:
            GPIO.output(self.IN3, GPIO.LOW)
            GPIO.output(self.IN4, GPIO.HIGH)
        else:
            GPIO.output(self.IN3, GPIO.LOW)
            GPIO.output(self.IN4, GPIO.LOW)

        # set motor speed
        if speed != 0.0:
            self.pwm_b.ChangeDutyCycle((abs(speed) * (1.0 - self.min_speed) + self.min_speed) * 100.0)
        else:
            self.pwm_b.ChangeDutyCycle(0)

    def setMotors(self, motor_a_speed, motor_b_speed):
        self.setMotorA(motor_a_speed)
        self.setMotorB(motor_b_speed)

    def stopMotors(self):
        self.setMotors(0.0, 0.0)
