import math


class Solution:
    def kClosest(self, points, K: int):
        """
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                if math.sqrt(points[i][0]*points[i][0]+points[i][1]*points[i][1]) > math.sqrt(points[j][0]*points[j][0]+points[j][1]*points[j][1]):
                    points[j],points[i] = points[i],points[j]
        return points[:K]
        """
        return sorted(points, key=lambda coordinate: coordinate[0] * coordinate[0] + coordinate[1] * coordinate[1])[:K]
