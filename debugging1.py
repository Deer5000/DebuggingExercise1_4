"""
Example Program
Use this as an example of how to work through the steps in the lesson.
"""
# PART 1: Gather Information
#
# Here is the stack trace we get from running the program:
# Traceback (most recent call last):
#   File "main.py", line 23, in <module>
#     answer = find_largest_number([3, 2, 1, 5, 4])
#   File "main.py", line 18, in find_largest_number
#     if list_of_nums[i] > largest_num:
# IndexError: list index out of range
# 
# According to the stack trace, there is an IndexError on line 18. That must mean that the variable 
# i is outside of the bounds of the list. That means we need to find out why i has a value that's
# greater than or equal to the length of the list.
# PART 2: State Assumptions
# "The first thing we do is set largest_num to the first element of the list. Is that actually what 
# happens? Let's insert a print statement and find out... Yep, largest_num gets set to 3."
#
# "Next, we loop over each number in list_of_nums and set its index to the variable i. Is that 
# actually true? Let's insert a print statement and find out... Nope, i is actually set to the 
# _value_ at each index. OK, that must be what is causing the bug."
#
# ... continue on until you've verified that you found the cause of the bug and fixed it ...
def find_largest_number(list_of_nums):
    largest_num = list_of_nums[0]
    for i in list_of_nums:
        if i > largest_num:
            largest_num = i
    return largest_num
if __name__ == '__main__':
    print('### Example ###')
    answer = find_largest_number([3, 2, 1, 5, 4])
    print(answer) # should print 5




    """
Exercise 1
"""
# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?
# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums) - 1):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff
    return largest_diff
if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])
    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)





"""
Exercise 2
"""
# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?
# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
        else:
            return False
    return False
if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False
    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True