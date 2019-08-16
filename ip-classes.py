# -*- coding: utf-8 -*-
#from __future__ import unicode_literals #make python2 act as python3 unicode #this causes ip.split(".") failed.

#Modifed from https://github.com/zulu-caPWN/IP-Classes

import sys
PY3 = sys.version_info[0] >= 3
if PY3:
    pass
else:
    input = raw_input

import readline #to make input() edit-able by LEFT key
import argparse
arg_parser = argparse.ArgumentParser(description='Baiwanzy Downloader')
args = ""

def quit(msgs, exit=True):
    if not isinstance(msgs, list):
        msgs = [msgs]
    for msg in msgs:
        print('\x1b[1;41m%s\x1b[0m\x1b[K' % msg)
    if exit:
        print('\x1b[1;41m%s\x1b[0m\x1b[K' % 'Abort.')
        sys.exit()

#comment_May_22_2014: https://networkengineering.stackexchange.com/questions/8025/determining-the-network-class-of-an-ip-address#comment13244_8025
#IPv4 address classes have been deprecated 20 years ago. Since then CIDR (classless inter-domain routing) is used. Classes don't exist anymore

#
''' https://stackoverflow.com/questions/34119940/ip-addressing-network-prefix-help-understanding
Classful networking was deprecated over 20 years ago, and I don't understand why it is still taught since nothing uses it anymore.
The network class has noting to do with the network mask, but the classes have default masks.
    Class A network addresses start with the first bit as 0, giving you 0.0.0.0 to 127.255.255.255 as the Class A address range. 
        - The default mask for Class A networks is 255.0.0.0.
    Class B network addresses start with the first two bits as 10, giving you 128.0.0.0 to 191.255.255.255 as the Class B range. 
        - The default mask for Class B networks is 255.255.0.0.
    Class C network addresses start with the first three bits as 110, giving you 192.0.0.0 to 223.255.255.255 as the Class C range. 
        - The default mask for Class C addresses is 255.255.255.0.
    Class D addresses start with the first four bits as 1110, giving you the 224.0.0.0 to 239.255.255.255 as the Class D range. 
        - Class D addresses are used for multicast, and multicast doesn't normally use masks since multicast groups are subscribed to individually.
    Class E addresses start with the first four bits as 1111, giving you the 240.0.0.0 to 255.255.255.255 as the Class E range. 
        - Class E addresses are reserved/experimental so they don't have a default mask
        -... , except for the Limited Broadcast address of 255.255.255.255 which is a host address with the mask of 255.255.255.2555.
'''

def ip_class(ip):

    if args.d:
        print( "You entered: %s" % ip )
    stripped_ip = ip.split(".")
    if len(stripped_ip) != 4:
         quit( "Invalid IP, try again" )

    oct1 = stripped_ip[0]
    oct2 = stripped_ip[1]
    oct3 = stripped_ip[2]
    oct4 = stripped_ip[3]
    if int(oct1) >=256 or int(oct2) >=256 or int(oct3) >=256 or int(oct4) >= 256:
        quit( "Invalid IP, try again" )

    if args.d:
        print( type(oct1) )
        print( "Individual Octets are ", oct1, oct2, oct3, oct4 )
        print( "Octet Lengths are", int(len(oct1)), int(len(oct2)), int(len(oct3)), int(len(oct4)) )
        print( type(stripped_ip) )

    # A class, before the private 10.x.x.x range
    if int(oct1) in range(1,10):
        print( "%s is an A class IP" % ip )
    # Private A class
    elif int(oct1) == 10:
        print( "%s is a Private A class IP" %ip )
    # remainder of A class after private 10.x.x.x range
    elif int(oct1) in range(11, 127):
        print( "%s is an A class IP" % ip )
    # loopback
    elif int(oct1) == 127:
        print( "%s is a Localhost (Loopback) IP" % ip )
    # APIPA
    elif int(oct1) == 169 and  int(oct2) == 254:
        print( "%s is an APIPA IP" %ip )
    # B Class, beginning of B class 128.x.x.x thru 171.x.x.x
    elif int(oct1) in range(128,172):
        print( "%s is a B class IP" % ip )
    # B class 172.0.x.x thru 172.15.x.x
    elif int(oct1) == 172 and int(oct2) in range(0,16):
        print( "%s is a B class IP" %ip )
    # Private B class 172.16.x.x thru 172.31.x.x
    elif int(oct1) == 172 and int(oct2) in range(16,32):
        print( "%s is a Private B class IP" % ip )
    # Resuming B class after the private 172.16.x.x thru 172.31.x.x range
    elif int(oct1) == 172 and int(oct2) in range(32,256):
        print( "%s is a B class IP" %ip )

    # C class, before the private ip range, so 192.0-167
    elif int(oct1) == 192 and int(oct2) in range(0, 168):
        print( "%s is a C class IP" % ip )
    # The entire Private C class, 192.168.all.all
    elif int(oct1) == 192 and int(oct2) == 168 :
        print( "%s is a private C class IP" % ip )
    # C class, finishing off 192.169.x.x thru 192.255.x.x
    elif int(oct1) == 192 and int(oct2) in range(169, 256):
        print( "%s is a C Class IP" % ip )
    # C class, remainder of 193.x.x.x thru 223.255.255.255
    elif int(oct1) in range(193, 224):
        print( "%s is a C class IP (193.xxx - 223)" % ip )
    # D class
    elif int(oct1) in range(224, 240):
        print( "%s is a D class IP (Multicast)" %ip )
    # E class
    elif int(oct1) in range(240, 255):
        print( "%s is an E class IP (Experimental)" % ip )
    else:
        print( "%s is not a valid IP" % ip )

if __name__ == "__main__":
    arg_parser.add_argument('-d', action='store_true', help='Debug by printing log.')
    arg_parser.add_argument('ip', nargs='?', help='Numeric ip') 
    args, remaining  = arg_parser.parse_known_args()
    if args.ip:
        ip = args.ip
    else:
        if PY3:
            ip = input('ip: ').strip()
        else: #https://bugs.python.org/issue7768
            ip = input('ip: '.encode('utf-8')).strip()
    ip_class(ip)

