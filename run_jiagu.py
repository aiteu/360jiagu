#!/usr/bin/python
# _*_ coding: UTF-8 _*_
#360 jiagu script

import os;

def exec_360_jiagu():
    os.chdir('/home/david/360gu/jiagu')
    os.system('java -jar jiagu.jar -login account pass')
    jiagu_cmd = 'java -jar jiagu.jar -jiagu /home/david/360gu/bbbao_533.apk /home/david/360gu/apk_jiagu -autosign'
    result = os.system(jiagu_cmd)
    if not result:
        print "====" + str(result) + "  success"
    else:
        print "----failed"
    return


exec_360_jiagu();
