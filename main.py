import api
import map
from threading import Thread
from threading import Event
import time

ldconsole_dir = "D:\OtherTools\leidian\LDPlayer9\ldconsole.exe"
ld_dir = "D:\OtherTools\leidian\LDPlayer9\ld.exe"
t1 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,0,h1 := '127.0.0.1:18231',m1 := map.DongCao(),s1 := 5,e1 := Event(),))
t2 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,1,h2 := '127.0.0.1:18232',m2 := map.DongCao(),s2 := 5,e2 := Event(),))
t3 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,2,h3 := '127.0.0.1:18233',m3 := map.DongCao(),s3 := 5,e3 := Event(),))
t4 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,3,h4 := '127.0.0.1:18234',m4 := map.DongCao(),s4 := 5,e4 := Event(),))
t5 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,4,h5 := '127.0.0.1:18235',m5 := map.DongCao(),s5 := 5,e5 := Event(),))
t6 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,5,h6 := '127.0.0.1:18236',m6 := map.DongCao(),s6 := 5,e6 := Event(),))
t7 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,6,h7 := '127.0.0.1:18237',m7 := map.DongCao(),s7 := 5,e7 := Event(),))
t8 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,7,h8 := '127.0.0.1:18238',m8 := map.DongCao(),s8 := 5,e8 := Event(),))
t9 = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,8,h9 := '127.0.0.1:18239',m9 := map.DongCao(),s9 := 5,e9 := Event(),))
t10= Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,9,h10 := '127.0.0.1:18240',m10 := map.DongCao(),s10 := 5,e10 := Event(),))

es = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10];hs = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10];ms = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10];ss = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()
# t9.start()
# t10.start()

time.sleep(10)

print("可以输入线程号重启线程")
while True:
    index = int(input())
    es[index-1].set()
    print("重启中，请等待3秒")
    time.sleep(3)
    es[index-1] = Event()
    tx = Thread(target=api.start_run,args=(ldconsole_dir,ld_dir,index-1,hs[index-1],ms[index-1],ss[index-1],es[index-1],))
    tx.start()