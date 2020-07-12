#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import sys
import requests
import threading
from queue import Queue

def elastic_river(host):
    urlA = 'http://%s/_cat/indices' % host
    urlB = 'http://%s/_river/_search' % host
    try:
        content = requests.get(urlA, timeout=5, allow_redirects=True, verify=False).content

        if "_river" in content.decode():
            print("%s is vul" % host)

            with open('success.txt', 'a') as af:
                af.write(urlB + '\n')
    except Exception as e:
        print (e)


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global queue
        while not queue.empty():
            ip = queue.get()
            elastic_river(ip)

if __name__ == "__main__":
    queue = Queue()

    f = open('ip.txt', "r")
    fileLists = f.readlines()
    for ip in fileLists:
        ip = ip.strip()
        queue.put(ip)

    for i in range(99):
        c = MyThread()
        c.start()
