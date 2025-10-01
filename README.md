Author: Galen Avram Flanagan

Date: 10/1/2002

dependencies:
- numbers for data type checks 
- pandas for dataframes and data manipulation
- matplotlib for charts and graphs
- random for seeds and random numbers
- pytorch for tests

A set of methods that can take in a csv file and get the average and standard deviation of a given column in the file. In addition it can print five random rows and create a graph of a given column of data. 

The original code did all of this globally not as functions and with limited committing, in addition the filepath to the data was hard coded so one would have to put the file in the correct location with the exact name. I fixed this by create 4 function around the parts of code. 1 to get the average, one to get the sample standard deviation, one to print 5 rows at random, and one to plot the values of a given column. In addition I added docstrings for all functions. In addition I removed loops where possible instead using pandas built in methods for average and standard deviation. 

This allows the code to be reused for more purposes and not require changes everysingle time someone wants to use the code for a different dataset or on a different column value. In addition it is much easier to figure out what the code does as the docstrings explain in detail the inputs, outputs and effects of each function ensuring one can easily find the right function they want. 

In addition I also added several error cases. The error cases help users realize quickly when their inputs are invalid and exactly what part of their inputs are invalid. This can streamline the use of the code and help minimize frustration of future programers by allowing them to easily spot minor errors like typo's (important to me as I make a lot of them when coding)

Lastly I added tests. These ensure that all functions are working appropriately and that other users will not have to fix the code in the future. 