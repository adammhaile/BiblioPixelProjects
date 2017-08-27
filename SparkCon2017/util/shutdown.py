#!/usr/bin/env python3

from urllib import request
from ips import ip_list
import os

for ip in ip_list:
    try:
        resp = request.urlopen('http://{}:5000/stop'.format(ip))
        print(resp.read())
        print('Shutting down {}'.format(ip))
        os.system("ssh pi@{} 'sudo shutdown now'".format(ip))
    except Exception as ex:
        print(ex)
