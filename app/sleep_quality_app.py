import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from pathlib import Path

# ===================================
# PAGE CONFIGURATION
# ===================================
st.set_page_config(
    page_title="Sleep Quality Analyzer | AI-Powered Insights",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================================
# CUSTOM CSS - PREMIUM DESIGN
# ===================================
def load_custom_css():
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hero Section */
    .hero-container {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 1px solid rgba(102, 126, 234, 0.3);
        border-radius: 24px;
        padding: 3rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .hero-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: #cbd5e1;
        margin-bottom: 1.5rem;
    }
    
    .hero-badges {
        display: flex;
        gap: 1rem;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1.5rem;
        background: rgba(102, 126, 234, 0.1);
        border: 1px solid rgba(102, 126, 234, 0.3);
        border-radius: 50px;
        font-size: 0.875rem;
        font-weight: 500;
        color: #cbd5e1;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
        border-right: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {
        color: #ffffff;
    }
    
    /* Section Headers */
    .section-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        font-size: 1.25rem;
        font-weight: 700;
        color: #ffffff;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid rgba(102, 126, 234, 0.3);
    }
    
    .section-icon {
        font-size: 1.5rem;
    }
    
    /* Input Labels */
    .stSlider label, .stSelectbox label, .stNumberInput label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Sliders */
    .stSlider [data-baseweb="slider"] {
        background: linear-gradient(to right, #667eea, #764ba2);
    }
    
    /* Select Boxes */
    .stSelectbox [data-baseweb="select"] {
        background: rgba(15, 23, 42, 0.5);
        border: 1px solid rgba(102, 126, 234, 0.3);
        border-radius: 12px;
    }
    
    /* Buttons */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 700;
        font-size: 1.125rem;
        padding: 1rem 2rem;
        border: none;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
    }
    
    /* Metric Cards */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 800;
        color: #667eea;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.875rem;
        font-weight: 600;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Score Card */
    .score-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 1px solid rgba(102, 126, 234, 0.3);
        border-radius: 24px;
        padding: 2rem;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    
    .score-value {
        font-size: 5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1;
        margin-bottom: 0.5rem;
    }
    
    .score-label {
        font-size: 1rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 1rem;
    }
    
    .score-description {
        font-size: 1.125rem;
        color: #cbd5e1;
        line-height: 1.6;
    }
    
    /* Status Badge */
    .status-badge {
        display: inline-block;
        padding: 0.5rem 1.5rem;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin: 1rem 0;
    }
    
    .status-excellent {
        background: rgba(16, 185, 129, 0.2);
        color: #10b981;
        border: 1px solid #10b981;
    }
    
    .status-good {
        background: rgba(6, 182, 212, 0.2);
        color: #06b6d4;
        border: 1px solid #06b6d4;
    }
    
    .status-moderate {
        background: rgba(245, 158, 11, 0.2);
        color: #f59e0b;
        border: 1px solid #f59e0b;
    }
    
    .status-poor {
        background: rgba(239, 68, 68, 0.2);
        color: #ef4444;
        border: 1px solid #ef4444;
    }
    
    /* Insight Cards */
    .insight-card {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .insight-card:hover {
        border-color: rgba(102, 126, 234, 0.4);
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
    }
    
    .insight-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    
    .insight-label {
        font-size: 0.875rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }
    
    .insight-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
    }
    
    /* Recommendation Cards */
    .recommendation-card {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .recommendation-card:hover {
        border-color: rgba(102, 126, 234, 0.4);
        transform: translateX(5px);
    }
    
    .recommendation-header {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 0.75rem;
    }
    
    .recommendation-icon {
        font-size: 1.5rem;
    }
    
    .recommendation-title {
        font-size: 1rem;
        font-weight: 600;
        color: #ffffff;
    }
    
    .recommendation-text {
        font-size: 0.875rem;
        color: #cbd5e1;
        line-height: 1.6;
        margin-left: 2.5rem;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background: linear-gradient(to right, #667eea, #764ba2);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 12px;
        color: #ffffff;
        font-weight: 600;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 4rem;
        border-top: 1px solid rgba(102, 126, 234, 0.2);
        color: #94a3b8;
        font-size: 0.875rem;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, rgba(102, 126, 234, 0.3), transparent);
        margin: 2rem 0;
    }
    
    /* Info Box */
    .stAlert {
        background: rgba(6, 182, 212, 0.1);
        border: 1px solid rgba(6, 182, 212, 0.3);
        border-radius: 12px;
        color: #cbd5e1;
    }
    
    /* Success Box */
    .stSuccess {
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 12px;
        color: #cbd5e1;
    }
    
    /* Warning Box */
    .stWarning {
        background: rgba(245, 158, 11, 0.1);
        border: 1px solid rgba(245, 158, 11, 0.3);
        border-radius: 12px;
        color: #cbd5e1;
    }
    
    /* Error Box */
    .stError {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 12px;
        color: #cbd5e1;
    }
    </style>
    """, unsafe_allow_html=True)

# ===================================
# LOAD MODEL
# ===================================
@st.cache_resource
def load_model():
    try:
        model_path = Path(__file__).parent.parent / 'models' / 'sleep_model.pkl'
        feature_path = Path(__file__).parent.parent / 'models' / 'model_columns.pkl'
        
        model = joblib.load(model_path)
        feature_cols = joblib.load(feature_path)
        return model, feature_cols
    except Exception as e:
        st.error(f"⚠️ Model not found. Please train the model first by running the notebook.")
        return None, None

# ===================================
# HELPER FUNCTIONS
# ===================================
def get_status_info(score):
    """Get status badge and description based on score"""
    if score >= 8:
        return "excellent", "Excellent", "🌟 Outstanding! Your sleep quality is exceptional. Keep up your healthy habits!"
    elif score >= 7:
        return "good", "Good", "✅ Great! Your sleep quality is above average. Minor improvements could make it even better."
    elif score >= 6:
        return "moderate", "Moderate", "⚠️ Fair. Your sleep quality could be improved. Consider adjusting some lifestyle factors."
    elif score >= 5:
        return "moderate", "Below Average", "⚠️ Your sleep needs attention. Several factors may be affecting your sleep quality."
    else:
        return "poor", "Poor", "❌ Your sleep quality needs significant improvement. Consider consulting a healthcare professional."

def calculate_insights(score, data):
    """Calculate wellness insights"""
    avg_consistency = (data['Bedtime_Consistency'] + data['Wakeup_Consistency']) / 2
    
    return {
        'wellness_level': 'High' if score >= 7 else 'Medium' if score >= 6 else 'Low',
        'risk_level': 'Low' if score >= 7 else 'Medium' if score >= 6 else 'High',
        'recovery_score': f"{int((score / 9) * 100)}%",
        'habit_consistency': 'Excellent' if avg_consistency >= 6 else 'Good' if avg_consistency >= 5 else 'Fair' if avg_consistency >= 4 else 'Poor'
    }

def generate_recommendations(data, score):
    """Generate personalized recommendations"""
    recommendations = []
    
    if data['Sleep Duration'] < 7:
        recommendations.append({
            'icon': '⏰',
            'title': 'Increase Sleep Duration',
            'text': 'Aim for 7-9 hours of sleep per night. Your current sleep duration may be insufficient for optimal recovery.'
        })
    
    if data['Stress Level'] > 6:
        recommendations.append({
            'icon': '🧘',
            'title': 'Manage Stress Levels',
            'text': 'Try meditation, yoga, or deep breathing exercises. High stress significantly impacts sleep quality.'
        })
    
    if data['Screen_Time_Before_Bed'] > 2:
        recommendations.append({
            'icon': '📱',
            'title': 'Reduce Screen Time',
            'text': 'Limit screen exposure 2 hours before bed. Blue light can disrupt your natural sleep cycle.'
        })
    
    if data['Caffeine_Cups_Per_Day'] > 3:
        recommendations.append({
            'icon': '☕',
            'title': 'Reduce Caffeine Intake',
            'text': 'Limit caffeine to 2-3 cups per day and avoid consumption after 2 PM for better sleep.'
        })
    
    if data['Bedtime_Consistency'] < 5:
        recommendations.append({
            'icon': '🕐',
            'title': 'Maintain Consistent Bedtime',
            'text': 'Go to bed at the same time every day. Consistency helps regulate your circadian rhythm.'
        })
    
    if data['Wakeup_Consistency'] < 5:
        recommendations.append({
            'icon': '⏰',
            'title': 'Consistent Wake Time',
            'text': 'Wake up at the same time daily, even on weekends. This strengthens your sleep-wake cycle.'
        })
    
    if data['Physical Activity Level'] < 30:
        recommendations.append({
            'icon': '🏃',
            'title': 'Increase Physical Activity',
            'text': 'Aim for at least 30 minutes of exercise daily. Regular activity promotes better sleep quality.'
        })
    
    if data['Water_Intake_Liters'] < 2:
        recommendations.append({
            'icon': '💧',
            'title': 'Stay Hydrated',
            'text': 'Drink 2-3 liters of water daily. Proper hydration supports overall health and sleep quality.'
        })
    
    if data['Weekend_Sleep_Debt'] > 2:
        recommendations.append({
            'icon': '😴',
            'title': 'Reduce Sleep Debt',
            'text': 'Maintain a consistent sleep schedule on weekends. Large variations indicate insufficient weekday sleep.'
        })
    
    if not recommendations:
        recommendations.append({
            'icon': '✨',
            'title': 'Excellent Habits!',
            'text': 'Your sleep habits look great! Continue maintaining your healthy lifestyle for optimal sleep quality.'
        })
    
    return recommendations

# ===================================
# MAIN APP
# ===================================
def main():
    # Load custom CSS
    load_custom_css()
    
    # Load model
    model, feature_cols = load_model()
    
    # Hero Section
    st.markdown("""
    <div class="hero-container">
        <div class="hero-icon">🌙</div>
        <h1 class="hero-title">Sleep Quality Analyzer</h1>
        <p class="hero-subtitle">Predict your sleep quality using AI-powered lifestyle analysis</p>
        <div class="hero-badges">
            <span class="badge">🧠 AI-Powered</span>
            <span class="badge">📊 Data-Driven</span>
            <span class="badge">🎯 Personalized</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar - Input Form
    with st.sidebar:
        st.markdown("## 📋 Your Lifestyle Profile")
        st.markdown("Tell us about your daily habits and routines")
        st.markdown("---")
        
        # Personal Information
        st.markdown('<div class="section-header"><span class="section-icon">👤</span> Personal Information</div>', unsafe_allow_html=True)
        age = st.slider("Age", 18, 80, 30, help="Your current age")
        gender = st.selectbox("Gender", ["Male", "Female"])
        
        st.markdown("---")
        
        # Sleep Habits
        st.markdown('<div class="section-header"><span class="section-icon">🌙</span> Sleep Habits</div>', unsafe_allow_html=True)
        sleep_duration = st.slider("Sleep Duration (hours)", 4.0, 12.0, 7.0, 0.1, help="Average hours of sleep per night")
        bedtime_consistency = st.slider("Bedtime Consistency", 1, 7, 5, help="1 = Very inconsistent, 7 = Very consistent")
        wakeup_consistency = st.slider("Wakeup Consistency", 1, 7, 5, help="1 = Very inconsistent, 7 = Very consistent")
        weekend_sleep_debt = st.slider("Weekend Sleep Debt (hours)", 0.0, 5.0, 1.0, 0.1, help="Extra sleep needed on weekends")
        
        st.markdown("---")
        
        # Lifestyle Factors
        st.markdown('<div class="section-header"><span class="section-icon">💪</span> Lifestyle Factors</div>', unsafe_allow_html=True)
        physical_activity = st.slider("Physical Activity (min/day)", 0, 120, 60, help="Minutes of exercise per day")
        stress_level = st.slider("Stress Level", 1, 10, 5, help="1 = Very low, 10 = Very high")
        screen_time = st.slider("Screen Time Before Bed (hours)", 0.0, 5.0, 1.0, 0.1, help="Hours of screen time before sleep")
        caffeine = st.slider("Caffeine Cups Per Day", 0, 10, 2, help="Number of caffeinated drinks")
        water_intake = st.slider("Water Intake (liters/day)", 0.0, 5.0, 2.0, 0.1, help="Daily water consumption")
        
        st.markdown("---")
        
        # Predict Button
        predict_button = st.button("✨ Analyze Sleep Quality", use_container_width=True)
    
    # Main Content Area
    if model is None:
        st.error("⚠️ Model not loaded. Please train the model first.")
        return
    
    if predict_button:
        # Prepare input data
        input_data = pd.DataFrame({
            'Age': [age],
            'Sleep Duration': [sleep_duration],
            'Physical Activity Level': [physical_activity],
            'Stress Level': [stress_level],
            'Screen_Time_Before_Bed': [screen_time],
            'Caffeine_Cups_Per_Day': [caffeine],
            'Bedtime_Consistency': [bedtime_consistency],
            'Wakeup_Consistency': [wakeup_consistency],
            'Water_Intake_Liters': [water_intake],
            'Weekend_Sleep_Debt': [weekend_sleep_debt],
            'Gender_Male': [1 if gender == "Male" else 0]
        })
        
        # Ensure column order matches training
        input_data = input_data[feature_cols]
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        score = round(prediction, 1)
        
        # Get status info
        status_class, status_text, description = get_status_info(score)
        
        # Calculate insights
        data_dict = {
            'Sleep Duration': sleep_duration,
            'Stress Level': stress_level,
            'Physical Activity Level': physical_activity,
            'Screen_Time_Before_Bed': screen_time,
            'Caffeine_Cups_Per_Day': caffeine,
            'Bedtime_Consistency': bedtime_consistency,
            'Wakeup_Consistency': wakeup_consistency,
            'Water_Intake_Liters': water_intake,
            'Weekend_Sleep_Debt': weekend_sleep_debt
        }
        insights = calculate_insights(score, data_dict)
        
        # Generate recommendations
        recommendations = generate_recommendations(data_dict, score)
        
        # Display Results
        st.markdown("## 📊 Your Sleep Quality Analysis")
        st.markdown("AI-powered insights based on your lifestyle profile")
        st.markdown("---")
        
        # Score Card
        st.markdown(f"""
        <div class="score-card">
            <div class="score-value">{score}</div>
            <div class="score-label">Sleep Quality Score</div>
            <div class="status-badge status-{status_class}">{status_text}</div>
            <div class="score-description">{description}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Progress Bar
        st.progress(score / 9)
        
        st.markdown("---")
        
        # Insights Grid
        st.markdown("### 💡 Key Insights")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="insight-card">
                <div class="insight-icon">💚</div>
                <div class="insight-label">Wellness Level</div>
                <div class="insight-value">{insights['wellness_level']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="insight-card">
                <div class="insight-icon">⚠️</div>
                <div class="insight-label">Risk Level</div>
                <div class="insight-value">{insights['risk_level']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="insight-card">
                <div class="insight-icon">🔄</div>
                <div class="insight-label">Recovery Score</div>
                <div class="insight-value">{insights['recovery_score']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="insight-card">
                <div class="insight-icon">📈</div>
                <div class="insight-label">Habit Consistency</div>
                <div class="insight-value">{insights['habit_consistency']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Recommendations
        st.markdown("### 💡 Personalized Recommendations")
        st.markdown("Actionable insights to improve your sleep quality")
        
        for rec in recommendations:
            st.markdown(f"""
            <div class="recommendation-card">
                <div class="recommendation-header">
                    <span class="recommendation-icon">{rec['icon']}</span>
                    <span class="recommendation-title">{rec['title']}</span>
                </div>
                <div class="recommendation-text">{rec['text']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Additional Info
        with st.expander("📖 Understanding Your Results"):
            st.markdown("""
            **Sleep Quality Score (4-9 scale):**
            - **8-9**: Excellent - Outstanding sleep quality
            - **7-8**: Good - Above average sleep quality
            - **6-7**: Moderate - Room for improvement
            - **5-6**: Below Average - Needs attention
            - **4-5**: Poor - Significant improvement needed
            
            **Key Factors Affecting Sleep:**
            - Sleep duration and consistency
            - Stress levels and management
            - Physical activity and exercise
            - Screen time before bed
            - Caffeine and hydration
            - Weekend sleep patterns
            """)
    
    else:
        # Welcome Screen
        st.markdown("## 👋 Welcome!")
        st.info("👈 **Get Started:** Fill in your lifestyle information in the sidebar and click 'Analyze Sleep Quality' to receive your personalized sleep quality assessment.")
        
        st.markdown("---")
        
        st.markdown("### 🎯 What You'll Get")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📊 Comprehensive Analysis**
            - AI-powered sleep quality prediction
            - Personalized wellness insights
            - Risk assessment
            - Recovery score calculation
            """)
            
            st.markdown("""
            **💡 Actionable Recommendations**
            - Customized improvement tips
            - Evidence-based suggestions
            - Lifestyle optimization advice
            - Habit tracking guidance
            """)
        
        with col2:
            st.markdown("""
            **🔬 Science-Backed**
            - Machine learning model
            - Trained on real sleep data
            - Validated predictions
            - Continuous improvements
            """)
            
            st.markdown("""
            **🎯 Easy to Use**
            - Simple input sliders
            - Instant results
            - Clear visualizations
            - Mobile-friendly interface
            """)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p><strong>Sleep Quality Analyzer</strong> | AI-Powered Sleep Insights</p>
        <p>This tool is for educational purposes only. Consult healthcare professionals for medical advice.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
