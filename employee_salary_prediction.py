import sys
import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

def predict_salary(features):
    model = joblib.load("model.pkl")
    prediction = model.predict([features])
    return prediction[0]

def run_gui():
    def submit():
        try:
            features = [
                int(entry_age.get()),
                int(entry_education_num.get()),
                int(entry_hours.get())
            ]
            pred = predict_salary(features)
            messagebox.showinfo("Prediction", f"Predicted Salary Class: {pred}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")

    root = tk.Tk()
    root.title("Employee Salary Predictor")

    tk.Label(root, text="Age:").grid(row=0, column=0)
    entry_age = tk.Entry(root)
    entry_age.grid(row=0, column=1)

    tk.Label(root, text="Education Number:").grid(row=1, column=0)
    entry_education_num = tk.Entry(root)
    entry_education_num.grid(row=1, column=1)

    tk.Label(root, text="Hours per Week:").grid(row=2, column=0)
    entry_hours = tk.Entry(root)
    entry_hours.grid(row=2, column=1)

    submit_btn = tk.Button(root, text="Predict", command=submit)
    submit_btn.grid(row=3, column=0, columnspan=2)

    root.mainloop()

def run_cli():
    print("Enter the following details:")
    age = int(input("Age: "))
    education_num = int(input("Education Number: "))
    hours_per_week = int(input("Hours per week: "))
    features = [age, education_num, hours_per_week]
    result = predict_salary(features)
    print(f"Predicted Salary Class: {result}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "gui":
        run_gui()
    else:
        run_cli()
