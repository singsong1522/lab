import multiprocessing,time

def daemon():
    pName =multiprocessing.current_process().name
    print('[%s]Daemon:start to work'%pName)
    time.sleep(5)
    print('[%s]Daemon:stop to work'%pName)

def nonDaemon():
    pName =multiprocessing.current_process().name
    print('[%s]Normal:start to work'%pName)
    time.sleep(5)
    print('[%s]Normal:stop to work'%pName)
if __name__ == '__main__':
    d1 = multiprocessing.Process(name='daemon',target=daemon)
    d1.daemon=True
    d2 = multiprocessing.Process(name='NonDaemon',target=nonDaemon)
    d2.daemon=False
    d1.start()
    #time.sleep(1)
    d2.start()
    time.sleep(5)
    d1.join()