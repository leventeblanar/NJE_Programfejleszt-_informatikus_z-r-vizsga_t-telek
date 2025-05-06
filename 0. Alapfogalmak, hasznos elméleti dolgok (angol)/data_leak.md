<h2>Data leak</h2>

Definition: A situation where sensitive, secure data or simply data that should not be public is placed into a process or accidentally becomes part of a process where it should not be. Because of this the system provides faulty, misleading or far better results back.

Examples:
- Machine Learning: The model sees data thatit should not beucase it can help it in future predictions
eg.: a bank model is trying to forecast if someone will pay back their loans
```
"Loan_paid_back" = Yes / No
```
If this gets into the teaching data, the model will be able to precisely tell what the outcome will be and this is not prediction, this is knowing which is not learning but teaching.

- Informational security: secure data gets out (eg.: API Key, client data)
eg.: code section is being hard coded into the code that is uploaded to GitHub 
openly accessable json file on a public server
accidentally sent in an email
token being written into a log file

- Data handling (eg. Pandas): when we merge two dataframes and one contains a column that it should not 
eg.: order_df (orders), payment_df(payments) - but the payment_df contains a column that tells if there was a successful payment
```python
merge_df = pd.merge(order_df, payment_df, on="order_id")
```


EXAMPLE:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Simulated dataset
df = pd.DataFrame({
    'income': [50000, 42000, 60000, 30000],
    'age': [35, 28, 45, 22],
    'loan_amount': [10000, 8000, 12000, 5000],
    'loan_paid_back': [1, 0, 1, 0]  # ← target column
})

# WRONG: Including the target column as a feature!
X = df[['income', 'age', 'loan_amount', 'loan_paid_back']]
y = df['loan_paid_back']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Model accuracy:", model.score(X_test, y_test))
```
Issue: the model will probably say 100% accuracy because it's cheating - it already has the answer in the input data

```python
# CORRECT: Only use independent variables
X = df[['income', 'age', 'loan_amount']]
y = df['loan_paid_back']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Model accuracy:", model.score(X_test, y_test))
```