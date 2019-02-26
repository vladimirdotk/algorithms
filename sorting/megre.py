from typing import Callable, List, Dict
from functools import wraps

def decor(func: Callable):
    @wraps(func)
    def inner(*args: List, **kwargs: Dict):
        #print(args, kwargs)
        print(locals().keys())
        return func(*args, **kwargs)
    return inner

@decor
def hello(x: int, y: int, z: int):
    print(locals().keys())

hello(1,2, z=3)
