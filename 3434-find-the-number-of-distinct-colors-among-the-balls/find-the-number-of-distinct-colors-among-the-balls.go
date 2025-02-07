func queryResults(limit int, queries [][]int) []int {
    m := make(map[int]int)
    color := make(map[int]int)
    n := len(queries)
    ans := make([]int,n)


    for i := 0; i < n; i++ {
        key := queries[i][0]
        value := queries[i][1]

        if m[key] == 0 {
            m[key] = value
        }else{
            prevColor := m[key]
            if color[prevColor] == 1{
                delete(color,prevColor)
            } else{
                color[prevColor] -= 1
            }
            m[key] = value
        }
        color[value] += 1
        ans[i] = len(color)
    }
    return ans
}