# Time O(n log n)
# Space O(n)

from heapq import *
from collections import deque
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.available = []
        for i in range(maxNumbers):
            heappush(self.available, i)
        self.numstatus = [True] * maxNumbers


    def get(self) -> int:
        if len(self.available) > 0:
            num = heappop(self.available)
            self.numstatus[num] = False
            return num
        else: return -1

    def check(self, number: int) -> bool:
        return self.numstatus[number]

    def release(self, number: int) -> None:
        if not self.numstatus[number]:
            self.numstatus[number] = True
            heappush(self.available, number)

# Using queue
# Time O(n)
# Space O(n)
from collections import deque
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.available = deque()
        for i in range(maxNumbers):
            self.available.append(i)
        self.numstatus = [True] * maxNumbers


    def get(self) -> int:
        if len(self.available) > 0:
            num = self.available.popleft()
            self.numstatus[num] = False
            return num
        else: return -1

    def check(self, number: int) -> bool:
        return self.numstatus[number]

    def release(self, number: int) -> None:
        if not self.numstatus[number]:
            self.numstatus[number] = True
            self.available.append(number)



# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)