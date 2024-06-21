# This program calculates distances between 2 points in 2D space
points = [(1, 1), (4, 5), (-9, 24)]

def euclideanDistance(points):
  distances = []
  for i in range(0, len(points)):
    for j in range(i + 1, len(points)):
      # print("i = " , i , ", j = " , j)
      if(j >= len(points)):
        # print("happened")
        return distances
      dist = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
      dist = round(dist, 2)
      # print("dist between point " , i , " and " , j , " = " , dist)
      distances.append(dist)
  return distances

print(euclideanDistance(points)) 