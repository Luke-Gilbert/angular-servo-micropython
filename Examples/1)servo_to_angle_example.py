#Required Code
# 1. import servo_angles                       #Imports Module
# 2. Servo = servo_angles.servo                #Call the class variable anything you want but adapt the bellow building blocks
#'Do the Action' Code                       #Bellow assumes you called the class variable (Required 2.) to Servo. If you did not: Adapt the bollow where says Servo.the_feature. 
# 1. Servo.angle(angle, pin number)         #Sets the servo angle to the first positional argument(angle), for the pin number in the seccond positional argument (pin number) ** See Bottom
# 2. A_Variable = (Servo.convert_pwm(90))   #(Servo.convert_pwm(angle)) returns the required Pwm value to reach the required variable.
# 3. Servo.pwm(pwm_value, pin number)       #Sets the servo in the given pin number to the given pwm value.

import servo_angles 
Servo = servo_angles.servo()
Servo.angle(180, 2)
import utime
pin = 2
while True:
    #x = 0 # Set Variable X
    #Servo.angle(x, 2) # Set Servo Angle to 0
    utime.sleep(0.5) #Wait for it to move (If on 180degrees already)
    for x in range(180): #Loop and increment x by 1
        Servo.angle(x, pin) # Set servo angle to X
        utime.sleep(0.05)# Sleep 0,05s between movements
