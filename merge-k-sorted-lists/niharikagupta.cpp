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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int k = lists.size();
        priority_queue<pair<int,ListNode*>,vector<pair<int,ListNode*>>,greater<pair<int,ListNode*>>> p;
        
        for(int i=0;i<k;i++){
            if(lists[i]!=NULL){
                p.push(make_pair(lists[i]->val,lists[i]));
            }
        }
        
        ListNode *temp=NULL;
        ListNode *head=NULL;
        
        while(!p.empty()){
            pair<int,ListNode*> min = p.top();
            p.pop();
            
            if(head==NULL){
                temp = min.second;
                head = min.second;
            }
            else{
                temp->next=min.second;
                temp=min.second;
            }
            
            if(min.second->next != NULL){
                p.push(make_pair(min.second->next->val,min.second->next));
            }
        }
        return head;
    }
        
};
