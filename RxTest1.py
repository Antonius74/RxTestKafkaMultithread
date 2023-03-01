import multiprocessing
import random
import time
from threading import current_thread
import rx
from rx.scheduler import ThreadPoolScheduler
from rx import operators as ops
# calculate cpu count, using which will create a ThreadPoolScheduler
thread_count = multiprocessing.cpu_count()
thread_pool_scheduler = ThreadPoolScheduler(thread_count)
print("Cpu count is : {0}".format(thread_count))
def adding_delay(value):
   #time.sleep(random.randint(5, 20) * 0.1)
   return value
# Task 1
rx.range(1, 50000).pipe(
   ops.map(lambda a: adding_delay(a)),
   ops.subscribe_on(thread_pool_scheduler)
).subscribe(
   lambda s: print("From Task 1: {0}".format(s)),
   lambda e: print(e),
   lambda: print("Task 1 complete")
)
# Task 2
rx.range(1, 50000).pipe(
   ops.map(lambda a: adding_delay(a)),
   ops.map(lambda a:  print("il mattino ha l'oro in bocca")),
   ops.subscribe_on(thread_pool_scheduler)
).subscribe(
   lambda s: print("From Task 2: {0}".format(s)),
   lambda e: print(e),
   lambda: print("Task 2 complete")
)
