def swap_case(s):
    result = ''
    for case in s:
        if case.islower():
            result += case.upper()
            continue
        result += case.lower()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)