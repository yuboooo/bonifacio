from itertools import permutations

# find the free male
def male_without_match(male_matches, males):
    for male in males:
        if male not in male_matches:
            return male
    return None

# for a specific male, find the female that the male has not proposed yet
def female_not_proposed(male, male_proposed, male_pref):
    for female in male_pref: # for all female in male_pref list
        if male_proposed is [] or female not in male_proposed[male]: # if female not proposed by male before
            return female # return that female
    return "None" # if all female are proposed by the male before, it means no match

# find a female that no male is proposed to yet
def female_free(female_list, engaged):
    for female in female_list:
        if female in engaged:
            return False
    return True

def female_favorback(male, female_list, females_prefs, female_engaged):
    love = True # initialize love to true
    for female in female_list: # for each female in male's highest rank female list
        if female not in female_engaged:
            female_engaged.extend([female])
        female_pref = females_prefs[female] # get that female's preference list on male
        if [male] not in female_pref: # if any female doesn't prefer the proposing male
            love = False # set love to false
    return love

# if female is engaged with m', check whether she prefer m over m' or not
def female_prefered(male, female, female_pref, female_matches):
    prefered = False
    prefered_matches = []

    if female in female_matches:
        current_matches = female_matches[female]
        # if m better than m'
        if current_matches != []:
            if [male] in female_pref and female_pref.index([male]) < female_pref.index(current_matches):
                prefered = True
                prefered_matches = [male] 
            potential_matches = []
            potential_matches.extend(current_matches)
            potential_matches.extend([male])
            '''potential_matches = [1, 3] --> perm_matches = [[1, 3], [3, 1]]'''
            perm_matches = list(map(list,list(permutations(potential_matches))))
            for match in perm_matches:
                if match in female_pref and female_pref.index(match) < female_pref.index(current_matches):
                    if prefered == False or female_pref.index(match) < female_pref.index(prefered_matches):

                        prefered = True
                        prefered_matches = match
            return (prefered, prefered_matches, current_matches)
        else:
            return (False, [], [])
    else:
        return (True, [male], [])
        
def defer_acceptance(males_prefs, females_prefs):
    male_matches = {}
    female_matches = {}
    male_proposed = {}
    female_engaged = []
    female_prefered_list = {}
    males = list(males_prefs.keys())
    while True:
        male = male_without_match(male_matches, males) # find the free male
        if male is None: # if all matched, terminate
            break

        if male not in male_proposed:
            male_proposed[male] = [] # male proposed list
        male_pref = males_prefs[male] # get current male's preference list

        def propose(): # recursive helper function to let male propose to next prefered female
            highest_rank_female = female_not_proposed(male, male_proposed, male_pref) # current highest ranked female that male not proposed yet

            if highest_rank_female == "None":
                male_matches[male] = "None"
                return

            if male_proposed[male] == []: # if not in proposed list, add into it
                male_proposed[male].append(highest_rank_female)
            else: # if in proposed list, continue append list
                if highest_rank_female not in male_proposed[male]:
                    male_proposed[male].append(highest_rank_female)

            if female_free(highest_rank_female, female_engaged): # if that female is free
                love = female_favorback(male, highest_rank_female, females_prefs, female_engaged) # check whether female also favor the proposing male
                if love == True: # if yes, then they engaged
                    male_matches[male] = highest_rank_female # engaged
                    for female in highest_rank_female:
                        female_matches[female] = [male]
                else: # male remains free, and propose to next prefered female
                    propose()

            else: # if the female is already engaged with other m'
                love = female_favorback(male, highest_rank_female, females_prefs, female_engaged) # check whether female also favor the proposing male
                for female in highest_rank_female:
                    female_pref = females_prefs[female]
                    if love == True:
                        female_prefered_list[female] = female_prefered(male, female, female_pref, female_matches)

                prefered = True
                for key, values in female_prefered_list.items():
                    if key in highest_rank_female and values[0] == False:
                        prefered = False

                if love == True: 
                    if prefered == True: # m > m'
                        for female, values in female_prefered_list.items(): # values = (prefered, prefered_matches, current_matches)
                            male_matches[male] = highest_rank_female
                            if values[0] == True:
                                female_matches[female] = values[1] # female match with m
                    else:
                        propose()

        propose()
        male_matches = dict(sorted(male_matches.items()))
        female_matches = dict(sorted(female_matches.items()))
    return [male_matches, female_matches]
