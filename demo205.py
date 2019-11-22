import multiprocessing,time,random
from datetime import datetime

def daemon():
    name = multiprocessing.current_process().name
    print(f"({datetime.now()}[{name}]start work")
    time.sleep(random.randint(1,10))
    print(f"({datetime.now()}[{name}]stop work")
if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon',target=daemon)
    d.daemon=True
    print(f"({datetime.now()}prepare work")
    d.start()
    d.join()
    print(f"({datetime.now()}program terminated")
