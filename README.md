# Employee-Salary-Prediction

## About the Project

This project predicts the **salary class** of an employee using a machine learning model based on the **K-Nearest Neighbors (KNN)** algorithm. The model is integrated into a user-friendly **Graphical User Interface (GUI)** using **Tkinter**, allowing real-time predictions based on user input. It also supports a CLI-based mode for those who prefer terminal interaction.

---

##  System Development Approach

###  System Requirements

- Python 3.10 or higher  
- `employee_data.csv` dataset  
- Compatible with Windows/Linux/MacOS

###  Libraries Used

- `pandas` – data processing  
- `numpy` – numerical operations  
- `scikit-learn` – ML model training & evaluation  
- `joblib` – model serialization  
- `tkinter` – GUI (built-in)

---

##  Step-by-Step Procedure

1. Import libraries  
2. Load dataset (`employee_data.csv`)  
3. Clean and preprocess data  
4. Select relevant features  
5. Perform train-test split  
6. Scale features using `StandardScaler`  
7. Train K-Nearest Neighbors model  
8. Save model and scaler using `joblib`  
9. Build GUI using `Tkinter`  
10. Load saved model in GUI  
11. Get user input and make prediction  
12. Display salary class prediction

---

##  How to Run the Project

###  Install Required Packages

```bash
pip install pandas numpy scikit-learn
```

###  Train the Model

Ensure `employee_data.csv` is available in the directory.

```bash
python train_modell.py
```

This will generate:
- `knn_model.pkl`
- `scaler.pkl`

###  Launch the GUI

```bash
python employee_salary_prediction.py
```

---

##  GUI Overview

The GUI allows users to enter the following features:

- Age  
- Distance From Home  
- Education  
- Job Level  
- Monthly Income  
- Percent Salary Hike  
- Stock Option Level  
- Total Working Years  
- Years At Company

After clicking **"Predict Salary Class"**, the predicted result appears below the button.

```
Predicted Salary Class: Medium
```

---

##  Result

- The model predicts the salary class of an employee as either **Low**, **Medium**, or **High**.
- Accuracy may vary depending on the input data distribution and feature scaling.

---

##  Conclusion

This project demonstrates a basic but effective machine learning pipeline, from data loading and model training to GUI deployment. It can serve as a foundational ML + GUI integration project, ideal for HR analytics or academic purposes.

---

##  Future Scope

- Try other ML algorithms like Random Forest, SVM, or XGBoost  
- Improve GUI using custom styling or use web-based UI like Streamlit  
- Add CSV upload and batch prediction  
- Integrate model evaluation metrics and graphs  
- Deploy the app online using Flask/Django

---

##  References

- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Tkinter GUI Guide](https://docs.python.org/3/library/tkinter.html)
- HR Dataset (custom/prepared data)

---



