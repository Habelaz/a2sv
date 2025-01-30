func isPalindrome(x int) bool {
    if x < 0{
        return false
    }
    num := x
    reverse := 0
    for x != 0 {
        reverse = 10 * reverse + x % 10
        x /= 10
    }

    // fmt.Println(reverse,x)
    return reverse == num
}