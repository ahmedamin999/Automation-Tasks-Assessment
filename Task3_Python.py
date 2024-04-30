import pandas as pd

# define DataFrane as 'df' and load the data into it
df = pd.read_csv('B:\VOIS\Automation Task Assessment\Employees.csv')

# Remove duplicates data in df using 'drop_duplicates' function
df.drop_duplicates(inplace=True)

# Convert the data in that Age column to integer values using 'astype(int)'.
df['Age'] = df['Age'].astype(int)

# Convert the USD salary to EGP (assuming 1 USD = 47.85 EGP)
ExchangeRate = 47.85
df['Salary in (EGP)'] = df['Salary(USD)'] * ExchangeRate

#### Print stats in the console:####
#	1- Average age
print(f"Average age: {df['Age'].mean()}")

#	2- Median Salaries
print(f"Median Salaries: {df['Salary_in_EGP'].median()}")
#	3- Ratio between males and female employees
male_count = df[df['Gender'] == 'M'].shape[0]
female_count = df[df['Gender'] == 'F'].shape[0]
print(f"Ratio between male and female employees: {male_count}:{female_count}")

# Write the data to a new CSV file
df.to_csv('B:\VOIS\Automation Task Assessment\Employees NEW.csv', index=False)

