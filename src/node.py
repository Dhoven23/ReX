import tensorflow as tf 
import sys
import Numpy as np
import json
from pythonping import ping
from paramiko import SSHClient


class Node:

	ID = 0x0000
	ipv4 = ''
	ipv6 = ''
	dns = 2552552550
	pingTime = 0
	client = SSHCLient()
	isconnected = False
	isbusy = False

	def __init__(self, ID, ipv4, ipv6, dns):

		self.ID = ID
		self.ipv4 = ipv4
		self.ipv6 = ipv6
		self.dns = dns
		self.pingTime = ping(ipv4)

	def update(self, ID, ipv4, ipv6, dns)

		if(self.ID not ID):
			self.ID = ID
		if(self.ipv4 not ipv4):
			self.ipv4 = ipv4
		if(self.ipv6 not ipv6):
			self.ipv6 = ipv6
		if(self.dns not dns):
			self.dns = dns
		self.pingTime = ping(ipv4)

	def connect(self, ipv4, ID, password)
		self.client.connect(ipv4,username = ID, password = password)

