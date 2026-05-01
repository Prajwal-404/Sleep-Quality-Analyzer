import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Page config
st.set_page_config(
    page_title="Sleep Quality Analyzer",
    page_icon="😴",
    layout="wide"
)

# Load model
@st.cache_resource
def load_model():
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        model_path = os.path.join(base_dir, "models", "sleep_model.pkl")
        columns_path = os.path.join(base_dir, "models", "model_columns.pkl")

        model = joblib.load(model_path)
        feature_cols = joblib.load(columns_path)

        return model, feature_cols

    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None
model, feature_cols = load_model()
# Title
st.title("😴 Sleep Quality Analyzer")
st.markdown("### Predict your sleep quality based on lifestyle factors")

if model is None:
    st.error("⚠️ Model not found. Please train the model first by running the notebook.")
    st.stop()

# Sidebar for inputs
st.sidebar.header("Enter Your Information")

# Input fields
age = st.sidebar.slider("Age", 18, 80, 30)
sleep_duration = st.sidebar.slider("Sleep Duration (hours)", 4.0, 12.0, 7.0, 0.5,format="%.1f")
physical_activity = st.sidebar.slider("Physical Activity Level (min/day)", 0, 180, 45, 5)
stress_level = st.sidebar.slider("Stress Level (1-10)", 1, 10, 5, 1)

st.sidebar.markdown("---")
st.sidebar.subheader("Lifestyle Factors")

screen_time = st.sidebar.slider("Screen Time Before Bed (hours)", 0.0, 5.0, 1.0, 0.5,format="%.1f")
caffeine_cups = st.sidebar.slider("Caffeine Cups Per Day",  0, 8, 2, 1)
bedtime_consistency = st.sidebar.slider("Bedtime Consistency (1-7)", 1, 7, 5, 1,
                                        help="1=Very inconsistent, 7=Very consistent")
wakeup_consistency = st.sidebar.slider("Wakeup Consistency (1-7)", 1, 7, 5, 1,
                                       help="1=Very inconsistent, 7=Very consistent")
water_intake = st.sidebar.slider("Water Intake (liters/day)", 0.5, 5.0, 2.0, 0.25)
weekend_sleep_debt = st.sidebar.slider("Weekend Sleep Debt (hours)", 0.0, 5.0, 1.0, 0.5,format="%.1f",
                                       help="Extra sleep needed on weekends")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

# Prepare input data
input_data = pd.DataFrame({
    'Age': [age],
    'Sleep Duration': [sleep_duration],
    'Physical Activity Level': [physical_activity],
    'Stress Level': [stress_level],
    'Screen_Time_Before_Bed': [screen_time],
    'Caffeine_Cups_Per_Day': [caffeine_cups],
    'Bedtime_Consistency': [bedtime_consistency],
    'Wakeup_Consistency': [wakeup_consistency],
    'Water_Intake_Liters': [water_intake],
    'Weekend_Sleep_Debt': [weekend_sleep_debt],
    'Gender_Male': [1 if gender == "Male" else 0]
})

# Ensure column order matches training
input_data = input_data[feature_cols]

# Predict button
if st.sidebar.button("🔮 Predict Sleep Quality", type="primary"):
    prediction = model.predict(input_data)[0]
    
    # Display results
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("---")
        st.markdown("## 📊 Your Sleep Quality Score")
        
        # Score display
        score_color = "green" if prediction >= 7 else "orange" if prediction >= 5 else "red"
        st.markdown(f"<h1 style='text-align: center; color: {score_color};'>{prediction:.1f} / 9</h1>", 
                   unsafe_allow_html=True)
        
        # Interpretation
        if prediction >= 8:
            st.success("🌟 Excellent! Your sleep quality is outstanding.")
            advice = "Keep up your healthy habits!"
        elif prediction >= 7:
            st.success("✅ Good! Your sleep quality is above average.")
            advice = "Minor improvements could make it even better."
        elif prediction >= 6:
            st.warning("⚠️ Fair. Your sleep quality could be improved.")
            advice = "Consider adjusting some lifestyle factors."
        elif prediction >= 5:
            st.warning("⚠️ Below Average. Your sleep needs attention.")
            advice = "Several factors may be affecting your sleep."
        else:
            st.error("❌ Poor. Your sleep quality needs significant improvement.")
            advice = "Consult a healthcare professional if issues persist."
        
        st.info(advice)
        
        st.markdown("---")
        
        # Recommendations
        st.markdown("### 💡 Personalized Recommendations")
        
        recommendations = []
        
        if sleep_duration < 7:
            recommendations.append("⏰ **Increase sleep duration**: Aim for 7-9 hours per night")
        
        if stress_level > 6:
            recommendations.append("🧘 **Manage stress**: Try meditation, yoga, or deep breathing")
        
        if screen_time > 2:
            recommendations.append("📱 **Reduce screen time**: Limit screens 2 hours before bed")
        
        if caffeine_cups > 3:
            recommendations.append("☕ **Reduce caffeine**: Limit to 2-3 cups, avoid after 2 PM")
        
        if bedtime_consistency < 5:
            recommendations.append("🕐 **Consistent bedtime**: Go to bed at the same time daily")
        
        if wakeup_consistency < 5:
            recommendations.append("⏰ **Consistent wake time**: Wake up at the same time daily")
        
        if physical_activity < 30:
            recommendations.append("🏃 **Increase activity**: Aim for 30+ minutes of exercise daily")
        
        if water_intake < 2:
            recommendations.append("💧 **Hydrate more**: Drink 2-3 liters of water daily")
        
        if weekend_sleep_debt > 2:
            recommendations.append("😴 **Reduce sleep debt**: Maintain consistent sleep schedule on weekends")
        
        if recommendations:
            for rec in recommendations:
                st.markdown(f"- {rec}")
        else:
            st.markdown("✨ Your habits look great! Keep maintaining them.")

# Information section
st.markdown("---")
st.markdown("### ℹ️ About This Tool")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **How it works:**
    - Machine learning model trained on sleep health data
    - Analyzes 10+ lifestyle and health factors
    - Provides personalized sleep quality prediction
    - Offers actionable recommendations
    """)

with col2:
    st.markdown("""
    **Important Notes:**
    - This is a predictive tool, not medical advice
    - Consult healthcare professionals for sleep disorders
    - Results based on statistical patterns
    - Individual results may vary
    """)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Sleep Quality Analyzer | ML Mini Project</p>",
    unsafe_allow_html=True
)
