class Solution:
    def numberOfWays(self, s: str) -> int:
        cnt_z = s.count('0')
        cnt_o = len(s) - cnt_z
        pref_z = 0
        pref_o = 0
        ans = 0

        for c in s:
            if c == '0':
                ans += pref_o * (cnt_o - pref_o)
                pref_z += 1
            else:
                ans += pref_z * ( cnt_z - pref_z)
                pref_o += 1
        return ans