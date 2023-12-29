class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def _compare_up(self,parent_idx,child_idx):
        if parent_idx <0 or self.heap[parent_idx] >= self.heap[child_idx]:
            return False
        else:
            return True
        
    def _switch_up(self,parent_idx,child_idx):
        self.heap[parent_idx], self.heap[child_idx] = self.heap[child_idx], self.heap[parent_idx]
        return parent_idx-1 // 2, parent_idx

    def insert(self, val):
        self.heap.append(val)
        child_idx = len(self.heap)-1
        parent_idx = (child_idx-1) // 2
        while self._compare_up(parent_idx,child_idx):
            parent_idx, child_idx = self._switch_up(parent_idx,child_idx)
    
    def _has_left_child(self, parent_idx):
        left_child = parent_idx*2+1
        if len(self.heap) >= left_child+1: return True
        else: return False 
    
    def _has_right_child(self, parent_idx):
        right_child = parent_idx*2+2
        if len(self.heap) >= right_child+1: return True
        else: return False 

    def _has_child(self, parent_idx):
        return self._has_left_child(parent_idx) or self._has_right_child(parent_idx)
    
    def _switch_down(self,parent_idx,child_idx):
        self.heap[parent_idx], self.heap[child_idx] = self.heap[child_idx], self.heap[parent_idx]
        return child_idx
    

    def _compare_down(self):
        parent_idx = 0
        while self._has_child(parent_idx):
            left_child = self.heap[parent_idx*2+1] if self._has_left_child(parent_idx) else None
            right_child = self.heap[parent_idx*2+2] if self._has_left_child(parent_idx) else None
            if left_child > right_child and left_child > self.heap[parent_idx]:
                parent_idx = self._switch_down(parent_idx,parent_idx*2+1)
            elif left_child < right_child and right_child > self.heap[parent_idx]:
                parent_idx = self._switch_down(parent_idx,parent_idx*2+2)

    
    def pop(self,val):
        if len(self.heap) > 1:
            self._switch(0,len(self.heap))
            item = self.pop()
            self._compare_down()
        elif len(self.heap) == 1:
            item = self.pop()
        else:
            item =None

        return item
        
