words = open(0,'r').read().split('\n')
for word in words:
    if word=='0' :
        break
    print('yes' if word == word[::-1] else 'no')