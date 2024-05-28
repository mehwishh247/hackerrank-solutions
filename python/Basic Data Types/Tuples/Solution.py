if __name__ == '__main__':
    n = int(input())
    t = map(int, input().split())
    
    print(hash(t))


    '''
    The above solution may not work since HackerRank have hard coded
    there answers while the hash function produce a different value 
    depending on which method is used to create a immutable tuple. It also
    change the resulting value over time.

    The following solution (using list comprehension) creates the closest
    value to the current result on HackerRank: 

    n = int(input())
    t = tuple[]
    
    print(hash(t))
    
    Your Output    : 3713080549409410656
    Expected Output: 3713081631934410656


    '''