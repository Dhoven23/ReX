# THIS CODE DOES NOT WORK NOR IS IT INTENDED TO
#
import tensorflow as tf 
import sys
import numpy as np
import json
from pythonping import ping
from paramiko import SSHClient


class Node:

	ID = 0x0000
	ipv4 = ''
	ipv6 = ''
	dns = 2552552550
	pingTime = 0
	client = SSHClient()
	isconnected = False
	isbusy = False

	def __init__(self, ID, ipv4, ipv6, dns):

		self.ID = ID
		self.ipv4 = ipv4
		self.ipv6 = ipv6
		self.dns = dns
		self.pingTime = ping(ipv4)

	def update(self, ID, ipv4, ipv6, dns):

		if not (self.ID == ID):
			self.ID = ID
		if not (self.ipv4 == ipv4):
			self.ipv4 = ipv4
		if not (self.ipv6 == ipv6):
			self.ipv6 = ipv6
		if not (self.dns == dns):
			self.dns = dns
		self.pingTime = ping(ipv4)

	def connect(self, ID, password):
		self.client.connect(self.ipv4,
			username = ID, 
			password = password
			)