
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from tkinter import *
from tkinter import messagebox

# Step 1: Create or simulate dataset
data = {
    'GRE Score': np.random.randint(290, 341, 100),
    'TOEFL Score': np.random.randint(92, 121, 100),
    'University Rating': np.random.randint(1, 6, 100),
    'SOP': np.round(np.random.uniform(1, 5, 100), 1),
    'LOR ': np.round(np.random.uniform(1, 5, 100), 1),
    'CGPA': np.round(np.random.uniform(6.8, 9.92, 100), 2),
    'Research': np.random.randint(0, 2, 100),
}

df = pd.DataFrame(data)

# Simulate target variable (Chance of Admit)
df['Chance of Admit '] = np.round(
    0.01 * df['GRE Score'] +
    0.02 * df['TOEFL Score'] +
    0.1 * df['University Rating'] +
    0.1 * df['SOP'] +
    0.1 * df['LOR '] +
    0.2 * df['CGPA'] +
    0.05 * df['Research'] +
    np.random.normal(0, 0.05, 100), 2
)
df['Chance of Admit '] = df['Chance of Admit '].clip(0, 1)

# Step 2: Train model
X = df[['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research']]
y = df['Chance of Admit ']
model = LinearRegression()
model.fit(X, y)

# Step 3: GUI App with Tkinter
root = Tk()
root.title("Graduate Admission Predictor")
root.geometry("400x600")

fields = [
    ("GRE Score (290–340)", 290, 340),
    ("TOEFL Score (92–120)", 92, 120),
    ("University Rating (1–5)", 1, 5),
    ("Statement of Purpose (1–5)", 1, 5),
    ("LOR Strength (1–5)", 1, 5),
    ("Undergraduate CGPA (6.8–9.92)", 6.8, 9.92),
    ("Research (0 or 1)", 0, 1)
]

entries = []

def predict():
    try:
        input_data = []
        for i, (label, min_val, max_val) in enumerate(fields):
            val = float(entries[i].get())
            if val < min_val or val > max_val:
                raise ValueError(f"{label} must be between {min_val} and {max_val}")
            input_data.append(val)
        input_array = np.array(input_data).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        messagebox.showinfo("Prediction Result", f"Predicted Chance of Admission: {prediction:.2f}")
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {str(e)}")

# UI Layout
Label(root, text="Enter Student Details", font=("Helvetica", 16, "bold")).pack(pady=10)

for label_text, min_val, max_val in fields:
    Label(root, text=label_text).pack()
    entry = Entry(root)
    entry.pack(pady=5)
    entries.append(entry)

Button(root, text="Predict Admission Chance", command=predict, bg="green", fg="white", font=("Arial", 12)).pack(pady=20)

root.mainloop()
