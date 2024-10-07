import sys

def main():
    n_length, m_length = input().split( )
    n_elements = input().split()
    list_a = input().split()
    set_a = set(list_a)
    list_b = input().split()
    set_b = set(list_b)
    checks(list_a,set_a,list_b,set_b, n_elements,n_length,m_length)
    print(happiness(n_elements,set_a,set_b))

def checks(list_a,set_a,list_b,set_b, n_elements,n_length,m_length):
    if len(list_a) != len(set_a) or len(list_b) != len(set_b):
        sys.exit('At least one of your sets has duplicate values')
    if len(set_a) != int(m_length) or len(set_b) != int(m_length):
        sys.exit('The length of at least one of your set does not match the declared length')
    if len(n_elements) != int(n_length):
        sys.exit('The length of your array does not match the declared length')

def happiness(n_elements,set_a,set_b):
    happiness = 0
    for number in n_elements:
        if number in set_a:
            happiness += 1
        elif number in set_b:
            happiness -=1
    return happiness




if __name__ == '__main__':
    main()
