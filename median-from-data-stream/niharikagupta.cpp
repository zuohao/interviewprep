class MedianFinder {
public:
    /** initialize your data structure here. */
    priority_queue<int, vector<int>, greater<int>> minHeap;
    priority_queue<int> maxHeap;
    
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if(maxHeap.empty() || num<maxHeap.top())
            maxHeap.push(num);
        else
            minHeap.push(num);
        if(maxHeap.size()>minHeap.size()+1){
            int temp = maxHeap.top();
            maxHeap.pop();
            minHeap.push(temp);
        }
        else if(minHeap.size()>maxHeap.size()+1){
            int temp = minHeap.top();
            minHeap.pop();
            maxHeap.push(temp);
        }
    }
    
    double findMedian() {
        if(minHeap.size()==maxHeap.size()){
            return (1.0*(minHeap.top()+maxHeap.top())/2);
        }
        else if(minHeap.size()>maxHeap.size()){
            return minHeap.top();
        }
        else{
            return maxHeap.top();
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
