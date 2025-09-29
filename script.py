import pandas as pd

input_file = "Recruitment of UIU Advanced Underwater Robotics and Automation Crew-2026  (Responses).xlsx"

output_file = "Mechanical_Applicants.xlsx"

df = pd.read_excel(input_file, sheet_name=0)

# Filter candidates who applied for Mechanical position
mechanical_df = df[df['Position Preference'].str.contains("Mechanical", case=False, na=False)]

mechanical_df.to_excel(output_file, index=False)

print(f" saved to {output_file}")