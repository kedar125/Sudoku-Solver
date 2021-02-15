import copy

dup = []

def out(grid):
    r= rcheck(grid)
    if r==1:
        return -1
    r=ccheck(grid)
    if r==1:
        return -1
    r=bcheck(grid)
    if r==1:
        return -1

    return 0


def finderror(): #CHECKS DUPLICITY IN THE LIST : dup
    global dup

    for i in dup:
        if i==0:
            pass
        else:
            if dup.count(i)>1:
                return 1

    return 0

#ROW CHECK
def rcheck(grid):
    global dup
    dup.clear()
    for l in range(0, 9):
        k = grid[l]
        dup = copy.deepcopy(k)
        j = finderror()
        if (j == 0):
            pass
        else:
            return 1
    dup.clear()
    return 0


#COLUMN CHECK
def ccheck(grid):
    global dup
    dup.clear()
    for l in range(0, 9):
        for i in grid:
            dup.append(i[l])
        j = finderror()
        if (j == 0):
            pass
        else:
            return 1
        dup.clear()
    dup.clear()
    return 0



def bcheck(grid):
    # BLOCK 1 2 3 CHECK
    global dup
    dup.clear()
    p = [0, 3, 6]
    for m in p:
        for l in range(m, m + 3):
            c = 0
            for i in grid:
                dup.append(i[l])
                c += 1
                if (c > 2):
                    break
        j = finderror()
        if j == 0:
            pass
        else:
            return 1

        dup.clear()

    # BLOCK 4 5 6 CHECK
    dup.clear()
    p = [0, 3, 6]
    for m in p:
        for l in range(m, m + 3):
            c = 0
            for i in grid:
                if c == 0 or c == 1 or c == 2:
                    pass
                else:
                    dup.append(i[l])
                    if c > 4:
                        break
                c += 1
        j = finderror()
        if j == 0:
            pass

        else:
            return 1

        dup.clear()

    # BLOCK 7 8 9 CHECK
    dup.clear()
    p = [0, 3, 6]
    for m in p:
        for l in range(m, m + 3):
            c = 0
            for i in grid:
                if (c == 0) or (c == 1) or (c == 2) or (c == 3) or (c == 4) or (c == 5):
                    pass
                else:
                    dup.append(i[l])
                    if c > 8:
                        break
                c += 1

        j = finderror()
        if j == 0:
            pass
        else:
            return 1

        dup.clear()

    return 0







