#!/usr/bin/python

from datetime import datetime
import time
import xmlrpclib
import base64
import re
import csv

SATELLITE_URL = "http://satellite.example.com/rpc/api"
SATELLITE_LOGIN = "satellite username"
SATELLITE_PASSWORD = base64.b64decode("encoded password")

systemname = raw_input("Enter the system name you want to check:\n")

client = xmlrpclib.Server(SATELLITE_URL, verbose=0)
key = client.auth.login(SATELLITE_LOGIN, SATELLITE_PASSWORD)

sysname = client.system.search.hostname(key, str(systemname))

print "System Name : " + str(sysname[0]['hostname'])

sysid = client.system.getId(key, sysname[0]['hostname'])

print "System ID : " + str(sysid[0]['id'])

print "CPU Details:"
syscpu = client.system.getCpu(key, sysid[0]['id'])
print "No. of CPU's : " + str(syscpu.get('count'))
print "CPU Architecture : " + str(syscpu.get('arch'))
print "CPU Model : " + str(syscpu.get('model'))
print "CPU Vendor : " + str(syscpu.get('vendor'))
print "CPU Cache : " + str(syscpu.get('cache'))

print "Memory Details:"
sysmem = client.system.getMemory(key, sysid[0]['id'])
print "Memory Size(MB) : " + str(sysmem.get('ram'))
print "Swap Size(MB) : " + str(sysmem.get('swap'))

print "Network Details:"
sysnetworkdev = client.system.getNetworkDevices(key, sysid[0]['id'])
for sysnetdev in range(0, len(sysnetworkdev)):
  if str(sysnetworkdev[sysnetdev].get('module')) not in "loopback":
    print "Network Device : " + str(sysnetdev)
    print "Hardware Address : " + str(sysnetworkdev[sysnetdev].get('hardware_address'))
    print "IPv4 Address : " + str(sysnetworkdev[sysnetdev].get('ip'))
    print "Module : " + str(sysnetworkdev[sysnetdev].get('module'))
    print "Broadcast Address : " + str(sysnetworkdev[sysnetdev].get('broadcast'))
    print "Netmask Value : " + str(sysnetworkdev[sysnetdev].get('netmask'))
    print "IPv6 Address : " + str(sysnetworkdev[sysnetdev].get('ipv6'))

print "OS Details:")
sysrunningkernel = client.system.getRunningKernel(key, sysid[0]['id'])
print "Kernel Version : " + str(sysrunningkernel)
sysdetail = client.system.getDetails(key, sysid[0]['id'])
print "Server Description :\n" + str(sysdetail.get('description'))
syslastreboot = re.search(".*\'last_boot\'\: \<DateTime \'(.*?)\'\ at.*", str(sysdetail))
print "System Last Rebooted on : " + str(syslastreboot.group(1))

print "Hardware Details :"
sysdmi = client.system.getDmi(key, sysid[0]['id'])
if 'virtualization' in sysdetail:
  print "Vendor Details : " + str(sysdmi.get('product'))
  print "BIOS Vendor : " + str(sysdmi.get('bios_vendor'))
  print "BIOS Release : " + str(sysdmi.get('bios_release'))
  print "BIOS Version : " + str(sysdmi.get('bios_version'))
else:
  print "Vendor Details : " + str(sysdmi.get('vendor'))
  print "BIOS Vendor : " + str(sysdmi.get('bios_vendor'))
  print "BIOS Release : " + str(sysdmi.get('bios_release'))
  print "BIOS Version : " + str(sysdmi.get('bios_version'))
  print "Serial Numbers : " + str(sysdmi.get('asset'))

sysbasechan = client.system.getSubscribedBaseChannel(key, sysid[0]['id'])
print "System Base Channel : " + str(sysbasechan.get('name'))

client.auth.logout(key)
