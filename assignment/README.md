# Debugging Calendar Program

This document outlines the debugging process for the provided calendar program.

# Original Issue:

The code failed to detect the double bookings when the overlap occured. The insertion logic method was wrongly written which led to incorrect insertion of a new node as a left or right child, and hence missed overlap detection. The calls in insert function did not handle all edge cases efficiently, especially for cases that might result in an unbalanced tree. There was also no input validation for start and end parameters.

# Debugging Steps:

    1. Analyze Code: 
        I checked the calendar and node classes while running the original code in multiple scenarios. Observed that double bookings were not always detected correctly. Mainly to find the cases where algorithm is inserting the wrong nodes. Due to this I came to know there isa bug in insertion logic

    2. Understanding Insertion Logic: 
        This is the important part of the code. First, I looked closely at the conditions (node.start <= self.end and node.end >= self.start) that determine whether the left or right child should be placed in the insert method. The concept of non-overlapping periods is not covered by these overly permissive requirements. Correcting the insert logic, which addresses all edge cases and input validation, is the next stage.

    3. Insertion Logic Correction: 
        The below conditions were added with edge cases and input validation checks:

            a. node.start < node.end: Input validation check
            b. node.start >= self.end: If the start value is greater than parent end value, then child must be added as right child.
            c. node.end <= self.start: If the end value is less than parent start value, then child must be added as left child.
            d. Otherwise: If both cases were failed which shows an overlap occured indicating the given interval is between the start end interval, hence False needed to be returned.

    4. Final Step: 
        To check the logic, I ran the code with many input cases, which covers all the edge cases and validations.
