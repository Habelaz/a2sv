class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

      my_set = set()
      for s, e in ranges:
          for num in range(s, e + 1):
              my_set.add(num)
              
      for num in range(left, right + 1):
          if num not in my_set:
              return False

      return True 