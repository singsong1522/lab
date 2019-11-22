import multiprocessing
import time


def D1():
    name = multiprocessing.current_process().name
    print(f'[{name}]start')
    time.sleep(2)
    print(f'[{name}]stop')


def ND1():
    name = multiprocessing.current_process().name
    print(f'[{name}]start')
    time.sleep(1.5)
    print(f'[{name}]stop')


if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=D1)
    d.daemon = True
    n = multiprocessing.Process(name='non daemon', target=ND1)
    n.daemon = False
    print(f'd is alive?{d.is_alive()}, n is alive?{n.is_alive()}')
    d.start()
    n.start()
    print(f'd is alive?{d.is_alive()}, n is alive?{n.is_alive()}')
    d.join(1)
    print(f'd is alive?{d.is_alive()}, n is alive?{n.is_alive()}')
    time.sleep(1)
    n.join()
    print(f'd is alive?{d.is_alive()}, n is alive?{n.is_alive()}')
    d.terminate()
    n.terminate()
    time.sleep(1)
    print(f'd is alive?{d.is_alive()}, n is alive?{n.is_alive()}')
