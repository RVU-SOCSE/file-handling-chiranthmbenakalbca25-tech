Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import os
>>> print(os.listdir("C:/Users/manub/Desktop/CHIRU/PYTHON"))
['7 divisible.py', 'assign.py', 'days.py', 'experience.csv', 'FULL.py', 'match.py', 'odd and even numbers.py', 'prime number.py', 'remainder.py', 'vowels.py', 'year.py']
>>> import os
>>> os.rename("C:/Users/manub/Desktop/CHIRU/PYTHON/match.py","C:/Users/manub/Desktop/CHIRU/PYTHON/the_match.py")
>>> import shutil
>>> shutil.copy("C:/Users/manub/Desktop/CHIRU/PYTHON/days.py","C:/Users/manub/Desktop/CHIRU/PYTHON/copy.py")
'C:/Users/manub/Desktop/CHIRU/PYTHON/copy.py'
>>> import shutil
>>> shutil.move("C:/Users/manub/Desktop/CHIRU/PYTHON/days.py","C:/Users/manub/Desktop/CHIRU")
'C:/Users/manub/Desktop/CHIRU\\days.py'
>>> shutil.move("C:/Users/manub/Desktop/CHIRU/days.py","C:/Users/manub/Desktop/CHIRU/PYTHON")
'C:/Users/manub/Desktop/CHIRU/PYTHON\\days.py'
