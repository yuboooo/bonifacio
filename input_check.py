def substitutability(prefs):
    check = True
    for workers in prefs.values():
        flag = False
        if len(workers[0]) <= 1:
            flag = True
        else:
            for w in workers[0]:
                if w in workers[1]:
                    flag = True
        check = check and flag
    return check 

def lad(fp, wp):
    pass