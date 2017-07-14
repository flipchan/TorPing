#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#/*
#* ----------------------------------------------------------------------------
#* "THE BEER-WARE LICENSE" (Revision 42):
#* <flipchan@riseup.net> wrote this file. As long as you retain this notice you
#* can do whatever you want with this stuff. If we meet some day, and you think
#* this stuff is worth it, you can buy me a beer in return Filip Kälebo
#* ----------------------------------------------------------------------------
#*/


#coded by flipchan inspired by(and a special thanks to) the research done by Eric Michaud, Thomas Olafsson and Mihai.

from stem.control import Controller
from sys import argv
import sys
#btw u must enable controll port in /etc/tor/torrc

#print argv[1]
#print argv

#remove bogus stuff




def help_msg():
	print 'TorPing by flipchan'
	print 'make sure you have enabled controll port 9051 in /etc/tor/torrc'
	print 'example usage:'
	print 'python tor_ping.py http://3g2upl4pq6kufc4m.onion simple'
	print 'python tor_ping.py http://3g2upl4pq6kufc4m.onion advanced'
	print 'python tor_ping.py <onion> <simple/advanced>'

def display_info(c):
	print 'Public Key: ' + str(c['_entries']['permanent-key'][0][2])
	print 'Publication time: ' + str(c['_entries']['publication-time'][0][0])
	print 'Signature: ' + str(c['_entries']['signature'][0][2])
	print 'rendezvous service descriptor: ' + str(c['_entries']['rendezvous-service-descriptor'][0])
	print 'Version: ' + str(c['_entries']['version'][0][0])
	

try:
	if len(argv) < 3:
			help_msg()
	else:
		hstocheck = str(argv[1]).replace('.onion', '').replace('https://', '').replace('http://', '')
		if not len(hstocheck) == 16:
			print 'invalid .onion'
		else:		
			print 'checking ' + argv[1]#hstocheck
      b = Controller.from_port(port = 9051)
			b.authenticate()
# descriptor of duck-duck-go's hidden service (http://3g2upl4pq6kufc4m.onion)
      c = b.get_hidden_service_descriptor(hstocheck).__dict__
			print 'checked:'
			print hstocheck
			print 'the hiddenservice is up'	
			if argv[2] == 'advanced':
				display_info(c)
			else:#verify the simple string input ... yes yes ..
				pass
			b.close()
except Exception:
	hstocheck = str(argv[1]).replace('https://', '').replace('http://', '')
	a = 'No running hidden service at ' + hstocheck
	print a 
	d = str(sys.exc_info()[1])
	if a == d:
		print 'the hidden service is down'
	else:
		print sys.exc_info()	
	b.close()
#stem returns a exception if it doesnt find it
			#>>> b.get_hidden_service_descriptor('3g2upl4pq6kufc45.onion').__dict__
			#Traceback (most recent call last):
				#File "<stdin>", line 1, in <module>
				#File "/usr/local/lib/python2.7/dist-packages/stem/control.py", line 414, in wrapped
					#raise exc
			#stem.DescriptorUnavailable: No running hidden service at 3g2upl4pq6kufc45.onion
				
			#except Exception:
				#print 'the hiddenservice is down'
