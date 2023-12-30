# 내장 모듈 heapq는 기본적으로 최소 힙을 구현 함.
# heapq의 원소에 음수로 사용시 최대 힙처럼 활용 가능.

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def __len__(self):
        return len(self.heap)

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

    
    def _switch_down(self,parent_idx,child_idx):
        self.heap[parent_idx], self.heap[child_idx] = self.heap[child_idx], self.heap[parent_idx]
        return child_idx
    

    def _compare_down(self):
        parent_idx = 0
        while self._has_left_child(parent_idx):
            if self._has_right_child(parent_idx):
                if self.heap[parent_idx] < max(self.heap[parent_idx*2+1],self.heap[parent_idx*2+2]):
                    if self.heap[parent_idx*2+1] > self.heap[parent_idx*2+2]:
                        parent_idx = self._switch_down(parent_idx,parent_idx*2+1)
                    else:
                        parent_idx = self._switch_down(parent_idx,parent_idx*2+2)
            else:
                if self.heap[parent_idx] < self.heap[parent_idx*2+1]:
                    parent_idx = self._switch_down(parent_idx,parent_idx*2+1)

    
    def pop(self):
        if len(self.heap) > 1:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            item = self.heap.pop()
            self._compare_down()
        elif len(self.heap) == 1:
            item = self.heap.pop()
        else:
            item =None

        return item
        