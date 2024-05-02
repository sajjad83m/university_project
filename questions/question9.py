
def q9(ranges):

    """ranges = [[1, 10, 'A'], [10, 40, 'B'], [20, 30, 'C'], [30, 40, 'D'],
              [40, 50, 'E']]"""

    years = []
    max_year = 0
    min_year = ranges[0][0]

    i = 0
    ranges_new = ranges.copy()
    for range1_i in range(0, len(ranges)):
        range1 = ranges[range1_i]
        for range2_i in range(i, len(ranges)):
            range2 = ranges[range2_i]
            born1 = range1[0]
            death1 = range1[1]
            born2 = range2[0]
            death2 = range2[1]

            if born1 == death2:
                #death2 -=1
                ranges_new[range2_i][1] -= 1
            if death1 == born2:
                #death1 -=1
                ranges_new[range1_i][1] -= 1
        i += 1

    years = []
    for range_ in ranges_new:
        for year in range(range_[0], range_[1] + 1):
            years.append(year)
            if year < min_year:
                min_year = year
            elif year > max_year:
                max_year = year

    max_years_occur = [(-1, -1)]  #[(occur, year)]
    for year in range(min_year, max_year + 1):
        if max_years_occur[0][0] < years.count(year):
            max_years_occur = [(years.count(year), year)]
        elif max_years_occur[0][0] == years.count(year):
            max_years_occur.append((years.count(year), year))

    i = 0
    ranges_out = []
    while i < len(max_years_occur):
        max_range = max_years_occur[i][1]
        min_range = max_years_occur[i][1]
        occur_num = max_years_occur[i][0]
        while i + 1 < len(max_years_occur) and max_years_occur[i][1] + 1 == max_years_occur[i + 1][1]:
            max_range = max_years_occur[i + 1][1]
            occur_num = max_years_occur[i + 1][0]
            i += 1
        ranges_out.append([(min_range, max_range), occur_num])
        i += 1

    for range_person in ranges_new:
        for range_out in ranges_out:
            if range_out[0][1] >= range_person[0] and range_out[0][1] <= range_person[1]:
                range_out.append(range_person[2])
                
    return ranges_out
