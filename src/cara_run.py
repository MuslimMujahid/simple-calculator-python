from parser import Parser
from Process import Process

print(Process(Parser("2+(2/2)").expression()).result())
