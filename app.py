import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 0. 頁面配置 ---
st.set_page_config(
    page_title="Foresight 88 | Tempo Intelligence",
    page_icon="⏳",
    layout="wide"
)

# 自定義 CSS
st.markdown("""
<style>
    h1 {
        color: #C5A059 !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        border-bottom: 2px solid #C5A059;
        font-weight: bold;
    }
    .stSlider [data-baseweb="slider"] {
        color: #C5A059;
    }
    .nav-instruction {
        font-size: 14px;
        color: #888;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 標題區
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("# ⏳") 
with col2:
    st.title("Foresight 88 Intelligence")
    st.markdown("**Tempo Economics™ Simulation Engine | v2.0 Beta**")

st.markdown("---")

# === 全局導航提示 ===
st.info("👆 **SYSTEM ARCHITECTURE**: This engine consists of two layers. Please switch tabs below to view **National Strategy** or **Personal Leadership**.")

# 建立分頁
tab1, tab2 = st.tabs(["🌍 National Sovereignty (Macro)", "🧠 Leader's Biological Tempo (Micro)"])

# ==========================================
# TAB 1: 國家宏觀模擬 (Macro)
# ==========================================
with tab1:
    st.subheader("1. Context Configuration")
    
    # --- UX FIX: 增加明確的「點擊這裡」提示 ---
    st.caption("👇 **Tap below to switch Jurisdiction Context:**")
    
    scenario = st.selectbox(
        "Select Target Region 🔽", # 標題加入箭頭暗示
        ["Abu Dhabi (Vision 2030) 🇦🇪", "Singapore (Smart Nation) 🇸🇬", "Japan (Stagnation) 🇯🇵", "South Korea (Crisis) 🇰🇷"]
    )
    
    # 2. 預設參數
    if "Abu Dhabi" in scenario:
        default_growth = 5.5
        default_stress = 45
        default_resilience = 85
        desc = "High resource buffer, ambitious AI integration. Opportunity to define global tempo."
    elif "Singapore" in scenario:
        default_growth = 3.5
        default_stress = 70
        default_resilience = 75
        desc = "High efficiency, high stress. Approaching the 'Optimization Ceiling'."
    elif "Japan" in scenario:
        default_growth = 1.2
        default_stress = 65
        default_resilience = 40
        desc = "Aging demographic limits resilience. Structural fatigue evident."
    else: # Korea
        default_growth = 2.5
        default_stress = 90
        default_resilience = 30
        desc = "CRITICAL: Tempo stress exceeds biological recovery limits. Demographic collapse risk."

    st.caption(f"💡 **Context Intelligence**: {desc}")
    
    # Macro 使用指南
    with st.expander("ℹ️ **MACRO PROTOCOL: How to Run (Click to Expand)**", expanded=False):
        st.markdown("""
        **Objective: Minimize the gap between Growth (Red) and Human Capacity (Gold).**
        1.  **Define Strategy**: Set your target GDP growth.
        2.  **Apply Stress**: Increase 'Systemic Acceleration' to simulate high-tempo policies.
        3.  **Observe**: Watch for the 'Sovereignty Gap' where human resilience fails to keep up.
        """)
    
    st.markdown("---")
    st.subheader("2. Stress Test Parameters")

    # 3. 互動滑桿
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        target_growth = st.slider("Target GDP Growth (%)", 0.0, 10.0, default_growth)
    with col_b:
        tempo_stress = st.slider("Systemic Acceleration (Stress)", 0, 100, default_stress)
    with col_c:
        human_resilience = st.slider("Human Capital Resilience", 0, 100, default_resilience)

    # 4. 運算核心
    years = np.arange(2025, 2036)
    n_years = len(years)
    
    gdp = [100 * ((1 + target_growth/100) ** i) for i in range(n_years)]
    
    friction_gap = max(0, (tempo_stress - human_resilience))
    decay_rate = friction_gap * 0.005 
    
    ghdp = []
    for i in range(n_years):
        cumulative_drag = (decay_rate * i * i) 
        val = gdp[i] * (1 - cumulative_drag)
        ghdp.append(val)

    # 5. 繪製圖表
    st.subheader("3. The Sovereignty Gap Visualization")
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_alpha(0.0) 
    ax.set_facecolor('#0e1117') 
    
    ax.plot(years, gdp, color='#FF4B4B', linestyle='--', label='Traditional GDP (Nominal)', linewidth=2)
    ax.plot(years, ghdp, color='#C5A059', label='Real GHDP (Human-Adjusted)', linewidth=3)
    
    ax.set_title("Forecast 2025-2035", color='gray', fontsize=12)
    ax.tick_params(axis='x', colors='gray')
    ax.tick_params(axis='y', colors='gray')
    ax.legend(facecolor='#0e1117', labelcolor='white')
    ax.grid(color='#444444', linestyle=':', linewidth=0.5)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('gray')
    ax.spines['left'].set_color('gray')

    st.pyplot(fig)

    # 6. 戰略診斷
    final_gap = gdp[-1] - ghdp[-1]
    
    m1, m2, m3 = st.columns(3)
    m1.metric("2035 GDP Projection", f"${int(gdp[-1])}B", "+Growth")
    m2.metric("2035 GHDP Projection", f"${int(ghdp[-1])}B", f"-{int(final_gap)}B Gap", delta_color="inverse")
    
    if final_gap > 30:
        st.error(f"⚠️ **SYSTEMIC WARNING**: Your strategy creates a **${int(final_gap)}B Human Deficit**. Structural instability predicted by 2029.")
    elif final_gap > 10:
        st.warning("⚠️ **RISK**: Friction is accumulating. Recommend implementing 'Tempo Policies'.")
    else:
        st.success("✅ **OPTIMAL**: Sovereignty is secure. Human capital is aligned with growth.")

# ==========================================
# TAB 2: 個人/領袖掃描 (Micro)
# ==========================================
with tab2:
    st.markdown("### 🧬 The Executive Biological Ledger")
    
    st.caption("""
    *Current Mode: Subjective Perception Input.* *🚀 **Roadmap v2.0**: Integration with **Apple Health / Oura Ring API** for real-time biometric telemetry. (Partnership pending)*
    """)
    
    with st.expander("ℹ️ **EXECUTIVE PROTOCOL: How to Run (Click to Expand)**", expanded=True):
        st.markdown("""
        **Objective: Maintain a positive Biological Tempo Score (>75).**
        1.  **Audit Liabilities**: Adjust 'Decisions' and 'Fragmentation' to match your current workload.
        2.  **Assess Assets**: Input your sleep quality and deep work hours.
        3.  **Check the Horizon**: Look at the **30-Day Burnout Horizon** graph below. Is it trending down?
        """)

    col_input, col_diag = st.columns([1, 1])
    
    with col_input:
        st.subheader("1. The Load (Liabilities)")
        decision_load = st.slider(
            "High-Stakes Decisions / Day", 
            min_value=0, max_value=10, value=4,
            help="Decisions involving >$1M impact or reputational risk."
        )
        
        fragmentation = st.slider(
            "Cognitive Fragmentation (1-10)", 
            min_value=1, max_value=10, value=7,
            help="1 = Monk mode, 10 = Constant interruptions/fire-fighting."
        )

        st.markdown("---")
        
        st.subheader("2. The Fuel (Assets)")
        sleep_quality = st.slider(
            "Restorative Depth (1-10)", 
            min_value=1, max_value=10, value=6,
            help="1 = Woke up tired, 10 = Woke up ready to conquer."
        )
        
        flow_state = st.slider(
            "Deep Work / Flow State (Hours)", 
            min_value=0.0, max_value=4.0, value=1.0, step=0.5,
            help="Uninterrupted time for strategic thinking."
        )

    # 核心算法
    biological_cost = (decision_load * 8) + (fragmentation * 5)
    biological_recovery = (sleep_quality * 6) + (flow_state * 15)
    
    net_tempo = biological_recovery - biological_cost
    sovereignty_score = 50 + net_tempo
    sovereignty_score = max(0, min(100, sovereignty_score))

    with col_diag:
        st.subheader("🧠 Real-time Audit")
        
        if sovereignty_score > 75:
            score_color = "normal" 
            status = "SOVEREIGN STATE"
            msg = "You are operating with surplus energy. This is where legacy is built."
        elif sovereignty_score > 40:
            score_color = "off"
            status = "FUNCTIONAL DEBT"
            msg = "You are borrowing energy from tomorrow. Sustainable for weeks, not months."
        else:
            score_color = "inverse"
            status = "SYSTEMIC INSOLVENCY"
            msg = "CRITICAL: Decision quality is mathematically compromised. Stop."

        st.metric(label="Biological Sovereignty Score", value=f"{int(sovereignty_score)} / 100", delta=status, delta_color=score_color)
        
        st.progress(int(sovereignty_score))
        
        st.info(f"💡 **Diagnosis**: {msg}")

        st.markdown("#### 📉 30-Day Burnout Horizon")
        days = np.arange(1, 31)
        daily_drift = net_tempo * 0.1 
        trajectory = [sovereignty_score + (daily_drift * d) for d in days]
        trajectory = [max(0, min(100, t)) for t in trajectory]
        
        fig_micro, ax_micro = plt.subplots(figsize=(6, 3))
        fig_micro.patch.set_alpha(0.0)
        ax_micro.set_facecolor('#0e1117')
        
        line_color = '#C5A059' if daily_drift >= 0 else '#FF4B4B'
        ax_micro.plot(days, trajectory, color=line_color, linewidth=3)
        ax_micro.axhline(y=40, color='gray', linestyle='--', linewidth=1, label='Crash Threshold')
        
        ax_micro.set_ylim(0, 100)
        ax_micro.set_xlabel("Days from Now", color='gray', fontsize=8)
        ax_micro.set_ylabel("Cognitive Capacity", color='gray', fontsize=8)
        ax_micro.tick_params(colors='gray')
        ax_micro.spines['top'].set_visible(False)
        ax_micro.spines['right'].set_visible(False)
        ax_micro.spines['bottom'].set_color('gray')
        ax_micro.spines['left'].set_color('gray')
        
        st.pyplot(fig_micro)

# ==========================================
# FOOTER: 免責聲明與聯繫
# ==========================================
st.markdown("---")

with st.expander("⚖️ **Disclaimer & Research Philosophy (Open to Read)**"):
    st.markdown("""
    **Foresight 88 Institute | Preliminary Research Model (v2.0)**
    
    1.  **Nature of Simulation**: This engine is a theoretical prototype designed to visualize the *Gross Human Dynamics Product (GHDP)* concept. It calculates the friction coefficient introduced by environmental stressors on human biological systems.
    
    2.  **Relation to GDP**: **We do not oppose GDP.** We view GDP as a metric of *Velocity*. GHDP is introduced as a complementary metric of *Sustainability*.
    
    3.  **Technological Stance**: **We are not anti-technology.** This model seeks to study the interplay between *algorithmic speed* and *biological recovery*, ensuring that technology serves human sovereignty.
    
    4.  **No Financial Advice**: The data projected here is for strategic illustrative purposes only.
    """)

st.markdown("### 🤝 **Initialize Strategic Dialogue**")
st.write("To deploy the GHDP™ framework in your jurisdiction or organization, contact the Foresight 88 research team.")

c1, c2, c3 = st.columns([1, 1, 3])
with c1:
    st.link_button("📧 Email Us", "mailto:eunice.wong@foresight88.institute")
with c2:
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/eunice-wong-ba8399362/")
with c3:
    st.caption("© 2025 Foresight 88 Institute. All Rights Reserved.")
