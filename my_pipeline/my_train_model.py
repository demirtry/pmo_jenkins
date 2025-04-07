import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import mlflow
from mlflow.models import infer_signature
import mlflow.sklearn
import joblib


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if __name__ == "__main__":
    df = pd.read_csv("./student_performance_clear.csv")
    X, Y = df.drop(columns=['Pass_Fail']), df['Pass_Fail']
    X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                        test_size=0.3,
                                                        random_state=42)

    param_grid = {
        'C': [0.01, 0.1, 1, 10],
        'penalty': ['l1', 'l2'],
        'solver': ['liblinear', 'saga'],
        'max_iter': [100, 200, 300]
    }

    mlflow.set_experiment("my experiment")

    with mlflow.start_run():
        lr = LogisticRegression(max_iter=10000)
        grid_search = GridSearchCV(lr, param_grid, cv=3, n_jobs=4)
        grid_search.fit(X_train, y_train)

        best_params = grid_search.best_params_

        for param, value in best_params.items():
            mlflow.log_param(param, value)

        best_model = grid_search.best_estimator_
        y_pred = best_model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='weighted')

        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("f1_score", f1)

        report = classification_report(y_test, y_pred, output_dict=True)
        for label, metrics in report.items():
            if label != 'accuracy':
                for metric, value in metrics.items():
                    mlflow.log_metric(f"{label}_{metric}", value)

        signature = infer_signature(X_train, y_pred)
        mlflow.sklearn.log_model(best_model, "my_model", signature=signature)

        with open("lr_students.pkl", "wb") as file:
            joblib.dump(best_model, file)

        dfruns = mlflow.search_runs()
        path2model = dfruns.sort_values("metrics.f1_score", ascending=False).iloc[0]['artifact_uri'].replace("file://", "") + '/my_model'
        print(path2model)
