def substitutability(prefs):
    check = True
    for proposed_side in prefs.values():
        flag = False
        if len(proposed_side[0]) <= 1:
            flag = True
        else:
            for p in proposed_side[0]:
                if p in proposed_side[1]:
                    flag = True
        check = check and flag
    return check 

def lad(prefs):
    for proposed_side in prefs.values():
        for i in range(len(proposed_side)-1):
            if len(proposed_side[i]) < len(proposed_side[i+1]):
                return False
    return True 
