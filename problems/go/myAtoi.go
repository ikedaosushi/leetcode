func myAtoi(str string) int {
    MIN := int(math.Pow(-2, 31))
    MAX := int(math.Pow(2, 31) - 1)
    reslStr := []string{}
    // fmt.Printf("%v, %v\n", MAX, MIN)
    validStrings := []string{" ", "-", "+"}
    symbolStrings := []string{"+", "-"}
    intStrings := []string{"+", "-"}
    removeString := " "
    // stopString := "."
    for i := 0; i < 10; i++ {
        intStrings = append(intStrings, strconv.Itoa(i))
    }
    // fmt.Printf("validStrings: %v\n", validStrings)
    hasSymbol := false
    
    for _, r := range(str) {
        s := string(r)
        if ! (contains(validStrings, s) || contains(intStrings, s)){
            break
        }

        if 0 < len(reslStr) && !contains(intStrings, s) {
            break
        }
        
        if contains(symbolStrings, s) {
            if hasSymbol {
                break
            }
            hasSymbol = true
        }
        if contains(intStrings, s) && s != removeString {
            reslStr = append(reslStr, s)
            if !hasSymbol {
                hasSymbol = true
            }
        }
        fmt.Printf("%v\n", s)
        fmt.Printf("%v\n", reslStr)
    }
    if len(reslStr) == 0 {
        return 0
    }
    
    resul, _ := strconv.Atoi(strings.Join(reslStr, ""))
    fmt.Printf("result: %v\n", strings.Join(reslStr, ""))
    if MAX < resul {
        resul = MAX
    }
    if resul < MIN {
        resul = MIN
    }
    
    return resul
}

func contains(s []string, e string) bool {
    for _, a := range s {
        if a == e {
            return true
        }
    }
    return false
}