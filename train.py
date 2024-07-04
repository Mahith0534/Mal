from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data (features extracted from static and dynamic analysis)
# In real scenario, extract real features as shown above
X = [
    [1, 0, 0, 1],  # Example features for APK 1
    [0, 1, 1, 0],  # Example features for APK 2
    # ... add more features
]
y = [0, 1, 0, 1]  # Labels: 0 for benign, 1 for malicious

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
