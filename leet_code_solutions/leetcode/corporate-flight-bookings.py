class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pref = [0] * (n+1)
        for i in range(len(bookings)):
            start = bookings[i][0]
            end = bookings[i][1]
            seats = bookings[i][-1]

            pref[start - 1] += seats
            pref[end] -= seats
        
        acc = 0 
        for i in range(len(pref)):
            acc += pref[i]
            pref[i] = acc
        
        return pref[:-1]
        