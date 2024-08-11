def designer(N, M):
    pattern = '.|.'
    mat = ''
    welcome = 'WELCOME'.center(M, '-')
    
    for i in range(N-2, 0, -2):
        line = pattern * i
        mat += line.center(M, '-') + '\n'
    
    result = mat[::-1] + '\n' + 'WELCOME'.center(M, '-') + '\n' +  mat
    return result.strip()

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    doormat = designer(N, M)
    print(doormat)