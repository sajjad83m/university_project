from questions.question10 import q10

def q6(city_x, city_y, store1_x, store1_y, store2_x, store2_y, store3_x, store3_y):

    def find_Bisection_coeff(store1_x, store1_y, store2_x, store2_y):  # this fuction will find the known and unknown's coefficients of bisection equation for put them to matrix with using q10 fuction
        
        x_mid = (store1_x + store2_x) / 2
        y_mid = (store1_y + store2_y) / 2                           #   b(y - y_mid) = a(x - x_mid) ->
        if (store2_y - store1_y) == 0:                              #   b*y - a*x = b*y_mid - a*x_mid     -> c = b*y_mid - a*x_mid
            b = 0                                                   #   a/b = slope, so if the slope will be infinite the b will be zero
            a = 1                                                   #   'a' can be any number
            c = -(a*x_mid)
            return a, b, c                                          #   'a' is the coefficient of 'x' variable and 'b' is the coefficient of 'y' variable
        else:
            slope = -(store2_x - store1_x) / (store2_y - store1_y)  #   i put unknown values on the left and known values on the right side for put them to matrix with using q10 function
            a = -slope                                              #   and find the cross point of bisiction and another line
            b = 1                                                   #   a, b are coefficients of unknown values and c is coefficient of known value
            c = b*y_mid - a*x_mid                                   #   I do that becuase of the division of x_mid/y_mid that will be infinite when y_mid will be zero and i can't handle that, but now this problem is handled
            return a, b, c

    def Bisections_cross_point(store1_x, store1_y, store2_x, store2_y,
                         store3_x, store3_y):

        a1, b1, c1 = find_Bisection_coeff(store1_x, store1_y, store2_x, store2_y)
        a2, b2, c2 = find_Bisection_coeff(store3_x, store3_y, store1_x, store1_y)
        cross_point = q10([[a1, b1], [a2, b2]], [c1, c2])
        if cross_point != None and cross_point[0] <= city_x and cross_point[0] >= 0 and cross_point[1] <= city_y and cross_point[1] >= 0:
            return cross_point
        return None


    def cross_BisectionAndCity_(x_city, y_city, store1_x, store1_y, store2_x, store2_y):

        a1, b1, c1 = find_Bisection_coeff(store1_x, store1_y, store2_x, store2_y)
        a2, b2, c2 = 0, 1, y_city
        point_top = q10([[a1, b1], [a2, b2]], [c1, c2])

        a1, b1, c1 = find_Bisection_coeff(store1_x, store1_y, store2_x, store2_y)
        a2, b2, c2 = 0, 1, 0
        point_bottom = q10([[a1, b1], [a2, b2]], [c1, c2])

        a1, b1, c1 = find_Bisection_coeff(store1_x, store1_y, store2_x, store2_y)
        a2, b2, c2 = 1, 0, 0
        point_left = q10([[a1, b1], [a2, b2]], [c1, c2])

        a1, b1, c1 = find_Bisection_coeff(store1_x, store1_y, store2_x, store2_y)
        a2, b2, c2 = 1, 0, x_city
        point_right = q10([[a1, b1], [a2, b2]], [c1, c2])

        points_ret = []
        for cross_point in (point_top, point_bottom, point_right, point_left):
            if cross_point != None and cross_point[0] <= city_x and cross_point[0] >= 0 and cross_point[1] <= city_y and cross_point[1] >= 0:
                points_ret.append(cross_point)
        return points_ret


    def closest_stores(x_point, y_point, store1_x, store1_y, store2_x, store2_y, store3_x, store3_y):

        dis1 = (store1_x - x_point)**2 + (store1_y - y_point)**2
        dis2 = (store2_x - x_point)**2 + (store2_y - y_point)**2
        dis3 = (store3_x - x_point)**2 + (store3_y - y_point)**2
        point = (x_point, y_point)
        store1 = (store1_x, store1_y)
        store2 = (store2_x, store2_y)
        store3 = (store3_x, store3_y)
        
        dis_store1 = (store1, dis1)
        dis_store2 = (store2, dis2)
        dis_store3 = (store3, dis3)
        
        closest_stores = []
        dis_min = dis_store1[1]
        for dis_store in (dis_store1, dis_store2, dis_store3):
            if dis_store[1] < dis_min:
                dis_min = dis_store[1]
                closest_stores.clear()
                closest_stores.append(dis_store[0])
            elif dis_store[1] == dis_min:
                closest_stores.append(dis_store[0])
            
        return closest_stores, point


    cross12city = cross_BisectionAndCity_(city_x, city_y, store1_x, store1_y, store2_x, store2_y)
    cross13city = cross_BisectionAndCity_(city_x, city_y, store1_x, store1_y, store3_x, store3_y)
    cross23city = cross_BisectionAndCity_(city_x, city_y, store2_x, store2_y, store3_x, store3_y)
    crossBisections = Bisections_cross_point(store1_x, store1_y, store2_x, store2_y, store3_x, store3_y)
    crossBisections = Bisections_cross_point(store1_x, store1_y, store2_x, store2_y, store3_x, store3_y)

    cross_points = []
    for lst in (cross12city, cross13city, cross23city):
        cross_points.extend(lst)

    close_stories = []

    for point in cross_points:
        close_stories.append(closest_stores(point[0], point[1], store1_x, store1_y, store2_x, store2_y, store3_x, store3_y))

    if crossBisections != None:
        close_stories.append(closest_stores(crossBisections[0], crossBisections[1], store1_x, store1_y, store2_x, store2_y, store3_x, store3_y))

    closeVertex1 = closest_stores(0.0, 0.0, store1_x, store1_y, store2_x, store2_y, store3_x, store3_y)
    closeVertex2 = closest_stores(0.0, city_y, store1_x, store1_y, store2_x, store2_y, store3_x, store3_y)
    closeVertex3 = closest_stores(city_x, 0.0, store1_x, store1_y, store2_x, store2_y, store3_x, store3_y)
    closeVertex4 = closest_stores(city_x, city_y, store1_x, store1_y, store2_x, store2_y, store3_x, store3_y)

    for i in (closeVertex1, closeVertex2, closeVertex3, closeVertex4):
        close_stories.append(i)

    store1_points = []
    store2_points = []
    store3_points = []
    for closeStore in close_stories:
        if closeStore[0].__contains__((store1_x, store1_y)) and not store1_points.__contains__(closeStore[1]):
            store1_points.append(closeStore[1])
        if closeStore[0].__contains__((store2_x, store2_y)) and not store2_points.__contains__(closeStore[1]):
            store2_points.append(closeStore[1])
        if closeStore[0].__contains__((store3_x, store3_y)) and not store3_points.__contains__(closeStore[1]):
            store3_points.append(closeStore[1])

    return store1_points, store2_points, store3_points

#print(q6(100, 100, 25, 25, 25, 50, 25, 75))



#def q3(city_x, city_y):
#
#    x1 = 48
#    x2 = 49
#    x3 = 150
#    y1 = 150
#    y2 = 50
#    y3 = 50
#    store_area1 = set()
#    store_area2 = set()
#    store_area3 = set()
#    city_boundries = set()
#    city_polygons = ()  #((city_x, city_y), (city_x, 0),(0, city_y), (0,0))
#    for x in range(0, city_x + 1):
#        city_boundries.add((x, 0))
#        city_boundries.add((x, city_y))
#
#    for y in range(0, city_y + 1):
#        city_boundries.add((0, y))
#        city_boundries.add((city_x, y))
#
#    for x in range(0, city_x + 1):
#        #take abstract for distance of between points
#        d_x1, d_x2, d_x3 = 0, 0, 0
#        #for x_n in {x1: d_x1, x2: d_x2, x3: d_x3}:
#        #if x - x_n < 0:
#        #    x, x_n = x_n, x
#        d_x1 = x - x1
#        d_x2 = x - x2
#        d_x3 = x - x3
#
#        for y in range(0, city_y + 1):
#
#            d_y1, d_y2, d_y3 = 0, 0, 0
#            #take abstract for distance between points
#            #for y_n in {y1: d_y1, y2: d_y2, y3: d_y3}:
#            #if y - y_n < 0:
#            #    y, y_n = y_n, y
#            d_y1 = y - y1
#            d_y2 = y - y2
#            d_y3 = y - y3
#
#            distancePow_1 = d_y1**2 + d_x1**2  #note that the distance is distance to pow two
#            distancePow_2 = d_y2**2 + d_x2**2
#            distancePow_3 = d_y3**2 + d_x3**2
#
#            if distancePow_1 <= distancePow_2 and distancePow_1 <= distancePow_3:
#                store_area1.add((x, y))
#            if distancePow_2 <= distancePow_1 and distancePow_2 <= distancePow_3:
#                store_area2.add((x, y))
#            if distancePow_3 <= distancePow_1 and distancePow_3 <= distancePow_2:
#                store_area3.add((x, y))
#            print(distancePow_1, '--', distancePow_2, '--', distancePow_3)
#
#    store_boundry12 = store_area1.intersection(store_area2)
#    store_boundry23 = store_area2.intersection(store_area3)
#    store_boundry13 = store_area1.intersection(store_area3)
#    #print(store_boundry12,' ',store_boundry13,' ',store_boundry23)
#    #lines = (store_boundry12, store_boundry23, store_boundry13, city_boundries)
#    store1_points = set()
#    store2_points = set()
#    store3_points = set()
#    #stories_points = (store1_points, store2_points, store3_points)
#    areas = ((store_area1, store1_points), (store_area2, store2_points),
#             (store_area3, store3_points), (city_boundries, set()))
#    #print(sorted(store_boundry13))
#    store_area1
#    print(len(store_area1), ' ', len(store_area2), ' ', len(store_area3))
#    #print(len(store_boundry12),len(store_boundry13),len(store_boundry23))
#    #print(sorted(city_boundries))
#
#    for i in range(0, len(areas)):
#        for j in range(i + 1, len(areas)):
#            for k in range(j + 1, len(areas)):
#                print(i, ' ', j, ' ', k)
#                #print(areas[i],'NEXT1', areas[j], 'NEXT2', areas[k], 'NEXT3')
#                #print(type(areas[i][0]))
#                areas[i][1].update(areas[i][0].intersection(
#                    areas[j][0], areas[k][0]))
#                areas[j][1].update(areas[i][0].intersection(
#                    areas[j][0], areas[k][0]))
#                areas[k][1].update(areas[i][0].intersection(
#                    areas[j][0], areas[k][0]))
#
#    for city_polygon in city_polygons:
#        for area in areas:
#            if area[0].__contains__(city_polygon):
#                area[1].add(city_polygon)
#    print(store1_points, ' ', store2_points, ' ', store3_points)
