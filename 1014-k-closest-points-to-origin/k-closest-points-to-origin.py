class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # mydict = {}
        # for x,y in points:
        #     summ = x*x + y*y
        #     mydict[summ] = [x,y]
        # ans = [mydict[key] for key in sorted(mydict.keys())]
        # if len(points) == k:
        #     return points
        points = sorted(points,key= lambda x : x[0]**2 + x[1]**2)
        return points[:k]
        
        