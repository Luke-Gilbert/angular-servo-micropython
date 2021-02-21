from machine import Pin,PWM
class servo():
    def convert_pwm(self, angle):
        return ((angle*650/3+9500)/6) #Formula to convert angle to correct pwm.
    def angle(self, angle, pin):
        pwm = PWM(Pin(pin))
        pwm.freq(50)
        servo_position = ((angle*650/3+9500)/6) # Formula to convert angle to correct pwm; Don't worry I wont repeat that formula again ;) DRY - Don't Repeat Yourself.
        pwm.duty_u16(int(servo_position))
    def pwm(self, pwm, pin):
        servopwm = PWM(Pin(pin))
        servopwm.freq(50)
        try:
            servopwm.duty_u16(int(pwm))
        except TypeError:
            print('Must be integer value input to servo_pwm')
        except Exception:
            raise