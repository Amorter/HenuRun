import subprocess
from subprocess import run
import time
class MyADB:
    device = ''
    def __init__(self,device):
        self.device = device
        time.sleep(0.5)
        run("adb devices",stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        
    def runFridaServer(self,host):
        port = host.split(':')[1]
        run('adb shell su -c chmod +x /data/local/tmp/www',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        run('adb shell su -c nohup /data/local/tmp/www -l ' + host + " &",stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print("启动frida server")
        run('adb forward tcp:' + port + ' tcp:'+port,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print("tcp端口映射")