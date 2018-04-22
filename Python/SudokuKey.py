def check_sudoku(inL):
    n = len(inL)
    digit = 1
    while digit <= n:
        i = 0
        while i < n:
            rcount = 0
            ccount = 0
            j = 0
            while j < n:
                if inL[i][j] == digit:
                    rcount += 1
                if inL[j][i] == digit:
                    ccount += 1
                j += 1
            if rcount != 1 or ccount != 1:
                return False
            i += 1
        digit += 1
    return True