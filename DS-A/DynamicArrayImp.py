import ctypes
import sys

class DynamicArray(object):
    
    def __init__(self):
        
        self.n = 0 #Actual count of the actual elements
        self.capacity = 1 #Default capacity
        self.A = self.make_array(self.capacity) #To call make.array
        
    def __len__(self):
        
        return self.n 
    
    def __getitem__(self,k): #Return the elements at index k
        
        if not 0 <= k < self.n: #If index(k) is NOT between 0 and the actual count of elements
            return IndexError('K is out of bounds!') #Return IndexError
        
        return self.A[k] #Return index k
    
    def append(self,ele): #To add ele to the end of the array
        
        if self.n == self.capacity: #If the capacity is full
            self._resize(2*self.capacity) # 2x if capacity isn't enough
            
        self.A[self.n] = ele
        self.n += 1
        
    def _resize(self,new_cap): #To increase the capacity
        
        B = self.make_array(new_cap) #The new array with bigger capacity
        
        for k in range(self.n): #All the existant values
            B[k] = self.A[k] #Referncin all the existing values from A to the B.
            
        self.A = B #Assigning our array to the new bigger one
        self.capacity = new_cap #Updating capacity
        
    def make_array(self,new_cap): #
        
        return (new_cap * ctypes.py_object)() #
    
arr = DynamicArray()

arr.append(1)

print(len(arr))

arr.append(2)
            
arr.append(3)

print(sys.getsizeof(arr))