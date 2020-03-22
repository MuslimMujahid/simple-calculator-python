import re, collections

string = '2+cos(2)+sin(90)%cos(2+tan(30))'
string = re.findall('[cos|sin|tan]+|[\d.]+|[)(*-/+^v%]', string)
print(string)