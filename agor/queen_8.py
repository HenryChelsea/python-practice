# coding: utf-8

# def queens (row, col):  
#     return [[]] if col == 0 \
#     else [[ran] + rst \
#     for ran in range(row) \
#     for rst in queens(row, col - 1) \
#     if safe(ran, rst)] 


def safe (ran, rst):  
    def check (pos):  
        return not (ran == rst[pos] or abs(ran - rst[pos]) == pos + 1)  
    return ands([check(pos) for pos in range(len(rst))])

def ands (ls):  
    return True if ls == []\
    else (False if not ls[0]\
    else ands(ls[1:]))

def queens(row, col):
    res = []
    if col != 0:
        for ran in range(row):
            for rst in queens(row, col - 1):
                print ">>> ", ran, ">>> ", rst
                if safe(ran, rst):
                    res.append([ran] + rst)
        return res
    else:
        return [[]]

if __name__ == '__main__':
    # print queens(4, 3)
    print queens(4, 4)