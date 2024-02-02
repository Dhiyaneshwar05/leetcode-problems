class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
    #gen all seq digits -> 10 - 100 =>   12, 23, 34, 45, 56, 67, 78, 89
    #                   -> 100 - 3000 => 123, 234, 345, 456, 567,678, 789, 12345
    #logic -> len(low_range) -> len(up_range)
    #ld=len(str(low)) #2
    #hd=len(str(high)) #5"""
        a = []
        for i in range(1, 10):
            num = i
            next_digit = i + 1

            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                if low <= num <= high:
                    a.append(num)
                next_digit += 1

        a.sort()
        return a
    