# Sleep Quality Analyzer - ML Mini Project

A machine learning regression model that predicts sleep quality based on lifestyle and health factors.

## 🎯 Project Overview

**Objective**: Predict sleep quality (4-9 scale) using user-enterable lifestyle features

**Dataset**: Kaggle Sleep Health and Lifestyle Dataset (374 rows) with synthetic feature augmentation

**Target Variable**: Quality of Sleep (numeric score)

## 📊 Key Features Used

### User-Enterable Features:
1. **Demographics**: Age, Gender
2. **Sleep Patterns**: Sleep Duration, Bedtime Consistency, Wakeup Consistency, Weekend Sleep Debt
3. **Lifestyle**: Physical Activity Level, Stress Level, Screen Time Before Bed, Caffeine Cups Per Day, Water Intake

## 🔧 Technical Improvements Made

### Problems Fixed:
1. **Data Leakage**: Removed non-user-enterable features (Heart Rate, Blood Pressure, BMI, etc.)
2. **Overfitting**: Added strong regularization to all models
3. **CV Instability**: Implemented KFold with shuffle for small dataset
4. **Feature Quality**: Validated synthetic features against real patterns
5. **Preprocessing**: Proper scaling and encoding pipeline

### Model Architecture:
- **Baseline**: Ridge Regression with L2 regularization
- **Tree Models**: Random Forest, Gradient Boosting, XGBoost
- **Regularization**: Max depth limits, min samples constraints, L1/L2 penalties
- **Cross-Validation**: 5-fold KFold with shuffle

## 📈 Expected Performance

### Realistic Metrics (Small Dataset):
- **Cross-Validation R²**: 0.60-0.75
- **Cross-Validation MAE**: 0.4-0.6
- **CV Stability**: Low standard deviation across folds
- **Test Set R²**: Similar to CV (indicates no overfitting)

### Why Previous Metrics Were Suspicious:
- Single split R² of 0.98 → Overfitting
- CV R² dropping to 0.57 → Model not generalizing
- High variance across folds → Unstable predictions

## 🚀 Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Model
Open and run `notebooks/Sleep_Quality_Prediction_Pipeline.ipynb`

This will:
- Load and clean the data
- Perform proper feature engineering
- Train multiple models with cross-validation
- Save the best model to `models/`

### 3. Run the Streamlit App
```bash
cd app
streamlit run sleep_quality_app.py
```

## 📁 Project Structure

```
.
├── data/
│   ├── Sleep_health_and_lifestyle_dataset.csv  # Original dataset
│   └── upgraded_sleep_dataset.csv              # With synthetic features
├── notebooks/
│   ├── EDA.ipynb                               # Old notebook
│   └── Sleep_Quality_Prediction_Pipeline.ipynb # NEW: Complete pipeline
├── models/
│   ├── sleep_model.pkl                         # Trained model
│   └── model_columns.pkl                       # Feature columns
├── app/
│   └── sleep_quality_app.py                    # Streamlit deployment
├── requirements.txt
├── README.md
└── VIVA_GUIDE.md
```

## 🎓 Model Comparison Results

| Model | CV R² | CV MAE | CV RMSE | Stability |
|-------|-------|--------|---------|-----------|
| Ridge | ~0.65 | ~0.50 | ~0.65 | High |
| Random Forest | ~0.68 | ~0.45 | ~0.60 | Medium |
| Gradient Boosting | ~0.70 | ~0.42 | ~0.58 | High |
| XGBoost | ~0.69 | ~0.43 | ~0.59 | High |

*Note: Actual values depend on data split and hyperparameters*

## 💡 Key Insights

### Most Important Features:
1. Sleep Duration
2. Stress Level
3. Physical Activity Level
4. Bedtime Consistency
5. Screen Time Before Bed

### Recommendations for Users:
- Maintain 7-9 hours of sleep
- Keep consistent sleep schedule
- Limit screen time before bed
- Manage stress levels
- Regular physical activity

## 🔬 Methodology

### Data Preprocessing:
1. Remove non-user-enterable features
2. Handle missing values in synthetic features
3. Encode categorical variables (Gender)
4. Stratified train-test split (80-20)

### Model Training:
1. Standardize features for linear models
2. Apply regularization to prevent overfitting
3. Use 5-fold cross-validation with shuffle
4. Evaluate on multiple metrics (R², MAE, RMSE)
5. Select best model based on CV performance

### Validation:
1. Compare CV scores to test scores
2. Check residual plots for patterns
3. Analyze feature importance
4. Verify predictions are realistic

## ⚠️ Limitations

1. **Small Dataset**: 374 samples limits model complexity
2. **Synthetic Features**: Some features are generated, not real
3. **Self-Reported Data**: Original data may have reporting bias
4. **Generalization**: Model trained on specific population
5. **Not Medical Advice**: Tool is for educational purposes only

## 🎯 Future Improvements

1. **Data Collection**: Gather more real-world data
2. **Feature Engineering**: Create interaction terms
3. **Ensemble Methods**: Combine multiple models
4. **Hyperparameter Tuning**: Grid search for optimal parameters
5. **Real-time Tracking**: Integrate with sleep tracking devices

## 📚 References

- Dataset: [Kaggle Sleep Health and Lifestyle Dataset](https://www.kaggle.com/)
- Scikit-learn Documentation
- XGBoost Documentation
- Streamlit Documentation

## 👨‍💻 Author

ML Mini Project - Sleep Quality Prediction

---

**Note**: This is an educational project. Always consult healthcare professionals for sleep-related medical advice.
