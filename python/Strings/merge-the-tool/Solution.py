from collections import OrderedDict

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(''.join(OrderedDict.fromkeys(string[i:i+k])))


'''
The following function also works but the above function is
more optimized and works quicker

def merge_the_tools(string, k):        
    for i in range(0, len(string), k):
        sub = ''
        for j in string[i:i+k]:
            if j not in sub:
                sub += j
                
        print(sub)

'''
        
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)