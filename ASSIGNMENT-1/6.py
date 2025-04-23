def distance(lst1,lst2):
    distance = 0.0
    for i in range(3):
        distance += abs(lst1[i]-lst2[i]) ** 2
    final = distance ** 0.5
    return final

points = []
print("Enter (x,y,z) coordinates in each line separated with comma: ")
for i in range(4):
    point = input()
    lst = list(map(int,point.split(",")))
    points.append(lst)

lst = []
for i in range(len(points)):
    min_dist = float("inf")
    point = []
    for j in range(len(points)):
        if i != j:
            dist = distance(points[i],points[j])
            if dist < min_dist:
                min_dist = dist
                point = points[j]
    lst.append([points[i],point])
    
for x in lst:
    print(f"{x[0]} -> {x[1]}")