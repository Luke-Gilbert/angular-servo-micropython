from machine import Pin,PWM #Import Required Libaries
class servo(): #The class
    def convert_pwm(self, angle):
        return ((angle*650/3+9500)/6) #Formula to convert angle to correct pwm.
    def angle(self, angle, pin):
        pwm = PWM(Pin(pin)) #Set pin
        pwm.freq(50) #Set Frequency
        servo_position = ((angle*650/3+9500)/6) # Formula to convert angle to correct pwm; Don't worry I wont repeat that formula again ;) DRY - Don't Repeat Yourself.
        pwm.duty_u16(int(servo_position)) #Set servo position
    def pwm(self, pwm, pin):
        try:
            servopwm = PWM(Pin(pin)) #Set pin
            servopwm.freq(50) #Set Frequency
        except Exception: #Error Handling
            print('Error; Will not attempt to continue \n Check out the github page if you are having issues.')
            raise
        try:
            servopwm.duty_u16(int(pwm)) #Set Servo Position
        except TypeError: #Error Handling (Common cause is non integer inputs)
            print('Must be integer value input to servo_pwm \n Will Attempt to continue')
        except Exception: #If not type error raise the error
            print('Error; Will not attempt to continue \n Check out the github page if you are having issues.')
            raise
