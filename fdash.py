import streamlit as st
import base64
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Malware Detection System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sample data for different models
model_data = {
    "Random Forest": {
        "accuracy": 0.9669,
        "precision": 0.9630,
        "recall": 0.9669,
        "F1 Score": 0.9630,
        "color": "#00ff00"  # Green
    },
    "Naive Bayes": {
        "accuracy": 0.9421,
        "precision": 0.9443,
        "recall": 0.9421,
        "F1 Score": 0.9421,
        "color": "#ff0000"  # Red
    },
    "SVM": {
        "accuracy": 0.9752,
        "precision": 0.9797,
        "recall": 0.9786,
        "F1 Score": 0.9786,
        "color": "#0000ff"  # Blue
    },
    "Logistic Regression": {
        "accuracy": 0.9339,
        "precision": 0.9288,
        "recall": 0.9339,
        "F1 Score": 0.9303,
        "color": "#800080"  # Purple
    }
}

# Function to encode a local GIF as Base64
def get_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Custom CSS styling with animated gradient background
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #05001A, #140032, #05001A, #140032, #05001A);
        background-size: 400% 400%;
        animation: gradientAnimation 15s ease infinite;
    }

    @keyframes gradientAnimation {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }

    /* Enhanced Title with Glowing Effect */
    .title-text {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.8rem;
        color: #00d4ff;
        text-align: center;
        text-transform: uppercase;
        position: relative;
        z-index: 3;
        margin-bottom: 2rem;
        text-shadow: 
            0 0 10px rgba(0, 212, 255, 0.8),
            0 0 20px rgba(0, 212, 255, 0.4),
            0 0 30px rgba(0, 212, 255, 0.2);
        animation: titleGlow 3s ease-in-out infinite alternate;
    }

    @keyframes titleGlow {
        0% {
            text-shadow: 
                0 0 10px rgba(0, 212, 255, 0.8),
                0 0 20px rgba(0, 212, 255, 0.4),
                0 0 30px rgba(0, 212, 255, 0.2);
        }
        100% {
            text-shadow: 
                0 0 15px rgba(0, 212, 255, 0.9),
                0 0 25px rgba(0, 212, 255, 0.5),
                0 0 35px rgba(0, 212, 255, 0.3),
                0 0 45px rgba(0, 212, 255, 0.2);
        }
    }

    /* Enhanced Sidebar Styling */
    .css-1d391kg {
        background: rgba(5, 0, 20, 0.9);
        backdrop-filter: blur(10px);
    }

    /* Custom button styling */
    .stButton > button {
        background-color: rgba(0, 212, 255, 0.1) !important;
        color: #00d4ff !important;
        border: 2px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 10px !important;
        padding: 15px 25px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 1.1rem !important;
        margin: 10px 0 !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        background-color: rgba(0, 212, 255, 0.2) !important;
        border-color: rgba(0, 212, 255, 0.8) !important;
        transform: translateX(5px);
    }

    /* Sidebar title styling */
    .sidebar-title {
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 2rem;
        border-bottom: 2px solid rgba(0, 212, 255, 0.3);
    }

    .sidebar-title h1 {
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem;
        color: #00d4ff;
        text-transform: uppercase;
        margin: 0;
        letter-spacing: 2px;
    }

    /* Model metrics card styling */
    .metrics-card {
        background-color: rgba(0,0,0,0.5);
        padding: 20px;
        border-radius: 10px;
        border: 2px solid rgba(0,212,255,0.3);
        margin-top: 20px;
    }

    .metrics-card h3 {
        color: #00d4ff;
        font-family: 'Orbitron', sans-serif;
        margin-bottom: 15px;
    }

    .metrics-card p {
        color: #00d4ff;
        margin-bottom: 10px;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""

# Function to create a bar chart for model metrics
def create_bar_chart(selected_model):
    metrics = ["Accuracy", "Precision", "Recall", "F1 Score"]
    values = [
        model_data[selected_model]["accuracy"],
        model_data[selected_model]["precision"],
        model_data[selected_model]["recall"],
        model_data[selected_model]["F1 Score"]
    ]
    
    fig = go.Figure(data=[go.Bar(
        x=metrics,
        y=values,
        marker_color=model_data[selected_model]["color"],
        text=values,
        textposition='auto'
    )])
    
    fig.update_layout(
        title={
            'text': f"{selected_model} Performance Metrics",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#00d4ff')
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#00d4ff'),
        xaxis=dict(title="Metrics", gridcolor='rgba(0,212,255,0.1)'),
        yaxis=dict(title="Score", gridcolor='rgba(0,212,255,0.1)', range=[0, 1]),
        hovermode='x unified'
    )
    
    return fig

# Function to create a grouped bar chart for comparing models
def create_grouped_bar_chart(selected_models):
    metrics = ["Accuracy", "Precision", "Recall", "F1 Score"]
    data = []
    
    for model in selected_models:
        data.append(go.Bar(
            name=model,
            x=metrics,
            y=[
                model_data[model]["accuracy"],
                model_data[model]["precision"],
                model_data[model]["recall"],
                model_data[model]["F1 Score"]
            ],
            marker_color=model_data[model]["color"]
        ))
    
    fig = go.Figure(data=data)
    
    fig.update_layout(
        title={
            'text': "Model Performance Comparison",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#00d4ff')
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#00d4ff'),
        xaxis=dict(title="Metrics", gridcolor='rgba(0,212,255,0.1)'),
        yaxis=dict(title="Score", gridcolor='rgba(0,212,255,0.1)', range=[0, 1]),
        barmode='group',
        hovermode='x unified'
    )
    
    return fig

# Dashboard Page
def dashboard_page():
    st.markdown("### Best Performing Model")
    st.markdown("Here are the results for the model with the highest accuracy:")

    # Find the best performing model (based on accuracy)
    best_model = max(model_data.keys(), key=lambda x: model_data[x]["accuracy"])
    best_model_metrics = model_data[best_model]

    # Display metrics in a card-like layout
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-card" style="
            background: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 10px;
            border: 2px solid {best_model_metrics['color']};
            text-align: center;
        ">
            <h3 style="color: {best_model_metrics['color']}; margin-bottom: 10px; font-family: 'Orbitron', sans-serif;">Accuracy</h3>
            <p style="font-size: 1.5rem; color: {best_model_metrics['color']}; font-weight: bold; font-family: 'Orbitron', sans-serif;">
                {best_model_metrics['accuracy']:.2%}
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card" style="
            background: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 10px;
            border: 2px solid {best_model_metrics['color']};
            text-align: center;
        ">
            <h3 style="color: {best_model_metrics['color']}; margin-bottom: 10px; font-family: 'Orbitron', sans-serif;">Precision</h3>
            <p style="font-size: 1.5rem; color: {best_model_metrics['color']}; font-weight: bold; font-family: 'Orbitron', sans-serif;">
                {best_model_metrics['precision']:.2%}
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card" style="
            background: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 10px;
            border: 2px solid {best_model_metrics['color']};
            text-align: center;
        ">
            <h3 style="color: {best_model_metrics['color']}; margin-bottom: 10px; font-family: 'Orbitron', sans-serif;">Recall</h3>
            <p style="font-size: 1.5rem; color: {best_model_metrics['color']}; font-weight: bold; font-family: 'Orbitron', sans-serif;">
                {best_model_metrics['recall']:.2%}
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="metric-card" style="
            background: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 10px;
            border: 2px solid {best_model_metrics['color']};
            text-align: center;
        ">
            <h3 style="color: {best_model_metrics['color']}; margin-bottom: 10px; font-family: 'Orbitron', sans-serif;">F1 Score</h3>
            <p style="font-size: 1.5rem; color: {best_model_metrics['color']}; font-weight: bold; font-family: 'Orbitron', sans-serif;">
                {best_model_metrics['F1 Score']:.2%}
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Add a glowing border effect for the best model
    st.markdown(f"""
    <div style="
        padding: 20px;
        border-radius: 10px;
        border: 2px solid {best_model_metrics['color']};
        box-shadow: 0 0 10px {best_model_metrics['color']}, 0 0 20px {best_model_metrics['color']};
        margin-top: 20px;
        text-align: center;
    ">
        <h3 style="color: {best_model_metrics['color']}; font-size: 1.8rem; font-family: 'Orbitron', sans-serif;">{best_model}</h3>
        <p style="color: #00d4ff; font-family: 'Orbitron', sans-serif;">This model has the highest accuracy among all models.</p>
    </div>
    """, unsafe_allow_html=True)

    # --- Section 2: Model Comparison ---
    st.markdown("### Model Comparison")
    st.markdown("Select models to compare their performance metrics:")

    # Multiselect for model comparison
    selected_models = st.multiselect(
        "Choose models to compare:",
        options=list(model_data.keys()),
        default=list(model_data.keys())[:2]  # Default to first two models
    )

    if selected_models:
        # Create a grouped bar chart for comparison
        fig = create_grouped_bar_chart(selected_models)
        st.plotly_chart(fig, use_container_width=True)

# Models Page
def models_page():
    st.markdown("### Model Performance Metrics")
    
    # Create two columns - one for buttons, one for the graph
    col1, col2 = st.columns([1, 3])
    
    # Model selection buttons in the first column
    with col1:
        st.markdown("#### Select Model")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Initialize session state for selected model if not exists
        if 'selected_model' not in st.session_state:
            st.session_state.selected_model = "Random Forest"
        
        # Create buttons for each model
        for model in model_data.keys():
            if st.button(model, key=f"btn_{model}"):
                st.session_state.selected_model = model
    
    # Display the graph in the second column
    with col2:
        # Create and display the bar chart
        fig = create_bar_chart(st.session_state.selected_model)
        st.plotly_chart(fig, use_container_width=True)
        
        # Add model description
        st.markdown(f"""
        <div class="metrics-card">
            <h3>Model Details: {st.session_state.selected_model}</h3>
            <p>Performance Metrics:</p>
            <ul style='color: #00d4ff;'>
                <li>Accuracy: {model_data[st.session_state.selected_model]["accuracy"]:.3f}</li>
                <li>Precision: {model_data[st.session_state.selected_model]["precision"]:.3f}</li>
                <li>Recall: {model_data[st.session_state.selected_model]["recall"]:.3f}</li>
                <li>F1 Score: {model_data[st.session_state.selected_model]["F1 Score"]:.3f}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Main Function
def main():
    # Apply custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # Sidebar Title
    st.sidebar.markdown('''
        <div class="sidebar-title">
            <h1>HacoHolics</h1>
        </div>
    ''', unsafe_allow_html=True)

    # Initialize session state for active tab
    if "tab" not in st.session_state:
        st.session_state["tab"] = "DASHBOARD"

    # Sidebar navigation
    with st.sidebar:
        st.write("")  # Add some spacing
        if st.button("DASHBOARD", key="dashboard"):
            st.session_state["tab"] = "DASHBOARD"
        if st.button("MODELS", key="models"):
            st.session_state["tab"] = "MODELS"

    # Main Title
    st.markdown('<h1 class="title-text"> AI/ML Malware Detection System</h1>', unsafe_allow_html=True)

    # Display content based on active tab
    if st.session_state["tab"] == "DASHBOARD":
        dashboard_page()
    elif st.session_state["tab"] == "MODELS":
        models_page()

# Run the app
if __name__ == "__main__":
    main()