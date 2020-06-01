/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    result := &ListNode{}
    return_ := result
    
    for l1 != nil && l2 != nil {
        if l1.Val < l2.Val {
            result.Next = l1
            l1 = l1.Next
            result = result.Next
        } else {
            result.Next = l2
            l2 = l2.Next
            result = result.Next
        }
    }
    if l1 != nil {
        result.Next = l1
    } else if l2 != nil {
        result.Next = l2
    }
    
    return return_.Next
}