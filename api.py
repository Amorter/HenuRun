import leidian
import map
import myfrida
import numpy
import time
import math
from threading import Thread
from threading import Event
def shake(lendian:leidian.Leidian,event:Event):
    while(True):
        lendian.shake()
        if event.is_set():
            break


def start_run(ldconsole_dir,ld_dir,index,host,region,speed,event:Event):
    leidian1 = leidian.Leidian(ldconsole_dir,ld_dir,index)
    leidian1.runFridaServer(host)
    print("启动FridaServer中>>>请等待3秒")
    time.sleep(3)
    frida1 = myfrida.MyFrida(host)
    t2 = Thread(target=frida1.hook,args=(event,))
    t2.start()
    print("Hook创高校园中>>>请等待3秒")
    time.sleep(3)

    region = map.DongCao()
    t1 = Thread(target=shake,args=(leidian1,event,))
    t1.start()
    r1 = region.getNextPointN()
    print("加载完毕，请开始跑步")
    while(True):
        r2 = region.getNextPointN()
        distance = math.sqrt(math.pow(abs(r1[0] - r2[0]),2) + math.pow(abs(r1[1] - r2[1]),2))
        num = round(100*1000*distance/(speed/1))
        arr_x = numpy.linspace(r1[0],r2[0],num)
        arr_y = numpy.linspace(r1[1],r2[1],num)
        for p in range(num):
            leidian1.changelocation(str(arr_x[p]),str(arr_y[p]))
            if event.is_set():
                break
            time.sleep(1)

        r1 = r2
        if event.is_set():
            break 