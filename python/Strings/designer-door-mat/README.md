Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
- Mat size must be _N_ X _M_. (_N_ is an odd natural number, and _N_ is _3_ times _M_.)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use |, _._ and _-_ characters.

**Sample Designs***
````
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
````

**Input Format**
A single line containing the space separated values of  and .

**Constraints**
- 5< N <101
- 15< M < 303

**Output Format**
Output the design pattern.

**Sample Input**
````
9 27
````
**Sample Output**
````
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
````