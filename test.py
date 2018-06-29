import re
x = {}
x['a'] = 'b', 'c'
print(re.sub(r'[()]',"", str(x['a']).replace("'","")))