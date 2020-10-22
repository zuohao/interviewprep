class Solution {
public:
    vector<int> findOrder(int n, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(n);
        vector<bool> visited(n,false);
        vector<bool> onPath(n,false);
        
        vector<int> res;
        for(int i=0;i<prerequisites.size();i++){
            graph[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }
        for(int i=0;i<n;i++){
            if(!visited[i] && dfs_cycle(graph,visited,onPath,i,res)){
               return {}; 
            }
        }
        reverse(res.begin(),res.end());
        return res;
    }
    bool dfs_cycle(vector<vector<int>> &graph, vector<bool> &visited, vector<bool> &onPath, int node, vector<int> &res){
        visited[node]=true;
        onPath[node]=true;
        
        for(int i=0;i<graph[node].size();i++){
            if(onPath[graph[node][i]])
                return true;
            if(!visited[graph[node][i]] && dfs_cycle(graph,visited,onPath,graph[node][i], res)){
                return true;
            }
        }
        onPath[node]=false;
        res.push_back(node);
        return false;
    }
};
