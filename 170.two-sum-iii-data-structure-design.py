class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.hash = {}
        self.count = 0

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)
        self.hash[number] = self.count
        self.count += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if len(self.nums) <= 1:
            return False
        for i in range(len(self.nums)):
            tar = value - self.nums[i]
            if tar in self.hash and self.hash[tar] != i:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
