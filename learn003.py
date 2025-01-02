"""
实现一个支持动态增量的计数器
"""
class Counter:
    def __init__(self):
        # 使用字典存储计数
        self.counts = {}

    def increment(self, key: str, delta: int) -> None:
        # 如果键已存在，增加值，否则初始化为 delta
        if key in self.counts:
            self.counts[key] += delta
        else:
            self.counts[key] = delta

    def decrement(self, key: str, delta: int) -> None:
        # 如果键已存在，减少值，否则初始化为 -delta
        if key in self.counts:
            self.counts[key] -= delta
        else:
            self.counts[key] = -delta

    def get(self, key: str) -> int:
        # 返回键对应的计数值，若键不存在，则返回 0
        return self.counts.get(key, 0)

# 测试代码
counter = Counter()
counter.increment("a", 5)
counter.increment("b", 3)
counter.decrement("a", 2)
print(counter.get("a"))  # 输出 3
print(counter.get("b"))  # 输出 3
print(counter.get("c"))  # 输出 0
