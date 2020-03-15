from parser import Parser
from Process import Process

print(Process(Parser("2+2").expression()).result())
# print(Parser('2+2*8').expression())
