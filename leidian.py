from subprocess import run
import subprocess
class Leidian:
    #ldconsole可执行文件目录
    ldconsole_dir = ""
    ld_dir = ""
    index = 0

    def __init__(self,ldconsole_dir,ld_dir,index):
        self.ldconsole_dir = ldconsole_dir
        self.ld_dir = ld_dir
        self.index = index

    def shake(self):
        run(self.ldconsole_dir + " action --index " + str(self.index) + " --key call.shake --value null")

    def changelocation(self,x,y):
        run(self.ldconsole_dir + " action --index " + str(self.index) + " --key call.locate --value " + x + "," + y)

    def runFridaServer(self,host):
        port = host.split(':')[1]
        run(self.ld_dir + ' -s ' + str(self.index) + ' chmod +x /data/local/tmp/www"')
        print("修改权限",end='\n')
        run(self.ld_dir + ' -s ' + str(self.index) + ' nohup /data/local/tmp/www -l ' + host + " >/dev/null 2>&1 &")
        print("启动frida server",end='\n') 
        run("adb -s emulator-" + str(self.index*2 + 5554) + " forward tcp:" + port + " tcp:" + port)
        print("tcp端口映射",end='\n')