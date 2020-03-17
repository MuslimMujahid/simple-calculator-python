from Parser import Parser
from Process import Process
import queue

# print(Process("v9").result())
Q = queue.LifoQueue()
Q.put(2)
Q.put(3)
Q.put(5)
Q.put(7)
Q.put(4)
print(Q.qsize())
print(Q.get())
print(Q.qsize())