import pandas as pd 
import os


# Files to load
school_data_to_load = os.path.join("Resources", "schools_complete.csv")
student_data_to_load = os.path.join("Resources", "students_complete.csv")

# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
print(school_data_df)
student_data_df = pd.read_csv(student_data_to_load)
print(student_data_df)