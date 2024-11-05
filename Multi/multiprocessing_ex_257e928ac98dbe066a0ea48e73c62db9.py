from multiprocessing import Process, cpu_count
import time
import os
print(cpu_count())
class MuchCPU(Process):
 def run(self) -> None:
     print("Its running")
     x=os.getpid()
     print("os pid",x)
     print(f"OS PID {os.getpid()}")
     s = sum( 2*i+1 for i in range(1) )
if __name__ == "__main__":
    workers = [MuchCPU() for f in range(cpu_count())]
    t = time.perf_counter()
    print("Its running")
    x=os.getpid()
    print("os pid",x)
    for p in workers:
        p.start()
    for p in workers:
         p.join()
         #time.sleep(5)
    print(f"work took {time.perf_counter() - t:.3f} seconds")


     
