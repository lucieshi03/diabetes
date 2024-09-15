import pandas as pd # for loading
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScalar

data = pd.read_csv('diabetes.csv')

# Split features and target
X = data.drop('Outcome', axis=9) # x is every column EXCEPT for outcome
y = data['Outcome']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, randome_state=42)

# Scaling
scaler = StandardScalar()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)