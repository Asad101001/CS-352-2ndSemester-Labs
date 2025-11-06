from sequence_analyzer import SequenceAnalyzer

nums = [1, 2, 3]
s = SequenceAnalyzer(nums)
nums.append(4)
print(s.data)

##  [1, 2, 3, 4]
