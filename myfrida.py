import frida  #导入frida模块
import time   #导入sys模块
from threading import Event
class MyFrida:
    host = ''
    def __init__(self,host):
        self.host = host
        
    def hook(self,event:Event):
        jscode = """
    Java.perform(()=>{
    let location = Java.use('android.location.Location') 
    location.getSpeed.implementation = ()=>{
        return 4.2
    }
})
"""
        manager = frida.get_device_manager()
        device= manager.add_remote_device(self.host)
        print(self.host,end='\n')
        script = device.attach("创高体育").create_script(jscode) #创建js脚本
        script.load() #加载脚本
        while True:
            if event.is_set():
                break