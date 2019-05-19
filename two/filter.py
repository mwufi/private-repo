import sys


def cut(numbers, disp=False):
    """Filter the input to create a balanced data
    
    Params:
    numbers - array of floats in [0.0, 1.0)
    """
    intervals = [0.2, 0.4, 0.6, 0.8, 1.0]
    buckets = [[] for i in intervals]
    for num in numbers:
        # find the right bucket
        for i, right in enumerate(intervals):
            if num < right:
                buckets[i].append(num)
                break
    
    if disp:
        print('Buckets:\n', buckets)
        
    # find out how many values to keep
    k = min([len(b) for b in buckets])
    
    # take k values from each bucket
    buckets = [b[:k] for b in buckets]
    data = []
    for b in buckets:
        data += b
        
    return data


def process(numbers):
    numbers = [str(x) for x in cut(numbers)]
    print(','.join(numbers))

    
if __name__ == "__main__":
    for x in sys.stdin:
        numbers = [float(i.strip()) for i in x.split(',')]
        process(numbers)