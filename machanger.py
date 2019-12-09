# !/usr/bin/env python     
import subprocess  #subprocess module help in executing the linux commands through python 
print("starting the script")  # printing a message

 #subprocess.call("linux command", shell=True)
  #shell = True means executing the command through shell and not directly.

subprocess.call("ifconfig wlan0 down",shell=True)  # first we have to bring the interface down 
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55",shell=True) # sepecifing the random mac address to the ether
subprocess.call("ifconfig wlan0 up",shell=True) # bringing the interface again up
print("ending the script") # end message 

