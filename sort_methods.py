from random import shuffle
from time import time
import matplotlib.pyplot as plt
from typing import Callable

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
            t = True
            for j in range(len(l)-i-1):
                t = False
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]
                    t = True
            if not t:
                break
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
        sup = []
        inf = []
        for elem in l[:-1]:
            if elem > pivot:
                sup.append(elem)
            else:
                inf.append(elem)
        
        l = sort_methods.quick_sort(inf) + [pivot] + sort_methods.quick_sort(sup)
        return l
    
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
        if len(l)<=5:
            return sort_methods.bubble_sort(l)
        pivot = l[-1]
        sup = []
        inf = []
        for elem in l[:-1]:
            if elem > pivot:
                sup.append(elem)
            else:
                inf.append(elem)
        
        l = sort_methods.quick_sort_bubble(inf) + [pivot] + sort_methods.quick_sort_bubble(sup)
        return l
    
    @staticmethod
    def insertion_sort(l : list):
        for i in range(len(l)):
            j = i
            while j>0 and l[j-1]>l[j]:
                l[j], l[j-1] = l[j-1], l[j]
                j-=1
        return l

class sort_benchmark:
    def __init__(self, methods : list[Callable], max_it : int, shift : int = 100) -> None:
        self.max = max_it
        self.list = [j for j in range(self.max)]
        self.x  = [j for j in range(1,self.max,shift)]
        self.y = self.advanced_bench(methods, 10, shift)
        self.plot(methods)

    def bench(self, func : Callable, shift : int):
        y = []
        for i in range(2,self.max+1, shift):
            x = [*self.list[:i]]
            s = time()
            x = func(x)
            e = time()
            y.append(e-s)
        return y
    
    def advanced_bench(self, funcs : Callable, it : int, shift = int):
        results = {f.__name__ : [] for f in funcs}
        for _ in range(it):
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
    sort_benchmark([sort_methods.enhanced_bubble_sort, sort_methods.bubble_sort], 5000)
