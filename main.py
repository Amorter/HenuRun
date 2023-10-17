import api
import map
from threading import Thread
ldconsole_dir = "D:\OtherTools\leidian\LDPlayer9\ldconsole.exe"
ld_dir = "D:\OtherTools\leidian\LDPlayer9\ld.exe"
t1 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,0,'127.0.0.1:18231',map.DongCao(),5,))
t2 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,1,'127.0.0.1:18232',map.DongCao(),5,))
t3 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,2,'127.0.0.1:18233',map.DongCao(),5,))
t4 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,3,'127.0.0.1:18234',map.DongCao(),5,))
t5 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,4,'127.0.0.1:18235',map.DongCao(),5,))
t6 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,0,'127.0.0.1:18236',map.DongCao(),5,))
t7 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,1,'127.0.0.1:18237',map.DongCao(),5,))
t8 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,2,'127.0.0.1:18238',map.DongCao(),5,))
t9 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,3,'127.0.0.1:18239',map.DongCao(),5,))
t10= Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,4,'127.0.0.1:18240',map.DongCao(),5,))


t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()
# t9.start()
# t10.start()