#Required Code
# 1. import servo_angles                       #Imports Module
# 2. Servo = servo_angles.servo                #Call the class variable anything you want but adapt the bellow building blocks
#'Do the Action' Code                       #Bellow assumes you called the class variable (Required 2.) to Servo. If you did not: Adapt the bollow where says Servo.the_feature. 
# 1. Servo.angle(angle, pin number)         #Sets the servo angle to the first positional argument(angle), for the pin number in the seccond positional argument (pin number) ** See Bottom
# 2. A_Variable = (Servo.convert_pwm(90))   #(Servo.convert_pwm(angle)) returns the required Pwm value to reach the required variable.
# 3. Servo.pwm(pwm_value, pin number)       #Sets the servo in the given pin number to the given pwm value.

import servo_angles 
Servo = servo_angles.servo()
import utime
for angle in range(180): #Loop and increment angle by 1
    pwmvalue = Servo.convert_pwm(angle) #Calculate required Pwm value for the incrementing angle
    print('To acheive ' + str(angle) + ' Degrees you would need a Pwm value of: ' + str(pwmvalue)) #Print Results
    utime.sleep(0.5)
    