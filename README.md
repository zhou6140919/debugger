# My Custom Debugger

## Features

 - [ ] Setup email address once
 - [x] Job fail email alert
 - [x] Easy-to-use functions

## Install
```bash
pip install ztdebugger
```

## Simple Usage

```python
from ztdebugger import ic

def foo(i):
    return i + 333

ic(foo(123))
```
Prints
```bash
ic| foo(123): 456
```

```python
d = {'key': {1: 'one'}}
ic(d['key'][1])

class klass():
    attr = 'yep'
ic(klass.attr)
```
Prints
```bash
ic| d['key'][1]: 'one'
ic| klass.attr: 'yep'
```

## Find where you are

```python
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
```bash
ic| tmp.py:5 in hello() at 20:59:30.457
ic| tmp.py:7 in hello() at 20:59:30.458
```

## Checkpoint

Add this inside your code anywhere you like
```python
ic.d()
```

## Decorator

```python
@ic.snoop()
def hello()
    s = "123"
    return s

print(hello())
```
Prints
```bash
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

As same as [rich.traceback.install()](https://rich.readthedocs.io/en/stable/traceback.html#automatic-traceback-handler)

```python
from ztdebugger import ic

# By default
ic.init()
# Add which email you want to send your exceptions to, only support qq sender now
# Send to yourself by default
ic.init(sender='xxx@qq.com', key='abcdefg')
# Or you can assign receiver to any email address you like
ic.init(sender='xxx@qq.com', receiver='xxx@126.com', key='abcdefg')

if __name__ == '__main__':
    main()
```
