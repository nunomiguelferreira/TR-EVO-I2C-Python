#!/usr/bin/env python

import time
import datetime 
from time import gmtime, strftime
import struct
import sys
import binascii
import pigpio # http://abyz.co.uk/rpi/pigpio/python.html
from Queue import *
#time.sleep(10)

TR_EVO_I2C_ADDR=0x31 #just input here the I2C address you assigned to the TR EVO
BUS=1

def ini_tr():
	pi=pigpio.pi() # open local Pi
	h = pi.i2c_open(BUS, TR_EVO_I2C_ADDR)
	pi.i2c_write_byte(h, 0x01)  # ask TR_EVO who am I
	return pi,h

def read_distance( pi , h):
	pi.i2c_write_byte(h, 0x00)  #requests value
	#time.sleep(0.000001)
	#these sleep values (this one and the one below) can be edited for consistent data aquisition rate
	(b,d) = pi.i2c_read_i2c_block_data(h, 0x00, 3)
	#time.sleep(0.005)
	decode = binascii.hexlify(d)
	distance = decode[0:4]
	distance = int(distance, 16)
	distance = distance/float(1000) #returns distance in meters
	#print str(distance)
	return distance 

def change_address( pi , h, add): #make sure address comes in hexadecimal, else it won't work. Also Valid addresses accepted by the TeraRanger Evo are in the range 0x02 to 0x7F
	pi.i2c_write_byte(h, 0xA2)  # sends request to change address
	time.sleep(0.02) 
	pi.i2c_write_byte(h, add)  # if add is in hexa, it will change the TR EVO I2C address into that(will rejoin I2C bus in a bit)
				   # if you change address, remember to change address in the constant above!
