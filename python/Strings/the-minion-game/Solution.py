def minion_game(string):
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in ['A', 'E', 'I', 'O', 'U']:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
            
    if kevin > stuart:
        print(f'Kevin {kevin}')
    elif stuart > kevin:
        print(f'Stuart {stuart}')
    else:
        print('Draw')
    
if __name__ == '__main__':
    s = input()
    minion_game(s)