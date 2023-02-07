import re

with open("./regex_test.txt") as f:
    data = f.readlines()
    print(data)
    f.close()

pattern1= re.compile('([A-J][a-z]+\sP|J[a-z]+\sA[a-z]+) ([G-W][a-z]+)')
pattern2= re.compile('([A-E][a-z]+) ([L-N][a-z]+)')

# print(pattern)
for famous in data:
    match1 = pattern1.search(famous)
    match2 = pattern2.search(famous)
    if match1:
        print('\n',f"{match1.group(1)} {match1.group(2)}")
    elif match2:
        print('\n',f"{match2.group(1)} {match2.group(2)}")
    else:
        print('None')

