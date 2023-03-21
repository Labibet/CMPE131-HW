import time
def timestamp(func):
    def printDate():
        print(time.ctime())
        # Call func()
        func()        
    return printDate
        
