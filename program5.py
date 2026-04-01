Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> df = pd.read_csv("C:/Users/manub/Desktop/CHIRU/PYTHON/prog5.csv")
>>> print(df)
   YearsExperience
0              1.1
1              1.3
2              1.5
3              2.0
4              2.2
5              2.9
6              3.0
7              3.2
8              3.2
>>> print(df.shape)
(9, 1)
>>> print(len(df))
9
>>> print(df.head(2))
   YearsExperience
0              1.1
1              1.3
