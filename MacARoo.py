#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:66", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
