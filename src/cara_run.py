from Parser import Parser
from Process import Process
import queue
import re, collections

# print(Process("v9").result())
text = "2u+2*s(5+10)"
text = re.sub('[\d.]+|[)(*-/+^v]', '', text)
print(len(text)) 