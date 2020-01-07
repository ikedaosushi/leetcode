func isPalindrome(x int) bool {
    r := []rune(strconv.Itoa(x))
    fmt.Printf("%v", r)
    
    var last, first rune
    
    for {
        if len(r) <= 1 { break }
        last = r[len(r)-1] 
        r = r[:len(r)-1]

        first = r[0]
        r = r[1:]
        
        if first != last {
            return false
        }
    }
    
    return true
}