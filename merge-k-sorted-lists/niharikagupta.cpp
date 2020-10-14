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
        priority_queue<pair<int,ListNode*>,vector<pair<int,ListNode*>>,greater<pair<int,ListNode*>>> p;
        for(int i=0;i<lists.size();i++)
            if(lists[i]!=NULL)
                p.push(make_pair(lists[i]->val,lists[i]));
        ListNode *head = new ListNode(0);//dummy
        ListNode *temp = head;
        
        while(!p.empty()){
            pair<int,ListNode*> min = p.top();
            p.pop();
            temp->next=min.second;
            temp=min.second;
            
            if(min.second->next != NULL)
                p.push(make_pair(min.second->next->val,min.second->next));
        }
        return head->next;
    }
        
};
