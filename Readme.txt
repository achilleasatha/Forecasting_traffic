Given an airport's total monthly passenger counts for a period of  months, forecast its passenger count for the next months.

Input Format

The first line contains an integer, , denoting the number of months of passenger data. The  subsequent lines each contain the monthly passenger counts in the form of  tab-separated values:

The first value is , where  is an an integer denoting the month number.
The second value is an integer denoting the number of passengers for that month.
Scoring

The final score obtained upon submitting your code is solely dependent on the hidden test case. We will compute the mean of the magnitude of the percentage difference by comparing your expected answers with the actual sessions for each of the missing records in all test cases (samples included).

 (for all forecasted values in all test cases).

Your final score on a scale of  will be:

If the mean value of  exceeds  (i.e.: your predictions are off by  or more on average), you will score zero. If your predictions are right on target, you will score .

When you hit  (instead of submit), we will run your solution against the sample test only. At that time, the visible score will be normalized out of  rather than . In case your program throws an error (or has an incorrect output format) for a single test case, the overall score assigned will be zero.

You may make no more than 15 submissions for this problem, during the contest.

Constraints


Output Format

For each line  (where ), print the forecasted passenger count for month number  on a new line.