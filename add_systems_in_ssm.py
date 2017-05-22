#!/usr/bin/python

from datetime import datetime
import time
import xmlrpclib
import base64

SATELLITE_URL = "http://sesklpsat01.astrazeneca.net/rpc/api"
SATELLITE_LOGIN = "t3admin"
SATELLITE_PASSWORD = base64.b64decode("eTVAMWZ0Yg==")

groupname = raw_input("Enter the group name you want to create:\n")
systemslist = raw_input("Enter the filename having systems list:\n")

client = xmlrpclib.Server(SATELLITE_URL, verbose=0)

key = client.auth.login(SATELLITE_LOGIN, SATELLITE_PASSWORD)

client.systemgroup.create(key,str(groupname),str(groupname))

fo = open(systemslist)
for line in fo:
  try:
    sysname = client.system.search.hostname(key, str(line))
    print sysname[0]['hostname']
    sysid = client.system.getId(key, sysname[0]['hostname'])
    print sysid[0]['id']
    client.systemgroup.addOrRemoveSystems(key,str(groupname),sysid[0]['id'],True)
    print sysid[0]['name'] + " server added successfully"
  except:
    print str(line) + " server has error in adding"
    continue

client.auth.logout(key)
