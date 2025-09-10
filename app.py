
# Streamlit app for Getaround Analytics
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page configuration with modern settings
st.set_page_config(
    page_title="Getaround Analytics Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.getaround.com/help',
        'Report a bug': None,
        'About': "# Getaround Analytics Dashboard\nBuilt with Streamlit for rental data analysis"
    }
)

# Custom CSS for modern styling
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #aa1ba3;
        --secondary-color: #e699e6;
        --accent-color: #cc66cc;
        --background-color: #fafafa;
        --card-background: #ffffff;
        --text-primary: #262730;
        --text-secondary: #6c757d;
        --border-color: #e1e5e9;
        --success-color: #28a745;
        --warning-color: #ffc107;
        --danger-color: #dc3545;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Modern card styling */
    .metric-card {
        background: var(--card-background);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);
    }
    
    /* Enhanced sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, var(--primary-color) 0%, #8a1a8a 100%);
    }
    
    /* Modern button styling */
    .stButton > button {
        background: linear-gradient(45deg, var(--primary-color), var(--accent-color));
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(170, 27, 163, 0.3);
    }
    
    /* Modern slider styling */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
    }
    
    /* Enhanced metrics display */
    [data-testid="metric-container"] {
        background: var(--card-background);
        border: 1px solid var(--border-color);
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    
    [data-testid="metric-container"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.12);
    }
    
    /* Modern typography */
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, var(--primary-color), var(--accent-color));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .section-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: var(--primary-color);
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid var(--border-color);
    }
    
    /* Loading animation */
    .loading-spinner {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid var(--border-color);
        border-radius: 50%;
        border-top-color: var(--primary-color);
        animation: spin 1s ease-in-out infinite;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        .section-title {
            font-size: 1.5rem;
        }
        .metric-card {
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Load dataset with modern loading states
@st.cache_data
def load_data():
    """Load and cache the rental data with modern loading indicators."""
    try:
        with st.spinner('🔄 Loading rental data...'):
            df = pd.read_csv("processed_delay_getaround_data.csv")
            return df
    except FileNotFoundError:
        st.error("🚫 **Data file not found!** Please ensure 'processed_delay_getaround_data.csv' exists in the current directory.")
        st.info("💡 **Tip:** Run the data processing script first to generate the required CSV file.")
        return None
    except Exception as e:
        st.error(f"⚠️ **Failed to load data:** {str(e)}")
        st.info("🔧 **Troubleshooting:** Check if the CSV file is properly formatted and accessible.")
        return None

# Initialize the app
df = load_data()
if df is None:
    st.stop()

# Data preprocessing
df = df.rename(columns={
        "checkin_type": "type",
        "delay_at_checkout_in_minutes": "delay",
        "previous_ended_rental_id": "prev_id",
        "time_delta_with_previous_rental_in_minutes": "time_delta"
    })


# Modern Sidebar Design
with st.sidebar:
    # Logo and branding
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/8/8e/Getaround_%28Europe%29.png" 
             style="width: 180px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar content (Dashboard Sections and Quick Stats removed)
    
    # Attribution with modern styling
    st.markdown("""
    <div style="background: rgba(255,255,255,0.1); padding: 1rem; 
                border-radius: 8px; text-align: center; margin-top: 2rem;">
        <p style="color: #aa1ba3; margin: 0; font-size: 0.9rem; font-weight: 600;">
            Made By <strong>Francesco Giraldi 2025</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Modern Main Title
st.markdown("""
<div class="main-title">
    🚗 Getaround Analytics Dashboard
</div>
<div style="text-align: center; margin-bottom: 3rem; color: var(--text-secondary);">
    <p style="font-size: 1.2rem; margin: 0;">Comprehensive rental data analysis and buffer threshold simulation</p>
</div>
""", unsafe_allow_html=True)

# Section 1: Overview with modern styling

# Data Filters Section
st.markdown("""
<div style="background: var(--card-background); padding: 1.5rem; border-radius: 12px; 
            box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 2rem;">
    <h4 style="color: var(--primary-color); margin: 0 0 1rem 0;">🔍 Data Filters</h4>
</div>
""", unsafe_allow_html=True)

# Filter controls
col_filter, col_refresh = st.columns([3, 1])
with col_filter:
    checkin_filter = st.selectbox(
        "Check-in type:",
        options=["both", "mobile", "connect"],
        index=0,
        help="Filter rentals by check-in type"
    )
with col_refresh:
    if st.button("🔄 Refresh Data", help="Reload and refresh the dashboard data"):
        st.cache_data.clear()
        st.rerun()

# Apply filters
if checkin_filter != "both":
    df_filtered = df[df["type"] == checkin_filter]
else:
    df_filtered = df.copy()

# Filter ended rentals for metrics
df_ended = df_filtered[df_filtered["state"] == "ended"]
df_positive_delay = df_ended[df_ended["delay"].notna() & (df_ended["delay"] > 0)]

# Modern Metrics Display with Cards
st.markdown("""
<div style="margin: 2rem 0 1rem 0;">
    <h4 style="color: var(--primary-color); margin: 0;">📈 Key Performance Indicators</h4>
</div>
""", unsafe_allow_html=True)

# Primary metrics row
col1, col2, col3 = st.columns(3)
with col1:
    total_rentals = len(df_filtered)
    st.metric(
        "Total Rentals", 
        f"{total_rentals:,}",
        delta=f"{(total_rentals/len(df)*100):.1f}% of dataset" if checkin_filter != "both" else None,
        help="Total number of rentals in the selected filter"
    )
with col2:
    completed_rentals = len(df_ended)
    completion_rate = (completed_rentals / total_rentals * 100) if total_rentals > 0 else 0
    st.metric(
        "Completed Rentals", 
        f"{completed_rentals:,}",
        delta=f"{completion_rate:.1f}% completion rate",
        help="Rentals that were successfully completed"
    )
with col3:
    canceled_rentals = (df_filtered["state"] == "canceled").sum()
    cancellation_rate = (canceled_rentals / total_rentals * 100) if total_rentals > 0 else 0
    st.metric(
        "Canceled Rentals", 
        f"{canceled_rentals:,}",
        delta=f"{cancellation_rate:.1f}% cancellation rate",
        delta_color="inverse",
        help="Rentals that were canceled"
    )

# Secondary metrics row
col4, col5, col6 = st.columns(3)
with col4:
    delayed_rentals = len(df_positive_delay)
    delay_rate = (delayed_rentals / completed_rentals * 100) if completed_rentals > 0 else 0
    st.metric(
        "Rentals with Delay", 
        f"{delayed_rentals:,}",
        delta=f"{delay_rate:.1f}% of completed",
        delta_color="inverse",
        help="Completed rentals that had checkout delays"
    )
with col5:
    avg_delay = df_positive_delay['delay'].mean() if len(df_positive_delay) > 0 else 0
    st.metric(
        "Avg Delay", 
        f"{avg_delay:.1f} min",
        help="Average delay time for delayed rentals"
    )
with col6:
    median_delay = df_positive_delay['delay'].median() if len(df_positive_delay) > 0 else 0
    st.metric(
        "Median Delay", 
        f"{median_delay:.0f} min",
        help="Median delay time for delayed rentals"
    )

# Section 2: Buffer Threshold Simulation
st.markdown('<div class="section-title">📉 Buffer Threshold Impact Simulation</div>', unsafe_allow_html=True)

st.markdown("""
<div style="background: var(--card-background); padding: 1.5rem; border-radius: 12px; 
            box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 2rem;">
    <p style="margin: 0; color: var(--text-secondary); font-size: 1.1rem;">
        🎯 <strong>Simulation Purpose:</strong> Analyze how different buffer thresholds impact rental availability, 
        critical overlaps, and potential cancellation prevention.
    </p>
</div>
""", unsafe_allow_html=True)

# Interactive threshold selector with modern styling
col_slider1, col_slider2 = st.columns([3, 1])
with col_slider1:
    threshold = st.slider(
        "Buffer threshold (minutes):", 
        min_value=0, 
        max_value=720, 
        value=60, 
        step=10,
        help="Set the minimum time buffer between consecutive rentals"
    )
with col_slider2:
    st.markdown(f"""
    <div style="background: var(--primary-color); color: white; padding: 1rem; 
                border-radius: 8px; text-align: center; margin-top: 1rem;">
        <h3 style="margin: 0; font-size: 1.5rem;">{threshold}</h3>
        <p style="margin: 0; font-size: 0.9rem;">minutes</p>
    </div>
    """, unsafe_allow_html=True)

# Filter datasets for analysis
df_buffer = df_filtered[df_filtered["time_delta"].notna()]
df_critical = df_filtered.dropna(subset=["delay", "time_delta"])
df_critical = df_critical[df_critical["delay"] > df_critical["time_delta"]]
df_canceled = df_filtered[(df_filtered["state"] == "canceled") & (df_filtered["time_delta"].notna())]

# Compute metrics
total_rentals = len(df_filtered)
affected_pct = 100 * (df_buffer["time_delta"] < threshold).sum() / total_rentals

total_critical = len(df_critical)
solved_pct = 100 * (df_critical["time_delta"] < threshold).sum() / total_critical if total_critical else 0

total_canceled = len(df_canceled)
canceled_pct = 100 * (df_canceled["time_delta"] < threshold).sum() / total_canceled if total_canceled else 0

# Modern Results Display
st.markdown("""
<div style="background: var(--card-background); padding: 2rem; border-radius: 12px; 
            box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin: 2rem 0;">
    <h3 style="color: var(--primary-color); margin: 0 0 1.5rem 0; text-align: center;">
        🎯 Results for a {threshold}-minute buffer
    </h3>
</div>
""".format(threshold=threshold), unsafe_allow_html=True)

# Results metrics in cards
result_col1, result_col2, result_col3 = st.columns(3)
with result_col1:
    st.metric(
        "🏢 Rentals Affected",
        f"{affected_pct:.1f}%",
        help="Percentage of all rentals that would be impacted by this buffer threshold"
    )
with result_col2:
    st.metric(
        "✅ Critical Cases Solved",
        f"{solved_pct:.1f}%",
        help="Percentage of critical overlap cases that would be resolved"
    )
with result_col3:
    st.metric(
        "🚫 Cancellations Preventable",
        f"{canceled_pct:.1f}%",
        help="Percentage of cancellations that could potentially be prevented"
    )

# Modern Interactive Visualization
st.markdown("""
<div style="margin: 2rem 0 1rem 0;">
    <h4 style="color: var(--primary-color); margin: 0;">📊 Interactive Impact Analysis</h4>
</div>
""", unsafe_allow_html=True)

# Create modern Plotly chart
labels = ["Rentals Affected", "Critical Cases Solved", "Cancellations Preventable"]
values = [affected_pct, solved_pct, canceled_pct]
colors = ["#aa1ba3", "#cc66cc", "#e699e6"]

fig = go.Figure(data=[
    go.Bar(
        x=labels,
        y=values,
        marker_color=colors,
        text=[f"{v:.1f}%" for v in values],
        textposition='outside',
        textfont=dict(size=14, color='#262730'),
        hovertemplate='<b>%{x}</b><br>Impact: %{y:.1f}%<extra></extra>'
    )
])

fig.update_layout(
    title={
        'text': f"Impact Analysis: {threshold}-minute Buffer Threshold",
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 18, 'color': '#aa1ba3'}
    },
    xaxis={
        'title': '',
        'tickfont': {'size': 12, 'color': '#262730'}
    },
    yaxis={
        'title': {'text': 'Impact Percentage (%)', 'font': {'size': 14, 'color': '#262730'}},
        'range': [0, max(values) * 1.2],
        'tickfont': {'size': 12, 'color': '#262730'}
    },
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font={'family': 'Arial, sans-serif'},
    margin=dict(t=80, b=60, l=60, r=60),
    height=400
)

fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')

st.plotly_chart(fig, use_container_width=True)

# Additional insights
st.markdown("""
<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); 
            padding: 1.5rem; border-radius: 12px; margin-top: 2rem;">
    <h4 style="color: var(--primary-color); margin: 0 0 1rem 0;">💡 Key Insights</h4>
    <ul style="margin: 0; color: var(--text-secondary);">
        <li><strong>Availability Impact:</strong> {affected_pct:.1f}% of rentals would need longer gaps between bookings</li>
        <li><strong>Problem Resolution:</strong> {solved_pct:.1f}% of critical timing conflicts would be eliminated</li>
        <li><strong>Cancellation Prevention:</strong> Up to {canceled_pct:.1f}% of cancellations could potentially be avoided</li>
    </ul>
</div>
""".format(affected_pct=affected_pct, solved_pct=solved_pct, canceled_pct=canceled_pct), unsafe_allow_html=True)
