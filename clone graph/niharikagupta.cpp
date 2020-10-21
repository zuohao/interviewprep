/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    unordered_map<Node*, Node*> mapping;
    Node* cloneGraph(Node* node) {
      if(node==NULL)
          return NULL;
      Node* newNode = new Node(node->val);
      mapping.insert(make_pair(node, newNode));
      
      for(int i=0;i<node->neighbors.size();i++){
        if(mapping.count(node->neighbors[i])==0){
          newNode->neighbors.push_back(cloneGraph(node->neighbors[i]));
        }
        else{
          newNode->neighbors.push_back(mapping[node->neighbors[i]]);
        }
      }
      return newNode;
    }
};
