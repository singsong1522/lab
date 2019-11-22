import multiprocessing,time,random

def daemon():
    name = multiprocessing.current_process().name
    print('[%s]start to work'%name)
    time.sleep(random.randint(1,10))
    print('[%s]stop to work'%name)
if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon',target=daemon)
    d.daemon=True
    print('prepare start')
    d.start()
    d.join()
    print('program terminated')
