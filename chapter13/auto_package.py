import gc

class AutoPackage():
    """
    A package to store a list of items until it fills up.
    When full, send all items to your destination.
    """

    def __init__(self, send=None, size=1000000):
        self.send = send
        self.size = int(size)

        self.package = []
    
    def add(self, item):
        self.package.append(item)

        if(self.size == len(self.package)):
            self.send_package()

    def send_package(self):
        if(len(self.package) > 0 and self.send != None):
            self.send(self.package)
        
        self.package = []

        gc.collect() # garbage collector
