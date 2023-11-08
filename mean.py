import pandas as pd

# Create a list of data
data = [
    {"patient_id": 12345, "age": 25, "sex": "Male", "weight": 175, "height": 75, "bmi": 25, "case_id": 123456, "follow_up_days": 30, "status": "Active"},
    {"patient_id": 65432, "age": 35, "sex": "Female", "weight": 160, "height": 60, "bmi": 20, "case_id": 654321, "follow_up_days": 25, "status": "In Progress"},
    {"patient_id": 78901, "age": 45, "sex": "Male", "weight": 180, "height": 80, "bmi": 28, "case_id": 789012, "follow_up_days": 15, "status": "Completed"},
    {"patient_id": 90123, "age": 55, "sex": "Female", "weight": 150, "height": 55, "bmi": 22, "case_id": 901234, "follow_up_days": 5, "status": "Pending"},
    {"patient_id": 101234, "age": 65, "sex": "Male", "weight": 190, "height": 90, "bmi": 32, "case_id": 1012345, "follow_up_days": 0, "status": "Cancelled"},
]

# Create a DataFrame
df = pd.DataFrame(data)

# Print the average age of all patients
print(df['age'].mean())