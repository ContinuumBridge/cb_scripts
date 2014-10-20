#!/usr/bin/env python
# checkeew.py
# Copyright (C) ContinuumBridge Limited, 2013-14 - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Peter Claydon
#
gerasurl = 'http://geras.1248.io/'

# Include the Dropbox SDK
#from dropbox.client import DropboxClient, DropboxOAuth2Flow, DropboxOAuth2FlowNoRedirect
#from dropbox.rest import ErrorResponse, RESTSocketError
#from dropbox.datastore import DatastoreError, DatastoreManager, Date, Bytes
from pprint import pprint
import requests
from urllib import urlencode
from requests.auth import HTTPBasicAuth
from datetime import datetime
import json
import time
import sys
import click
from os import rename
from os.path import expanduser
import os, sys

def nicetime(timeStamp):
    localtime = time.localtime(timeStamp)
    milliseconds = '%03d' % int((timeStamp - int(timeStamp)) * 1000)
    now = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
    return now

def epochtime(date_time):
    pattern = '%Y-%m-%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(date_time, pattern)))
    return epoch

@click.command()
@click.option('--list', nargs=1, help='Lists time series on Geras. --list all or --list <pattern>.')
@click.option('--get', nargs=1, help='Gets time series from Geras. --get <name of time series.')
@click.option('--start', nargs=1, help='Start time for getting time series in the format: 18-10-2014 11:05:02.')
@click.option('--end', nargs=1, help='End time for getting time series in the format: 18-10-2014 11:05:02.')
@click.option('--csv', nargs=1, help='Name of file containing time series to put into csv file.')
@click.option('--key', prompt='Geras API key', help='Your Geras API key. See http://geras.1248.io/user/apidoc.')

def pulldata(list, key, get, start, end, csv):
    if list:
        r = requests.get('http://geras.1248.io/serieslist', auth=(key,''))
        timeseries = json.loads(r.content)
        if list.lower() == "all":
            print(json.dumps(timeseries, indent=4))
        else:
            for t in timeseries:
                if list in t:
                    print t
    elif get:
        if start:
            startTime = epochtime(start)
            if end:
                endTime = epochtime(end)
            else:
                endTime = time.time()
            url = gerasurl + 'series/' + get +'?start=' + str(startTime) + '&end=' + str(endTime)
        elif end:
            print "If you specify an end time, you must also specify a start time"
            exit()
        else:
            url = gerasurl + 'series/' + get
        r = requests.get(url, auth=(key,''))
        timeseries = json.loads(r.content)
        #print(json.dumps(timeseries, indent=4))
        for t in timeseries["e"]:
            print nicetime(t["t"]) + '  ' +  str("%2.1f" %t["v"])
    elif csv:
        try:
            with open(csv, 'r') as configFile:
                csvSeries = json.load(configFile)
        except:
            print "Could not open csv config file or file badly formatted"
            exit()
        print(json.dumps(csvSeries, indent=4))
        if start:
            startTime = epochtime(start)
            if end:
                endTime = epochtime(end)
            else:
                endTime = time.time()
        elif end:
            print "If you specify an end time, you must also specify a start time"
            exit()
        timeseries = {}
        for s in csvSeries:
            if start:
                url = gerasurl + 'series/' + get +'?start=' + str(startTime) + '&end=' + str(endTime)
            else:
                url = gerasurl + 'series/' + get
            r = requests.get(url, auth=(key,''))
            timeseries[s] = json.loads(r.content)["e"]
        munge = True
        lines= []
        num = 0
        while munge:
            # Pick a series.
            # lines = [t, v] for that series
            # Next series:
            #   First time of lines:
            #     Depends on whether t if same as > or <. 
            for t in timeseries:
                pos = 0
                for s in t:
                    if num == 0:
                        lines.append([s["t"], s["v"]
                    else:
                        if s["t"] < lines[pos[0]]
                            lines.insert([s["t"], 
                            
            lines = [timeseries
            line 
                    for r in readings:
                        timeStamp = float(r.get('Date'))
                        if timeStamp > max:
                            max = timeStamp
                        dat = r.get('Data')
                        line = commas + str("%2.1f" %dat)
                        values.append([timeStamp, line])
                    commas += ","
                    rows.append([devHandle, devName, sensor, niceTime(max)])


if __name__ == '__main__':
    pulldata()

