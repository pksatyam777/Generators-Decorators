def wrapper(f):
    def fun(l):
        f('+91 {} {}'.format(n[-10:-5], n[-5:]) for n in l)
    return fun

@wrapper
def sort_phone(l):
    print('\n Output', *sorted(l), sep='\n')
if __name__ == '__main__':
    l = [input() for _ in range(int(input("No. of mobile phone No. ")))]
    sort_phone(l)
