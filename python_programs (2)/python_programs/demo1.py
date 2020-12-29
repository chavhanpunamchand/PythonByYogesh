import threading
import time

def task1():
    for item in range(3):
        time.sleep(1)
        #print(threading.current_thread().getName(),": ",item)
    print(threading.current_thread().getName(), " Completed ")

def task2():
    for item in range(10):
        time.sleep(1)
        #print(threading.current_thread().getName(),": ",item)
    print(threading.current_thread().getName(), " Completed ")

def task3():
    for item in range(20):
        time.sleep(1)
        print(threading.current_thread().getName(),": ",item)
    print(threading.current_thread().getName(), " Completed ")
if __name__ == '__main__':

    t1 = threading.Thread(target=task1,name="N1")  #  3
    t2 = threading.Thread(target=task2,name="N2")   # 6
    t3 = threading.Thread(target=task3, name="D",daemon=True) # 20 sec

    t1.start()
    t2.start()
    t3.start()

    #t1.join()
    #t2.join()
    #t3.join() # not going to wait for this--> t3. stops-->

    #print('Main Completed ')



import sys
sys.exit(0)



class Product:
    def __init__(self,pid,pnm):
        self.prodName = pnm
        self.prodId = pid

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''({self.prodId},{self.prodName})  ,'''


import time

def generate_productId():   # generator
    pid = 110
    while True :
        pid = pid + 1
        yield pid
genr = generate_productId()

def create_product():
    pid = next(genr)
    return Product(pid,"XXXX{}".format(pid))



product_inventory = []
def product_manf():
    while True:
        prod = create_product()
        #print(threading.current_thread().name +" : ",prod)
        product_inventory.append(prod)
        print(threading.current_thread().name + " :({}) ".format(len(product_inventory)) , product_inventory[::-1])
        time.sleep(2)

def sale_product():  #
    while True:
        if product_inventory:
            prod = product_inventory.pop(0)
            print(threading.current_thread().name + " Consumed : ", prod)
            time.sleep(5)
        else:
            print('Consumer : since products out of stock -- waiting for 5 seconds')
            time.sleep(20)

import threading
if __name__ == '__main__':
    t1 = threading.Thread(target=product_manf,name="Producer1")
    t1.start()

    t11 = threading.Thread(target=product_manf, name="Producer2")
    t11.start()


    t2 = threading.Thread(target=sale_product, name="Customer")
    t2.start()





import sys
sys.exit(0)









import threading
class A(threading.Thread):

    def run(self):
        pass



def fun():
    pass

if __name__ == '__main__':
    t1 = threading.Thread(target=fun) # thread -- subprocess/lightweight--> task -->
    t2 = A()    # run method madhe -->

    t1.start()
    t2.start()

