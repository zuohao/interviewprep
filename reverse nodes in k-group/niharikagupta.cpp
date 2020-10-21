/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    
    ListNode* reverseLinkedList(ListNode* cur, int k) {
        ListNode* prev=NULL;ListNode* nxt=NULL;
        while(cur!= NULL && k>0){
            nxt=cur->next;
            cur->next=prev;
            prev=cur;
            cur=nxt;
            k--;
        }
        return prev;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        
        if(head == NULL)
            return NULL;
        int count=0;
        ListNode* cur = head;
        while(count<k && cur!=NULL){
            cur=cur->next;
            count++;
        }
        if(count==k){
            ListNode* reversedHead = reverseLinkedList(head,k);
            head->next=reverseKGroup(cur,k);
            return reversedHead;
        }
        return head;
    }
};
