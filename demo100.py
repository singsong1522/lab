import multiprocessing
import time
def worker():
    print('start to run')
    time.sleep(2)
    print('run finished')
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        print(f'now execute part:{i}')
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
    print('result=',jobs)
    time.sleep(3)
    print('result=', jobs)

