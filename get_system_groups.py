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
  groupname = []
  try:
    sysname = client.system.search.hostname(key, str(line))
    sysid = client.system.getId(key, sysname[0]['hostname'])
    groups = client.system.listGroups(key, sysid[0]['id'])
    for group in groups:
      if group.get('subscribed') == 1:
        groupname.append(str(group.get('system_group_name')))
    print(sysname[0]['hostname'], ',', groupname)
  except:
    print("Unable to get the groups for the system" + str(line))
    continue

client.auth.logout(key)
