# angular-servo-raspberry-pico
Set servo to set angles when using microcontrollers with micropython

The best way to use is to download the servo_angles.py and put it on the Raspberry Pi Pico's (Or any other MicroPython Microcontroller) File System (I would recommend opening it in Thonny and then saving it to file system.)
Then import servo_angles in your code.


Code Features:

Required Code
1. import servo_angles                    #Imports Module
2. Servo = servo_angles.servo             #Call the class variable anything you want but adapt the bellow building blocks

Do the Action Code                        #The bellow assumes the Class Variable is called Servo.
1. Servo.angle(angle, pin number)         #Sets the servo angle to the first positional argument(angle), for the pin number in the seccond positional argument (pin number) ** See Bellow
2. A_Variable = (Servo.convert_pwm(90))   #(Servo.convert_pwm(angle)) returns the required Pwm value to reach the required variable.
3. Servo.pwm(pwm_value, pin number)       #Sets the servo in the given pin number to the given pwm value.

** Says first and second positional argument, this is from this perspective; Technically because, 'def angle(self, angle, pin):' in the code makes it the second and third positional arguments.

I strongly recommend you see the examples in the example folder.
Here is the main example:

import servo_angles 
Servo = servo_angles.servo()
Servo.angle(180, 2)
import utime
pin = 2
while True:
    utime.sleep(0.5) #Wait for it to move (If on 180degrees already)
    for x in range(180): #Loop and increment x by 1
        Servo.angle(x, pin) # Set servo angle to X
        utime.sleep(0.05)# Sleep 0,05s between movements
