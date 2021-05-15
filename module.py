#!/usr/bin/python
import RPi.GPIO as GPIO
import time


def servo(angle):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    servo1 = GPIO.PWM(11,50)
    servo1.start(0)
    duty = angle/18 + 2
    GPIO.output(11,True)
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(11,False)
    servo1.ChangeDutyCycle(0)
    servo1.stop()
    GPIO.cleanup()



def distance(a):
    GPIO.setmode(GPIO.BOARD)
    if a == 1:
         PIN_TRIGGER = 13
         PIN_ECHO = 15
    elif a == 2:
         PIN_TRIGGER = 16
         PIN_ECHO = 18
    elif a == 3:
         PIN_TRIGGER = 29
         PIN_ECHO = 31
    elif a == 4:
         PIN_TRIGGER = 33
         PIN_ECHO = 35


    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    #print("Waiting for sensor to settle")
    time.sleep(2)
    #print("Calculating distance")

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)


    while GPIO.input(PIN_ECHO)==0:
          pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
          pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time

    dist = round(pulse_duration * 17150, 2)
    return dist
