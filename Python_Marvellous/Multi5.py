import threading

def Display(value1,value2):
    print("Inside Display",value1,value2)
    

def main():
    print("Inside main")
    T1 = threading.Thread(target=Display, args = (11,21))   #Create thread (Assign a target to thread for Display function)
    T1.start()                                            #To run the thread



if __name__ == "__main__":
    main()
