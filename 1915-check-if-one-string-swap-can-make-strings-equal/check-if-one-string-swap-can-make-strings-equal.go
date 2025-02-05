func areAlmostEqual(s1 string, s2 string) bool {
    ind1 :=0
    ind2 := 0
    count := 0

    for i := 0; i < len(s1); i++ {
        if s1[i] != s2[i] {
            count += 1
            if ind1 == 0 {
                ind1 = i
            } else {
                ind2 = i
            }
        }
    }
    if (count != 0) && (count != 2) {
        return false
    }
    if (s1[ind1] == s2[ind2]) && (s1[ind2] == s2[ind1]){
        return true
    }
    return false
}