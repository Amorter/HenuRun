import api
import map
from threading import Thread
t1 = Thread(target=api.start_run,args=("D:\OtherTools\leidian\LDPlayer9\ldconsole.exe","D:\OtherTools\leidian\LDPlayer9\ld.exe",0,'127.0.0.1:18231',map.DongCao(),5,))
t2 = Thread(target=api.start_run,args=("D:\OtherTools\leidian\LDPlayer9\ldconsole.exe","D:\OtherTools\leidian\LDPlayer9\ld.exe",1,'127.0.0.1:18232',map.DongCao(),5,))
t3 = Thread(target=api.start_run,args=("D:\OtherTools\leidian\LDPlayer9\ldconsole.exe","D:\OtherTools\leidian\LDPlayer9\ld.exe",2,'127.0.0.1:18233',map.DongCao(),5,))
#t4 = Thread(target=api.start_run,args=("D:\OtherTools\leidian\LDPlayer9\ldconsole.exe","D:\OtherTools\leidian\LDPlayer9\ld.exe",3,'127.0.0.1:18234',map.DongCao(),5,))
#t5 = Thread(target=api.start_run,args=("D:\OtherTools\leidian\LDPlayer9\ldconsole.exe","D:\OtherTools\leidian\LDPlayer9\ld.exe",4,'127.0.0.1:18232',map.DongCao(),5,))

t1.start()
t2.start()
t3.start()
#t4.start()
#t5.start()