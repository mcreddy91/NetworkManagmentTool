#! /usr/bin/env python

from pysnmp.entity.rfc3413.oneliner import ntforg
from pysnmp.proto import rfc1902
from pysnmp.proto.api import v2c
import datetime
import random
import time
import cx_Oracle
#from print_cursor import PrintCursor

class TrapGen:
    def __init__(self):
        self.data = ""
        self.dictionary = {}
        self.dev_cilly = self.getDeviceCLLI()

        self.getDictionary()

    def send_trap(self):
        self.generate()

        ntfOrg = ntforg.NotificationOriginator()

        ntfOrg.sendNotification(
        ntforg.CommunityData('public'),
        ntforg.UdpTransportTarget(('192.168.111.108', 5050)),
        'trap',
        ntforg.MibVariable('SNMPv2-MIB', 'sysLocation'),
        ('1.3.6.1.6.3.1.1.5.4', v2c.OctetString(self.data)))

        #print "Trap has been sent:" + ' ' + self.data

    def generate(self):
        ts = time.time()
        #st = datetime.datetime#.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        #dev_id = ('UA5120001RT','UA5120002RT','UA5120003RT','UA5120004RT')

        self.data = str(self.dev_cilly[ random.randint( 0,len(self.dev_cilly)-1 ) ]) +'|'+ str(self.dictionary[random.randint(0,13)])+'|'+str(ts)

    def getDictionary(self):
        with open("data/traps.txt",'r') as infile:
            for line in infile:
                key,value = line.split(':')
                self.dictionary[int(key)] = str(value).rstrip()

    def getDeviceCLLI(self):
        con = cx_Oracle.connect('orcdb/passw0rd@192.168.111.138/orcl')
        print "Connected"

        data = []
        cur = con.cursor()
        cur.execute("select ID from SYSTEM.DEVICE")
        #data = cur.fetchall()
        for item in cur.fetchall():
            #print item[0]
            data.append(item[0])
        return data

if __name__ == '__main__':
    obj = TrapGen()
    while(1):
        obj.send_trap()
        #time.sleep(random.randint(5,10))
        #obj.getDeviceCLLI()
