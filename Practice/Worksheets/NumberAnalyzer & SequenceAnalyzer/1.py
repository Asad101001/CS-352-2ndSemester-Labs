from sequence_analyzer import SequenceAnalyzer

nums = [1, 2, 3]
s = SequenceAnalyzer(nums)
nums.append(69)
print(s.data)

##  [1, 2, 3, 69]
