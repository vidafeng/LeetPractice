/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    // create a new node
    // set current to tempNode
    // while list1 and list2 are not null
    // compare the values and add smaller value node to current
    // move the corresponding pointer to the next node
    // return merged list starting from tempNode.next so the 0 is not incl

    let tempNode = new ListNode(null);
    let current = tempNode;

    while (list1 && list2) {
        console.log(tempNode)
        if (list1.val <= list2.val) {
            current.next = list1;
            list1 = list1.next
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }
    current.next = list1 || list2;

    return tempNode.next; 
    
};