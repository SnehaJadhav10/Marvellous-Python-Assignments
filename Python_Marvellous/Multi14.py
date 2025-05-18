import os
import time
import multiprocessing

def fun(no):
    print("PID is:",os.getpid())
    sum = 0
    for i in range(1,no):
        sum = sum + (i*i*i)
    return sum


def main():
    
    start_time = time.time()

    Data = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]
    result = []
    
    p = multiprocessing.Pool()
    result = p.map(fun,Data)

    p.close()
    p.join()  # join is used for waiting until process is completed

    print(result)

    end_time = time.time()

    print("Time required for execution:",end_time - start_time)


if __name__ == "__main__":
    main()