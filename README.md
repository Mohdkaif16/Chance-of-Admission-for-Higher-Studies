
# 🎓 Graduate Admission Predictor

This project predicts the **chance of admission** to a graduate program based on student inputs such as GRE, TOEFL, CGPA, and more. It uses **Linear Regression** and provides a **Tkinter-based GUI** for easy interaction.

## 🔍 Features

- Predicts admission probability using 7 key features:
  - GRE Score
  - TOEFL Score
  - University Rating
  - Statement of Purpose (SOP)
  - Letter of Recommendation (LOR)
  - Undergraduate CGPA
  - Research Experience (0 or 1)
- Interactive GUI built with Tkinter
- Simulated training data
- Easy to run and modify

## 📦 Requirements

Install the required Python libraries using pip:

```bash
pip install pandas numpy scikit-learn
```

Tkinter is usually included with Python installations. If not, install it using your package manager:

- For Windows: Already included
- For Ubuntu/Debian:
  ```bash
  sudo apt-get install python3-tk
  ```

## 🚀 How to Run

1. Clone the repository or download the Python file:
   ```bash
   git clone https://github.com/your-username/admission-predictor.git
   cd admission-predictor
   ```

2. Run the program:
   ```bash
   python admission_predictor.py
   ```

3. A GUI will open. Enter the student's details and click "Predict Admission Chance" to view the result.

## 🛠 Customization

- To use a real dataset instead of the generated one, modify the section:
  ```python
  df = pd.read_csv("your_dataset.csv")
  ```

- You can also save and load the model using `pickle` for better performance in production.

## 📷 Screenshot

![screenshot](screenshot.png) *(Add a screenshot of the GUI here)*

## 🤖 Author

- Developed by: [Your Name]
- LinkedIn: [Your LinkedIn Profile]
- GitHub: [Your GitHub Profile]

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
