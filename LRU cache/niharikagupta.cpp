class LRUCache {
public:
    map<int,list<pair<int,int>> :: iterator> m;
    list<pair<int,int>> l;
    int size;
    int total;
    
    LRUCache(int capacity) {
        size=0;
        total=capacity;
    }
    
    int get(int key) {
        int v;
        if(m.count(key)>0){
            v = (*m[key]).second;
            l.erase(m[key]);
            l.push_front(make_pair(key,v));
            m[key] = l.begin();
            return v;
        }
        else{
            return -1;
        }
    }
    
    void put(int key, int value) {
        if(m.count(key)>0){
            l.erase(m[key]);
        }
        else if(size<total){
            size++;
        }
        else{
            m.erase(l.back().first);
            l.pop_back();
        }
        l.push_front(make_pair(key,value));
            m[key]=l.begin();
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
