func clearDigits(s string) string {
    stack := []rune{}
    for _,ch := range s {
        if unicode.IsDigit(ch)  {
            stack = stack[:len(stack)-1]
        } else {
            stack = append(stack,ch)
        }
    }
    // fmt.Println(stack)
    return string(stack)
}