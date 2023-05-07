import threading

class MyThread(threading.Thread):
    def _init_(self, name):
        threading.Thread._init_(self)
        self.name = name
    def run(self):
        print("Thread {} is running ".format(self.name))
        
t1 = MyThread("1")
t2 = MyThread("2")
t1.start()
t2.start()
Footer