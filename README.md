[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dianapolise/heart_disease/blob/main/heart_disease.ipynb)

# *Heart Disease*

This document leverages Seaborn, Pandas, NumPy, Scikit-Learn, XGBoost, and TensorFlow to conduct analytical investigations on a cardiovascular diseases dataset, aiming to evaluate the effects of various factors on disease outcomes. The dataset comprises key attributes from approximately 900 patients, including age, sex, resting blood pressure, fasting blood sugar, and other relevant variables.

Initially, four distinct Neural Network architectures were developed and evaluated to identify the model that best fits the dataset. The selected model was subsequently applied to the test set for validation. Additionally, Linear Regression and Logistic Regression models were trained using Scikit-Learn. Further analysis involved the implementation of a Decision Tree, a Random Forest, and an XGBoost model to ultimately determine the most effective approach for predicting cardiovascular conditions in future patients.

## ***Features***

Binary Classification: Implements 5 different model for distinguishing between two categories (e.g., Healthy or Heart disease).

Data Preprocessing: Handles and preprocesses data efficiently using pandas.

Data Visualization: Explores relationships and correlations in the dataset with seaborn.

## ***Installation***

To run this project, you’ll need:

- Python 3.12

- Libraries: numpy, pandas, seaborn, scikit-learn, tensorflow, xgboost

**Install the required dependencies using pip:**

```bash
pip install numpy pandas seaborn scikit-learn tensorflow xgboost
```

## ***Usage***

Clone this repository or download the notebook.

Open the provided Jupyter Notebook.

The built-in dataset is loaded and processed automatically within the notebook.

Run the notebook to:

- Train the model.

- Evaluate its performance.

- Visualize the results.

Outputs include metrics such as prediction accuracy (~85-88%) and insights from visualized relationships in the data.

## Dataset

This project utilizes the [Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) provided by **Federico Soriano** on Kaggle. The dataset contains labeled information to predict heart failure events based on a variety of features.

This dataset was created by combining different datasets already available independently but not combined before. In this dataset, 5 heart datasets are combined over 11 common features which makes it the largest heart disease dataset available so far for research purposes. The five datasets used for its curation are:

- Cleveland: 303 observations
- Hungarian: 294 observations
- Switzerland: 123 observations
- Long Beach VA: 200 observations
- Stalog (Heart) Data Set: 270 observations

***creators***:

Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.

University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.

University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.

V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.

***Donor***:

David W. Aha (aha '@' ics.uci.edu) (714) 856-8779

## ***Contributing***

For contributions or suggestions, feel free to reach out via the email provided at the end of the notebook.

## ***License***

This project is licensed under the CC0 (Creative Commons Zero) license. It is open-source and free to use, modify, and share.
