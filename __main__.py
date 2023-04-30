from sort_benchmark import *
from sort_methods import *


if __name__ == '__main__':
    sort_benchmark([sorted, quick_sort, cyril_quick_sort_bubble], 100000, 1000, 50)
    #sort_benchmark([sort_methods.bubble_sort, sort_methods.enhanced_bubble_sort, sort_methods.cyril_bubble_sort], 10000, 1000, 15)