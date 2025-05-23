import multiprocessing
import time
import os

def SumEven(no):
    print("PID of SumEven task is:",os.getpid())
    print("PPID of SumEven task is:",os.getppid())  #PID of main 101
    sum = 0
    for i in range(2,no+1,2):
        sum = sum + i
    print(sum)

def SumOdd(no):
    print("PID of SumOdd task is:",os.getpid())
    print("PPID of SumOdd task is:",os.getppid())   #PID of main 101
    sum = 0    
    for i in range(1,no+1,2):
        sum = sum + i
    print(sum)

def main():

    print("Demonstration of parallel execution:")

    print("PID of main process is: ",os.getpid())    #PID 101

    start_time = time.time()

    T1 = multiprocessing.Process(target= SumEven,args=(9000000,))
    T2 = multiprocessing.Process(target= SumOdd,args=(9000000,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    end_time = time.time()

    print("Time required for execution:",end_time - start_time)

    print("End of main")


if __name__ == "__main__":
    main()
