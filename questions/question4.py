
def q4(results):

    """results = {'teama': {'teamb':  1, 'teamc': -1, 'teamd':  1},
              'teamb': {'teama': -1 ,'teamc':  1, 'teamd': -1},
              'teamc': {'teama':  1, 'teamb': -2, 'teamd':  0},
              'teamd': {'teama':  -1, 'teamb':  1, 'teamc':  0}}"""

    list_ret = []
    def permutations(before, array):
        #print(before_str)
        if len(array) == 1:
            before.append(array[0])
            list_ret.append(before)
            before = []
        for i in array:
            array_2 = list.copy(array)
            array_2.remove(i)
            permutations(before.__add__([i]) ,array_2)
        return list_ret
    
    list_per = permutations([] ,list(results.keys()))
    out_list = []
    for per in list_per:
        #print(per)
        for i in range(0, len(per)-1):
            team1 = per[i]
            team2 = per[i+1]
            if results[team1][team2] ==-1:
                break
        else:
            out_list.append(per)
    return out_list
