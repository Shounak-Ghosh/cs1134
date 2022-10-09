import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self,iter_collection=None):
        self.data_arr = make_array(1) # list data
        self.capacity = 1 # list true capacity
        self.n = 0 # list max index

        if (iter_collection != None):
            try:
                i = iter(iter_collection)
            except TypeError:
                raise TypeError('argument must be iterable') 
            
            for elem in iter_collection:
                self.append(elem)
            


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind

        return self.data_arr[ind]


    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind

        self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)
    
    # lab code starts here 
    def __repr__(self):
        return '[' + ', '.join([str(self[i]) for i in range(len(self))]) + ']'

    def __add__(self, other):
        new_arr = ArrayList()
        new_arr.extend(self)
        new_arr.extend(other)
        return new_arr
    
    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, other):
        new_arr = ArrayList()
        for i in range(other):
            new_arr.extend(self)
        return new_arr

    def __rmul__(self, other):
        return self * other
    
    def remove(self, val):
        found = False
        for i in range(self.n-1):
            if (self.data_arr[i] == val):
                found = True
            if found:
                self.data_arr[i] = self.data_arr[i+1]
        if found:
            self.n -= 1
            self.data_arr[self.n] = None

        if not found:
            raise ValueError('value not found')
    
    def removeAll(self, val):
        val_count = 0
        new_index = 0
        
        # use pointer new index to skip over all current indexes with val
        for i in range(self.n):
            if (self.data_arr[i] != val):
                self.data_arr[new_index] = self.data_arr[i]
                new_index += 1
            else: 
                val_count += 1 # need to subtract final val_count from n

        self.n -= val_count

           

    
    

    
