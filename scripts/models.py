# Importing necessary libraries
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error

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
