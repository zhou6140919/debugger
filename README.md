# My Custom Debugger

## Install
```
pip install ztdebugger
```

## Simple Usage

```
from ztdebugger import ic

def foo(i):
    return i + 333

    ic(foo(123))
```
Prints
```
ic| foo(123): 456
```

```
d = {'key': {1: 'one'}}
ic(d['key'][1])

class klass():
    attr = 'yep'
    ic(klass.attr)
```
Prints
```
ic| d['key'][1]: 'one'
ic| klass.attr: 'yep'
```

## Find where you are

```
from ztdebugger import ic


def hello():
    ic()
    if 1:
        ic()
    else:
        ic()


hello()
```
Prints
```
ic| tmp.py:5 in hello() at 20:59:30.457
ic| tmp.py:7 in hello() at 20:59:30.458
```

## Checkpoint

Add this inside your code anywhere you like
```
ic.d()
```

## Decorator

```
@ic.snoop()
def hello()
    s = "123"
    return s

print(hello())
```
Prints
```
Source path:... /Users/admin/Downloads/tmp.py
20:56:24.294518 call         5 def hello():
20:56:24.294597 line         6     s = "123"
New var:....... s = '123'
20:56:24.294608 line         7     return s
20:56:24.294623 return       7     return s
Return value:.. '123'
Elapsed time: 00:00:00.000135
123
```

## Colorful Debugger

```
from ztdebugger import ic

if __name__ == '__main__':
    ic.run(main)
```
