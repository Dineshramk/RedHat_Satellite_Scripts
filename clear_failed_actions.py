#!/usr/bin/python

from datetime import datetime
import time
import xmlrpclib
import base64

SATELLITE_URL = "http://satellite.example.com/rpc/api"
SATELLITE_LOGIN = "satellite username"
SATELLITE_PASSWORD = base64.b64decode("encoded password")

client = xmlrpclib.Server(SATELLITE_URL, verbose=0)

key = client.auth.login(SATELLITE_LOGIN, SATELLITE_PASSWORD)

failedactions = client.schedule.listFailedActions(key)
failedcount = 0
for i in range(0, len(failedactions)):
  if failedactions[i]['inProgressSystems'] == 0:
    failedcount += 1
    try:
      client.schedule.archiveActions(key, int(failedactions[i]['id']))
      print str(failedactions[i]['id']) + " successfully archived"
    except:
      print str(failedactions[i]['id']) + " failed to archive"
      continue
print "Total No of Actions Archived : " + str(failedcount)	  

archivedactions = client.schedule.listArchivedActions(key)
archivedcount = 0
for i in range(0, len(archivedactions)):
  if archivedactions[i]['inProgressSystems'] == 0:
    archivedcount += 1
    try:
      client.schedule.deleteActions(key, int(archivedactions[i]['id']))
      print str(archivedactions[i]['id']) + " successfully archived"
    except:
      print str(archivedactions[i]['id']) + " failed to archive"
      continue
print "Total No of Actions Deleted : " + str(archivedcount)

client.auth.logout(key)
