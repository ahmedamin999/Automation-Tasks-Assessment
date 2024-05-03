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

#### 5- Convert the USD salary to EGP
```ExchangeRate = 47.85```
``` df['Salary in (EGP)'] = df['Salary(USD)'] * ExchangeRate ```
assuming ExchangeRate = 47.85 

#### Print in the console some stats like: Average age, Median Salaries, Ratio between males and female employees
``` print(f"Average age: {df['Age'].mean()}")```

get average 'Age' value by using ``` df['Age'].mean()``` function then print it in console using ```print()```

```print(f"Median Salaries: {df['Salary_in_EGP'].median()}")``` to get Median.

```male_count = df[df['Gender'] == 'M'].shape[0] ``` to count number of males
``` female_count = df[df['Gender'] == 'F'].shape[0] ``` to count number of females
``` print(f"Ratio between male and female employees: {male_count}:{female_count}") ``` to get tha ratio between them and print it in the console


#### write the data in a new CSV file
```df.to_csv('B:\VOIS\Automation Task Assessment\Employees NEW.csv', index=False)``` write a path with a different file name to export the data frame after changing it into it
### Full Code:
[Full Code](https://github.com/ahmedamin999/Automation-Tasks-Assessment/blob/Task3/Task3_Python.py)
