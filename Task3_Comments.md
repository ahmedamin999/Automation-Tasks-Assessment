# Automation-Tasks-Assessment
## Task 3: Python
### Introduction
According to the requirements in task 3, I had to use a library that analyzes data sets. After searching, **"Pandas"** was the best library to do this task because It has functions for analyzing, cleaning, exploring, and manipulating data.

### Code Details:
#### 1- Import Pandas Library to use in this code as 
``` import pandas as pd ```

#### 2- define DataFrane as 'df' and load the data into it
``` df = pd.read_csv('B:\VOIS\Automation Task Assessment\Employees.csv')```
where ``` 'B:\VOIS\Automation Task Assessment\Employees.csv' ``` is the path of CSV file in my PC.

#### 3- Remove duplicates data in df
```  df.drop_duplicates(inplace=True) ```
using ``` drop_duplicates``` function

#### 4- Remove any decimal places in the Age column
``` df['Age'] = df['Age'].astype(int) ```
We can use ``` astype(int)``` to cast all data in 'Age' Column into integer then replace new data instaded of old data 

[Full Code](https://github.com/ahmedamin999/Automation-Tasks-Assessment/blob/Task3/Task3_Python.py)
