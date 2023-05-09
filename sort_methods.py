from random import shuffle
from typing import Callable
from datastructures import *

def merge_sort(l : list):
    if len(l) in (1,0):
        return l
        
    x = merge_sort([*l[:len(l)//2]])
    r = merge_sort([*l[len(l)//2:]])
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

def insertion_sort(l : list):
    for i in range(1,len(l)+1):
        j = i
        while(j>0 and l[j]<l[j-1]):
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1


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

def bubble_sort(l : list):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

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
    
    l = quick_sort(inf) + [pivot] + quick_sort(sup)
    return l

def bogo_sort(l : list):
    def is_sorted(l):
        for i in range(len(l[:-1])):
            if l[i] > l[i+1]:
                return False
        return True
    
    while not is_sorted(l):
        shuffle(l)
    return l

def quick_sort_bubble(l : list):
    if len(l) in (1,0):
        return l
    if len(l)<=10:
        return cyril_bubble_sort(l)
    pivot = l[-1]
    sup = []
    inf = []
    for elem in l[:-1]:
        if elem > pivot:
            sup.append(elem)
        else:
            inf.append(elem)
    
    l = quick_sort_bubble(inf) + [pivot] + quick_sort_bubble(sup)
    return l
    
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
            data[j], data[i] =data[i], data[j]
            j+=1
            
    data[end], data[j] = data[j], data[end]
    
    cyril_quick_sort(data,start,j-1)
    cyril_quick_sort(data,j+1,end)
    return(data)

def insertion_sort(l : list):
    for i in range(len(l)):
        j = i
        while j>0 and l[j-1]>l[j]:
            l[j], l[j-1] = l[j-1], l[j]
            j-=1
    return l

def cyril_bubble_sort(data,start=0,n=None):
    if n == None:
        n = len(data)
    while n > 0:
        newn = 0
        for j in range(start+1,n):
            if(data[j-1]>data[j]):
                data[j], data[j-1]=data[j-1], data[j]
                newn=j
        n=newn
    return data

def cyril_quick_sort_bubble(data,start=0,end=None,threshold=10):
    if end == None:
        end = len(data)-1
    elif end >= len(data):
        end = len(data)-1
    if start >= end:
        return 
    if end-start <= threshold :
        return cyril_bubble_sort(data,start,end)
    
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
        
        data[i], data[j]=data[j], data[i]
    
    cyril_quick_sort_bubble(data,start,j)
    cyril_quick_sort_bubble(data,j+1,end)
    return(data)

def __tim_sort_min_run(min : int, n : int):
    r=0
    while n >= min:
        r |= n & 1
        n >>= 1
    return n + r

def tim_sort(l : list)->list:
    n = len(l)
    m = __tim_sort_min_run(32, n)

    for s in range(0, n, m):
        e = min(s+m-1, n-1)
        l[s:e] = insertion_sort(l[s:e])

    while m < len(l):
        for i in range(0, n, 2*m):
            mid = min(n - 1, i + m - 1)
            right = min(i + 2 * m, n)
            if mid < right:
                l[i:right] = merge_sort(l[i:right])
        m*=2
    
    return l

def tree_sort(l : list)->list:
    t = Binary_sort_node(l[0])
    for e in l[1:]:
        t.add_value(e)
    l=t.get_sorted()
    return l

def test_sort(method : Callable, n : int):
    l = [i for i in range(n)]
    shuffle(l)
    print(method(l))

if __name__ == '__main__':
    test_sort(tree_sort, 10000)
