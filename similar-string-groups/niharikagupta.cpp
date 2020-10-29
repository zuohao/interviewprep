class Solution {
public:
    int numSimilarGroups(vector<string>& A) {
        int n = A.size();
        vector<vector<int>> graph(n);
        
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(similar(A[i],A[j])){
                    graph[i].push_back(j);
                    graph[j].push_back(i);
                }
            }
        }
        int res=0;
        vector<bool> visited(n,false);
        for(int i=0;i<n;i++){
            if(!visited[i]){
                dfs(graph, visited, i);
                res++;
            }
        }   
        return res;
    }
    
    bool similar(string word1, string word2){
        int diff=0;
        for(int i=0;i<word1.size();i++){
            if(word1[i]!=word2[i]){
                diff++;
            }
        }
        return diff <= 2;
    }
    
    void dfs(vector<vector<int>> &graph, vector<bool> &visited, int index){
        visited[index]=true;
        for(int i=0;i<graph[index].size();i++){
            if(!visited[graph[index][i]])
                dfs(graph, visited, graph[index][i]);
        }
    }
};
