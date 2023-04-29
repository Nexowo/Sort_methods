from random import shuffle
from time import time
import matplotlib.pyplot as plt
from typing import Callable
from tqdm import tqdm

class sort_benchmark:
    def __init__(self, methods : list[Callable[...,list]], max_it : int, shift : int = 100, it : int  = 10) -> None:
        self.max = max_it
        self.list = [j for j in range(self.max)]
        self.x  = [j for j in range(1,self.max,shift)]
        self.y = self.advanced_bench(methods, it, shift)
        self.plot(methods)

    def bench(self, func : Callable, shift : int):
        y = []
        for i in tqdm(range(2,self.max+1, shift), desc=func.__name__):
            x = [*self.list[:i]]
            s = time()
            x = func(x)
            e = time()
            y.append(e-s)
        return y
    
    def advanced_bench(self, funcs : list[Callable[...,list]], it : int, shift = int):
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
    
    def plot(self, methods : Callable[..., list]):
        fig, ax = plt.subplots()
        for i, m in enumerate(methods):
            ax.plot(self.x, self.y[i], label = m.__name__.replace('_',' '))
            ax.legend()
        plt.show()