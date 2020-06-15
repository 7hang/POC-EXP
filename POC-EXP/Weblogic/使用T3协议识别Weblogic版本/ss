#coding=utf-8
import sys
import socket
from socket import error as socket_error
import urllib

'''
'''

def t3conn(host, port):
        try:
            server_address = (host, port)
            #print 'INFO: Attempting Connection: ' + str(server_address)
            sock = socket.create_connection(server_address, 4)
            sock.settimeout(5)
            headers = 't3 10.3.6\nAS:255\nHL:19\n\n'
            sock.sendall(headers)
            data = ""

            try:
                data = sock.recv(1024)
            except socket.timeout:
                print 'ERROR: Socket Timeout Occurred: ' + str(host) + ':' + str(port) + '\n'

            sock.close()
            return data
        except socket_error:
            print 'ERROR: Connection Failed: ' + str(host) + ':' + str(port) + '\n'
            return ""


def parseURL(url):
    protocol, s1 = urllib.splittype(url)
    host, s2=  urllib.splithost(s1)
    host, port = urllib.splitport(host)

    if port == None and protocol == 'https':
        port = 443
    elif port == None and protocol == 'http':
        port = 80

    return protocol,host,port

def weblogic(url):
    for i in range(0, 10):
        protocol,host,port = parseURL(url)
        data = t3conn(host, port)
        if data.strip() == 'HELO':
            print 'INFO: Sever only returned HELO, retrying to get server version.'
            continue

        if data == "":
            break

        print data

        if 'HELO' in data:
            found_weblogic_version = data[5:13]

            print '[+] version: %s' % found_weblogic_version 
            #print '[+] result: %s' % data
            break

def poc(url):
    pass

if __name__ == '__main__':
    weblogic(sys.argv[1])
