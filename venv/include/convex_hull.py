import time
q = [(2, 2), (3, 3), (5, 2), (4, 0), (3, 1),(-1, 0), (0, 1), (1, 0), (0, -2)] #points list
remove_list = []
points_left = []
points_right = []
point_left = []
point_right = []
leftp = []
rightp = []
clockwise = [(2,2),(3,3),(5,2),(4,0),(3,1)] #input clockwise sequence of right half
counterclockwise = [(1,0),(0,1),(-1,0),(0,-2)] #input anticlockwise sequence of left half

def slope(p1, p2, p3):
    #slope calculation function
    m = ((p2[1]-p1[1])*(p3[0]-p2[0])) - ((p2[0]-p1[0])*(p3[1]-p2[1]))
    return m

def Diff(list1, list2):
    #returns intersection of both list
    return (list(set(list1) - set(list2)))

def merge(points_left,points_right):

    left_point = max(points_left)
    right_point = min(points_right)
    c_left_point = left_point
    c_right_point = right_point

    #upper tangent
    while(True):
        lm = left_point
        rm = right_point
        z = len(clockwise)
        for i in range(1, z):
            n = clockwise[i]
            m = slope(left_point,right_point,n)
            if m<=0:
                remove = right_point
                remove_list.append(remove)
                right_point = n


        z = len(counterclockwise)
        for i in range(1, z):
            n = counterclockwise[i]
            m = slope(right_point,left_point,n)
            if m>=0:
                remove = left_point
                remove_list.append(remove)
                left_point = n
        if (left_point == lm and right_point ==  rm):
            break

    while (True):
        lm = c_left_point
        rm = c_right_point

        #lower tangent
        z = len(clockwise)

        for i in range(1, z):
            n = clockwise[z-i]
            m = slope(c_left_point,c_right_point,n)
            if m >= 0:
                remove = c_right_point
                remove_list.append(remove)
                c_right_point = n

        z = len(points_left)
        for i in range(1, z):
            n = points_left[z- i]
            m = slope(c_right_point,c_left_point,n)
            if m <= 0:
                remove = c_left_point
                remove_list.append(remove)
                c_left_point = n

        if (c_left_point == lm and c_right_point ==  rm):
            break

    final_tangent = [right_point,left_point,c_right_point,c_left_point]#upper and lower tangent points
    print (Diff(q,Diff(remove_list, final_tangent)))#removing points from the main list point list - Last array printed is the final result
    return (Diff(q,Diff(remove_list, final_tangent)))


def convexhull(q):

    n = len(q)
    if n<4:
        print (q)
        return q
    else:
        median = len(q)/2 #int return lower bound value
        q_left = q[0:median]#creating list for left and right points
        q_right = q[median:]
        leftp = convexhull(q_left)
        rightp = convexhull(q_right)

        return merge(q_left,q_right)

q.sort()
start_time = time.time() #execution time calculation starts from here
convexhull(q)
end_time = time.time()
print ((end_time-start_time))



