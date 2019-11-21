import logging
class LoggingDictionary(dict):
    def __setitem__(self, key, value):
        logging.info(f'setting{value}to{key}')
        super().__setitem__(key, value)
logging.basicConfig(filename='logs\\demo83.log',
                    level=logging.INFO)
l1=LoggingDictionary()
l1['ken']='iOS'
l1['frank']='oracle'
print(l1)