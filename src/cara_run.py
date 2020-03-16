from Parser import Parser
from Process import Process

print(Process(Parser("25v5").expression()).result())
# print(Process(Parser("3*5+(10^2)").expression()).result())
