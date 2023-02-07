import re

with open("./names.txt") as f:
    data = f.readlines()
    print(data)
    f.close()

twitter= re.compile('(@[A-Za-z0-9]+)$')

# only gets twitter handle. need to finish getting the names. 

# ([A-Z][a-zA-Z]+)([A-Z][a-zA-z]+)
# print(pattern)
for tweet in data:
    ch1 = twitter.search(tweet)
    if ch1:
        print('\n',f"{ch1.group(1)}")
   
    # else:
    #     print('None')