#!/usr/bin/env python

import ConfigParser

class ConfManeger():
	def __init__(self):
		self.config = ConfigParser.RawConfigParser()
		self.CreateConfFile()

	def CreateConfFile(self):
		#create config file
		self.config.add_section('logging')
		#self.config.set('logging', 'log_lvl', '/data/xml/device_info.xml')
		self.config.set('logging', 'format', '')
		self.config.set('logging', 'insert_log', 'data/insert.log')
		self.config.set('logging', 'trap_log', 'data/trap.log')

		self.config.add_section('trap')
		self.config.set('trap', 'ip', "192.168.111.118")
		self.config.set('trap', 'trap_list', 'data/traps.txt')
		self.config.set('trap', 'connection', 'orcdb/passw0rd@192.168.111.138/orcl')

		self.config.add_section('network_maneger')
		self.config.set('network_maneger', 'output_file', 'data/device_info.txt')
		self.config.set('network_maneger', 'xml_file', 'data/xml/device_info.xml')
		self.config.set('network_maneger', 'device_list_file', 'src/devices.txt')

		with open('conf/configs.cfg', 'wb') as configfile:
			self.config.write(configfile)

	def PrintConfFile(self):
		self.sections = self.config.sections()
		for section in self.sections:
			print '-----------------------------------------------------------------------'
			print 'Section: ' + section
			items = self.config.items(section)
			for item in items:
				print item 
		print '-----------------------------------------------------------------------'
	
	def getLogFormat(self):
		return self.config.get('logging', 'format')

	def getInsertLog(self):
		return self.config.get('logging', 'insert_log')

	def getTrapLog(self):
		return self.config.get('logging', 'trap_log')

	def getTrapIp(self):
		return self.config.get('trap', 'ip')

	def getTrapList(self):
		return self.config.get('trap', 'trap_list')

	def getDBConnection(self):
		return self.config.get('trap', 'connection')

	def getOutputFile(self):
		return self.config.get('network_maneger', 'output_file')

	def getDeviceInfoFile(self):
		return self.config.get('network_maneger', 'xml_file')

	def getDevicesFile(self):
		return self.config.get('network_maneger', 'device_list_file')

