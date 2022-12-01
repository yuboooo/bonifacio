from itertools import permutations
from copy import deepcopy
from defer_acceptance import defer_acceptance
from reduction import reduction
from input_check import substitutability, lad


def bonifacio(fp, wp):
    # Return a set of stable matching
    u_sets = []
    # Check input requirement
    check_sub = substitutability(fp) and substitutability(wp)
    check_lad = lad(fp) and lad(wp)
    if check_sub and check_lad:
        # Get firm's and worker's optimal stable matching
        uf = defer_acceptance(fp, wp)
        uw = defer_acceptance(wp, fp)
        u_sets.append(uf)
        u_sets.append(uw)
        def cycle(uf, uw):
            if uf != uw:
                # Run reduction to reduce the size of preference list
                new_fp, new_wp = reduction(fp, wp)
                # Find cycle for new preference list
                c_sets = find_cycle(new_fp, new_wp) # c_sets --> set of cycle consist of c1, c2 ... cn
                # Get new set of stable matching from cycle we found (Substitute on uf)
                new_u_sets = run_cycle(cycles)
                u_sets.extend(new_u_sets)
                for new_u in new_u_sets:
                    cycle(new_u, uw)
            else:
                return None
        cycle(uf, uw)
    else:
        return None
    return u_sets