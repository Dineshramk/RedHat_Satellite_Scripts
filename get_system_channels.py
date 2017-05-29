#!/usr/bin/python
from __future__ import print_function
from datetime import datetime
import array
import time
import xmlrpclib
import sys
import base64

SATELLITE_URL = "http://satellite.example.com/rpc/api"
SATELLITE_LOGIN = "satellite username"
SATELLITE_PASSWORD = base64.b64decode("encrypted password")

systemslist = raw_input("Enter the filename having systems list:\n")

client = xmlrpclib.Server(SATELLITE_URL, verbose=0)
key = client.auth.login(SATELLITE_LOGIN, SATELLITE_PASSWORD)


fo = open(systemslist)
for line in fo:
  basechannel = []
  childchannel = []
  try:
    sysname = client.system.search.hostname(key, str(line))
    sysid = client.system.getId(key, sysname[0]['hostname'])
    basechannels = client.system.listSubscribableBaseChannels(key, sysid[0]['id'])
    for basecha in basechannels:
      if basecha.get('current_base') == 1:
        basechannel.append(basecha.get('label'))
    childchannels = client.system.listSubscribedChildChannels(key, sysid[0]['id'])
    for childcha in childchannels:
      childchannel.append(childcha.get('label'))
    print(sysname[0]['hostname'], ',', basechannel , ',', childchannel)
  except:
    print("Unable to get the channels for the system" + str(line))
    continue

client.auth.logout(key)
