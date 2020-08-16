- 第一周总结
  - 第一周总体感觉比较突兀，没有做好提前预习，所以从预习到第一周的课程要完全看一遍；
  - 还没有形成好的学习方法，属于探索。但经过一周的学习，知道了学习方法和节奏；
  - 第一周学习的基础知识，基本掌握了，老师讲的很到位，我基本从0到1学习，也掌握到关键点；
  - 每节课讲到的算法，双指针、夹逼等要按照老师的要求弄熟。

- 改写Deque（Python）
简单实现deque对象，使其具有 addfirst() 和 addlast() 接口：

```python
class Deque():
    def __repr__(self):
        return str(self.list)
    def __init__(self):
        self.list = []
        
    def addfirst(self, num):
        self.list = list[num].extend(self.list) 
    
    def addlast(self, num):
        self.list.append(num)
        
    def popleft(self):
        if not self.list: raise IndexError("pop from empty list")
        x = self.list[0]
        self.list.__delitem__(0)
        return x
    
    def popright(self):
        if not self.list: raise IndexError("pop from empty list")
        x = self.list[-1]
        self.list.__delitem__(-1)
        return x
```

