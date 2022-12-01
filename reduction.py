# imports
from defer_acceptance import defer_acceptance
from copy import deepcopy


# Return subsets assigned in the optimal stable matchings
def get_u(u1, u2):
    u_temp = [u1, u2]
    u = {}
    for k in u2.keys():
        u[k] = tuple(u[k] for u in u_temp)
    return u

# return dictionary where value is a set(list)
def get_u_sets(u):
    u_sets = {}
    for k in u.keys():
        lst = list(u[k])
        u_sets[k] = list(set(lst[0] + lst[1]))
    return u_sets

# sets --> 2-d array(value of preference dictionary); set1/set2 --> 1-d array
def blair_preferred(sets, set1, set2):
    if sets.index(set1) < sets.index(set2):
        return True
    return False

# u_sets --> array(value of u_sets); sets --> array
def set_in_u(u_set, sets):
    for s in sets:
        if s not in u_set:
            return True
    return False

# Reduction Step 1 and Step 2:
def reduction_step1_step2(firms_prefs, workers_prefs, one_to_one):

    uf1, uw1 = defer_acceptance(males_prefs=deepcopy(firms_prefs), females_prefs=deepcopy(workers_prefs), one_to_one=one_to_one) # DA - firms proposing
    uw2, uf2 = defer_acceptance(males_prefs=deepcopy(workers_prefs), females_prefs=deepcopy(firms_prefs), one_to_one=one_to_one) # DA - workers proposing
    uf = get_u(uf1, uf2)
    uw = get_u(uw2, uw1)
    uf_sets = get_u_sets(uf)
    uw_sets = get_u_sets(uw)

    # Step 1 and Step 2 of reduction for one side
    # Output: preference list after reduction
    def reduction_for_oneside(preference_lists, u_sets, u1, u2):
        delete = {}
        for keys, values in preference_lists.items():
            for value in values:
                for v in value:
                    if keys in u_sets:
                        # Step 1:
                        if v not in u_sets[keys] and blair_preferred(preference_lists[keys], value, u1[keys]):
                            if keys not in delete:
                                delete[keys] = [v]
                            else:
                                if v not in delete[keys]:
                                    delete[keys].append(v)

                        # Step 2:
                        elif v not in u_sets[keys] and blair_preferred(preference_lists[keys], u2[keys], value):
                            if keys not in delete:
                                delete[keys] = [v]
                            else:
                                if v not in delete[keys]:
                                    delete[keys].append(v)

        return delete
    # Reduction on firms' side:
    delete_workers = reduction_for_oneside(firms_prefs, uf_sets, uf1, uf2)
    # Reduction on workers' side:
    delete_firms = reduction_for_oneside(workers_prefs, uw_sets, uw2, uw1)

    def delete_sets(preference_lists, delete):
        new_preference_lists = deepcopy(preference_lists)
        for keys, values in preference_lists.items():
            
            for value in values:
                if keys in delete:
                    for v in delete[keys]:
                        if v in value and value in new_preference_lists[keys]:
                            new_preference_lists[keys].remove(value)
        return new_preference_lists
    
    new_firms = delete_sets(firms_prefs, delete_workers)
    new_workers = delete_sets(workers_prefs, delete_firms)

    return [new_firms, new_workers]

# Reduction Step 3
def mutually_acceptable(firms_prefs, workers_prefs):
    flatten_firms = {}
    flatten_workers = {}
    firms = []
    workers = []
    for keys, values in firms_prefs.items():
        firms.append(keys)
        flatten_firms[keys] = list(set(sum(values, [])))
    for keys, values in workers_prefs.items():
        workers.append(keys)
        flatten_workers[keys] = list(set(sum(values, [])))

    for keys, values in flatten_firms.items():
        diff = list(set(workers).difference(values))
        for d in diff:
            for firm in deepcopy(workers_prefs)[d]:
                if keys in firm:
                    workers_prefs[d].remove(firm)
    for keys, values in flatten_workers.items():
        diff = list(set(firms).difference(values))
        for d in diff:
            for worker in deepcopy(firms_prefs)[d]:
                if keys in worker:
                    firms_prefs[d].remove(worker)
                    
    return [firms_prefs, workers_prefs]

def reduction(firms_prefs, workers_prefs, one_to_one=False):
    # Perform reduction step 1 and step 2
    new_firms, new_workers = reduction_step1_step2(firms_prefs, workers_prefs, one_to_one)
    new_firms, new_workers = mutually_acceptable(new_firms, new_workers)
    return [new_firms, new_workers]


