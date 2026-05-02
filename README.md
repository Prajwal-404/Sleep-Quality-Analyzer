# Sleep Quality Analyzer

AI-powered machine learning application that predicts sleep quality from lifestyle and wellness factors.

## Overview

Sleep Quality Analyzer uses machine learning to predict sleep quality scores based on user-provided lifestyle habits. The application provides personalized recommendations to help users improve their sleep patterns through data-driven insights.

**Key Capabilities:**
- Predicts sleep quality on a 4-9 scale
- Analyzes 11 lifestyle and wellness factors
- Generates personalized improvement recommendations
- Real-time predictions through interactive web interface

## Features

- **Sleep Quality Prediction** - ML-powered regression model trained on real sleep health data
- **Lifestyle Analysis** - Evaluates sleep duration, stress, physical activity, screen time, caffeine intake, and more
- **Personalized Recommendations** - Actionable insights based on individual lifestyle patterns
- **Interactive Web UI** - Premium dark-themed Streamlit interface with real-time predictions
- **Instant Inference** - Pre-trained model provides immediate results

## Tech Stack

**Core:**
- Python 3.8+
- Streamlit
- Scikit-learn
- XGBoost
- Pandas & NumPy

**ML Pipeline:**
- Jupyter Notebook
- Matplotlib & Seaborn
- Joblib

## Project Structure

```
Sleep-Quality-Analyzer/
├── app/
│   ├── sleep_quality_app.py          # Streamlit web application
│   └── STREAMLIT_UI_GUIDE.md         # UI documentation
├── models/
│   ├── sleep_model.pkl                # Trained ML model
│   └── model_columns.pkl              # Feature columns & preprocessing
├── notebooks/
│   ├── Sleep_Quality_Prediction_Pipeline.ipynb  # Model training pipeline
│   └── EDA.ipynb                      # Exploratory data analysis
├── data/
│   ├── Sleep_health_and_lifestyle_dataset.csv   # Original dataset
│   └── upgraded_sleep_dataset.csv     # Processed dataset with features
├── requirements.txt                   # Python dependencies
└── README.md
```

## How It Works

1. **User Input** - User provides lifestyle data through interactive sliders and dropdowns
2. **Data Processing** - Input is formatted and aligned with model's expected features
3. **Prediction** - Trained Gradient Boosting model predicts sleep quality score
4. **Results Display** - App shows score, status badge, wellness insights, and recommendations
5. **Personalized Advice** - Dynamic recommendations generated based on user's specific patterns

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Sleep-Quality-Analyzer.git
cd Sleep-Quality-Analyzer

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
# Run Streamlit app
streamlit run app/sleep_quality_app.py
```

The application will automatically open in your default browser at `http://localhost:8501`

### Training the Model

To retrain the model with new data:

```bash
# Open Jupyter Notebook
jupyter notebook

# Navigate to notebooks/Sleep_Quality_Prediction_Pipeline.ipynb
# Run all cells to train and save the model
```

## Model Details

**Algorithm:** Gradient Boosting Regressor

**Input Features (11):**
- Age
- Gender
- Sleep Duration (hours)
- Physical Activity Level (minutes/day)
- Stress Level (1-10 scale)
- Screen Time Before Bed (hours)
- Caffeine Intake (cups/day)
- Bedtime Consistency (1-7 scale)
- Wakeup Consistency (1-7 scale)
- Water Intake (liters/day)
- Weekend Sleep Debt (hours)

**Output:** Sleep Quality Score (4-9 scale)

**Performance Metrics:**
- Cross-Validation R²: ~0.70
- Mean Absolute Error: ~0.42
- 5-Fold Cross-Validation with stratified splits

**Model Files:**
- `sleep_model.pkl` - Serialized trained model
- `model_columns.pkl` - Feature order and preprocessing metadata

## Usage Example

1. Launch the application
2. Fill in your lifestyle information in the sidebar:
   - Personal details (age, gender)
   - Sleep habits (duration, consistency)
   - Lifestyle factors (activity, stress, screen time)
3. Click "Analyze Sleep Quality"
4. View your predicted sleep score and personalized recommendations

## Screenshots

*Coming soon - Screenshots of the application interface*

## Dataset

**Source:** Kaggle Sleep Health and Lifestyle Dataset

**Size:** 374 samples with 11 user-enterable features

**Preprocessing:**
- Removed non-user-enterable features (Heart Rate, Blood Pressure, BMI)
- Added synthetic lifestyle features for enhanced prediction
- Applied proper encoding for categorical variables

## Future Enhancements

- Deploy to cloud platform (Streamlit Cloud, Heroku, AWS)
- Add user authentication and profile management
- Implement sleep trend tracking over time
- Integrate with wearable device APIs
- Add advanced analytics dashboard
- Multi-language support

## License

This project is available for educational and portfolio purposes.

## Author

ML Mini Project - Sleep Quality Prediction

---

**Note:** This application is for educational purposes only and should not replace professional medical advice.
