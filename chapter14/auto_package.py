class AutoPackage():
    """
    A package to store a list of items until it fills up.
    When full, send all items to your destination.
    """

    def __init__(self, send_package=None, size=1000000):
        self.send_package = send_package
        self.size = int(size)

        self.package = []
    
    def add(self, item):
        self.package.append(item)

        if(self.size >= len(self.package)):
            self.send()

    def send(self):
        if(len(self.package) > 0 and self.send_package != None):
            self.send_package(self.package)
        
        self.package.clear()
