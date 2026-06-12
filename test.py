from src.cleaner import clean_data
from src.visualizer import generate_salary_chart

df, report = clean_data("uploads/Employee.csv")

df.to_csv("cleaned/cleaned_employees.csv", index=False)

generate_salary_chart(df)

print("Data cleaned successfully!")
print("\nCleaning Report:")
print(report)
print("\nChart saved successfully!")