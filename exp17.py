from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

def load_data():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_decision_tree(X_train, y_train):
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)
    return clf

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=load_iris().target_names)
    return accuracy, report

def main():
    # Load data
    X_train, X_test, y_train, y_test = load_data()

    # Train Decision Tree
    decision_tree_model = train_decision_tree(X_train, y_train)

    # Evaluate model
    accuracy, report = evaluate_model(decision_tree_model, X_test, y_test)

    # Print results
    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)

if __name__ == "__main__":
    main()
