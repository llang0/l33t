// 876. Middle of the Linked List

// Given the head of a singly linked list, return the middle node of the linked list.

// If there are two middle nodes, return the second middle node.

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    var middle = head;
    var end = head;

    // for every two spaces you advance the 'end' node, advance the 'middle' node one space
    while(end !== null && end.next !== null){
        middle = middle.next;
        end = end.next.next; 
    }
    return middle;
};