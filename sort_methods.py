from random import shuffle
from time import time
import matplotlib.pyplot as plt
from typing import Callable
from tqdm import tqdm

class sort_methods:
    @staticmethod
    def merge_sort(l : list):
        if len(l) in (1,0):
            return l
        
        x = sort_methods.merge_sort([*l[:len(l)//2]])
        r = sort_methods.merge_sort([*l[len(l)//2:]])
        i = j = k = 0
        while i < len(x) and j < len(r):
            if x[i] < r[j]:
                l[k] = x[i]
                i+=1
            else:
                l[k] = r[j]
                j+=1
            k+=1

        if i < len(x):
            l[k:] = x[i:]

        if j < len(r):
            l[k:] = r[j:]

        return l
    
    @staticmethod
    def enhanced_bubble_sort(l : list):
        for i in range(len(l)):
            t = False
            for j in range(len(l)-i-1):
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]
                    t = True
            if not t:
                return l
        return l

    @staticmethod
    def bubble_sort(l : list):
        for i in range(len(l)):
            for j in range(len(l)-i-1):
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]
        return l
    
    @staticmethod
    def quick_sort(l : list):
        if len(l) in (1,0):
            return l
        
        pivot = l[-1]
        sup = inf =[]
        for elem in l[:-1]:
            if elem > pivot:
                sup.append(elem)
            else:
                inf.append(elem)
        
        return sort_methods.quick_sort(inf) + [pivot] + sort_methods.quick_sort(sup)

    
    @staticmethod
    def bogo_sort(l : list):
        def is_sorted(l):
            for i in range(len(l[:-1])):
                if l[i] > l[i+1]:
                    return False
            return True
        
        while not is_sorted(l):
            shuffle(l)
        return l
    
    @staticmethod
    def quick_sort_bubble(l : list):
        if len(l) in (1,0):
            return l
        if len(l)<=10:
            return sort_methods.cyril_bubble_sort(l)
        pivot = l[-1]
        sup = inf = []
        for elem in l[:-1]:
            if elem > pivot:
                sup.append(elem)
            else:
                inf.append(elem)
        
        return sort_methods.quick_sort_bubble(inf) + [pivot] + sort_methods.quick_sort_bubble(sup)
        
    
    @staticmethod
    def cyril_quick_sort(data : list, start : int = 0, end : int|None = None):
        if end == None:
            end = len(data)-1
        elif end >= len(data):
            end = len(data)-1
        if start >= end:
            return
        
        p = (start + end)//2
        j = start
        s = data[end]
        data[end]=data[p]
        data[p] = s
        for i in range(start,end):
            if(data[i]<= data[end]):
                s=data[i]
                data[i] = data[j]
                data[j] = s
                j+=1
        p=j
        
        s = data[end]
        data[end]=data[p]
        data[p] = s
        
        sort_methods.cyril_quick_sort(data,start,p-1)
        sort_methods.cyril_quick_sort(data,p+1,end)
        return(data)

    @staticmethod
    def insertion_sort(l : list):
        for i in range(len(l)):
            j = i
            while j>0 and l[j-1]>l[j]:
                l[j], l[j-1] = l[j-1], l[j]
                j-=1
        return l
    
    @staticmethod
    def cyril_bubble_sort(data,start=0,n=None):
        if n == None:
            n = len(data)
        while n > 0:
            newn = 0
            for j in range(start+1,n):
                if(data[j-1]>data[j]):
                    s=data[j]
                    data[j]=data[j-1]
                    data[j-1]=s
                    newn=j
            n=newn
        return data
    
    @staticmethod
    def cyril_quick_sort_bubble(data,start=0,end=None,threshold=10):
        if end == None:
            end = len(data)-1
        elif end >= len(data):
            end = len(data)-1
        if start >= end:
            return 
        if end-start <= threshold :
            return sort_methods.cyril_bubble_sort(data,start,end)
        
        p = data[(start + end)//2]
        i = start
        j = end
        
        while True :
            
            while data[i]<p :
                i+=1
            
            while data[j]>p:
                j-=1
            
            if i>=j:
                break
            
            s=data[i]
            data[i]=data[j]
            data[j]=s
        
        sort_methods.cyril_quick_sort_bubble(data,start,j)
        sort_methods.cyril_quick_sort_bubble(data,j+1,end)
        return(data)

class sort_benchmark:
    def __init__(self, methods : list[Callable], max_it : int, shift : int = 100, it : int  = 10) -> None:
        self.max = max_it
        self.list = [j for j in range(self.max)]
        self.x  = [j for j in range(1,self.max,shift)]
        self.y = self.advanced_bench(methods, it, shift)
        self.plot(methods)

    def bench(self, func : Callable, shift : int):
        y = []
        for i in tqdm(range(2,self.max+1, shift), desc='bench'):
            x = [*self.list[:i]]
            s = time()
            x = func(x)
            e = time()
            y.append(e-s)
        return y
    
    def advanced_bench(self, funcs : Callable, it : int, shift = int):
        results = {f.__name__ : [] for f in funcs}
        for _ in tqdm(range(it), desc='Number of it'):
            shuffle(self.list)
            for f in funcs:
                results[f.__name__].append(self.bench(f, shift))
        r = []
        for f in funcs:
            r.append(self.avg_res(results[f.__name__]))
        
        return r

    def avg_res(self, l : list[list[float]]):
        new_l = []
        for i in range(len(l[0])):
            new_l.append(0)
            for j in range(len(l)):
                new_l[i] += l[j][i]/len(l[0])
        return new_l
    
    def plot(self, methods : Callable):
        fig, ax = plt.subplots()
        for i, m in enumerate(methods):
            ax.plot(self.x, self.y[i], label = m.__name__.replace('_',' '))
            ax.legend()
        plt.show()

if __name__ == '__main__':
    sort_benchmark([sort_methods.quick_sort, sort_methods.cyril_quick_sort, sort_methods.cyril_quick_sort_bubble, sort_methods.quick_sort_bubble], 50000, 500, 20)
    #sort_benchmark([sort_methods.bubble_sort, sort_methods.enhanced_bubble_sort, sort_methods.cyril_bubble_sort], 5000)
