# Importing necessary libraries
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Define a function to train multiple models
def train_models(X_train, y_train):
    models = {}

    # Linear Regression
    linear_reg = LinearRegression()
    linear_reg.fit(X_train, y_train)
    models['Linear Regression'] = linear_reg
    
    # Decision Tree Regressor
    decision_tree = DecisionTreeRegressor(random_state=42)
    decision_tree.fit(X_train, y_train)
    models['Decision Tree'] = decision_tree
    
    # Random Forest Regressor
    random_forest = RandomForestRegressor(n_estimators=100, random_state=42)
    random_forest.fit(X_train, y_train)
    models['Random Forest'] = random_forest
    
    # XGBoost Regressor
    xgboost = XGBRegressor(n_estimators=100, random_state=42)
    xgboost.fit(X_train, y_train)
    models['XGBoost'] = xgboost
    
    return models

# Define a function to evaluate the models
def evaluate_models(models, X_test, y_test):
    evaluation_results = {}
    
    for name, model in models.items():
        y_pred = model.predict(X_test)
        
        # Calculate evaluation metrics
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        
        evaluation_results[name] = {
            'Mean Squared Error': mse,
            'Mean Absolute Error': mae,
            'R-Squared': r2
        }
    
    return evaluation_results


# Feature Importance Analysis for Random Forest, XGBoost, Linear Regression, and Decision Tree
def feature_importance_analysis(models, X_train, feature_names):
    for model_name in ['Random Forest', 'XGBoost', 'Linear Regression', 'Decision Tree']:
        model = models.get(model_name)
        
        if model_name in ['Random Forest', 'XGBoost'] and hasattr(model, 'feature_importances_'):
            importances = model.feature_importances_
        elif model_name == 'Linear Regression':
            importances = np.abs(model.coef_)  # Use absolute value of coefficients for feature importance
        elif model_name == 'Decision Tree' and hasattr(model, 'feature_importances_'):
            importances = model.feature_importances_
        else:
            continue  # Skip if the model does not have feature importances
        
        # Sort the feature importances in descending order
        sorted_idx = importances.argsort()[::-1]

        # Plot the feature importances as a vertical bar chart
        plt.bar([feature_names[i] for i in sorted_idx], importances[sorted_idx])
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.ylabel('Feature Importance')
        plt.title(f'{model_name} Feature Importance')
        plt.tight_layout()  # Adjust the layout to prevent clipping of labels
        plt.show()


# SHAP Analysis
# def shap_analysis(models, X_train):
#     explainer = shap.Explainer(models['Random Forest'], X_train)
#     shap_values = explainer(X_train)
    
#     # Summary plot
#     shap.summary_plot(shap_values, X_train)

#     # Force plot for individual prediction
#     shap.force_plot(explainer.expected_value, shap_values[0,:], X_train[0,:], matplotlib=True)

# Report comparison between model performance
def report_comparison(evaluation_results):
    report = pd.DataFrame(evaluation_results).T
    print("\nModel Performance Comparison:")
    print(report)
