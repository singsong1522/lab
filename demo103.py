import multiprocessing
import time

def worker():
    name = multiprocessing.current_process().name
    print('[%s] start' % name)
    time.sleep(4)
    print('[%s] stop' % name)

def my_service():
    name = multiprocessing.current_process().name
    print('[%s] start' % name)
    time.sleep(6)
    print('[%s] stop' % name)

if __name__ == '__main__':
    service = multiprocessing.Process(name='bg service',
                                      target=my_service)
    s1 = multiprocessing.Process(name='worker 1', target= worker)
    s2 = multiprocessing.Process(target = worker)
    s1.start()
    s2.start()
    service.start()
