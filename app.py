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
    h1 { color: #C5A059 !important; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; white-space: pre-wrap; border-radius: 4px 4px 0px 0px;
        gap: 1px; padding-top: 10px; padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] { border-bottom: 2px solid #C5A059; font-weight: bold; }
    .stSlider [data-baseweb="slider"] { color: #C5A059; }
</style>
""", unsafe_allow_html=True)

# 標題區
col1, col2 = st.columns([1, 4])
with col1: st.markdown("# ⏳") 
with col2:
    st.title("Foresight 88 Intelligence")
    st.markdown("**Tempo Economics™ Simulation Engine | v2.2 Misalignment Model**")

st.markdown("---")
st.info("👆 **SYSTEM ARCHITECTURE**: This engine consists of two layers. Please switch tabs below to view **National Strategy** or **Personal Leadership**.")

# 建立分頁
tab1, tab2 = st.tabs(["🌍 National Sovereignty (Macro)", "🧠 Leader's Biological Tempo (Micro)"])

# ==========================================
# TAB 1: 國家宏觀模擬 (Tempo Misalignment Engine)
# ==========================================
with tab1:
    st.subheader("1. Context Configuration")
    st.caption("👇 **Tap below to switch Jurisdiction Context:**")
    
    scenario = st.selectbox(
        "Select Target Region 🔽",
        ["Abu Dhabi (Vision 2030) 🇦🇪", "Singapore (Smart Nation) 🇸🇬", "Japan (Stagnation) 🇯🇵", "South Korea (Crisis) 🇰🇷"]
    )
    
    # 預設參數
    if "Abu Dhabi" in scenario:
        default_growth, default_stress, default_resilience = 5.5, 45, 85
        desc = "High resource buffer. Opportunity to define global tempo."
    elif "Singapore" in scenario:
        default_growth, default_stress, default_resilience = 3.5, 70, 75
        desc = "High efficiency. Approaching the 'Optimization Ceiling'."
    elif "Japan" in scenario:
        default_growth, default_stress, default_resilience = 1.2, 65, 40
        desc = "Structural fatigue evident. Low volatility but high drag."
    else: # Korea
        default_growth, default_stress, default_resilience = 2.5, 90, 30
        desc = "CRITICAL: Tempo misalignment exceeds biological limits. High oscillation risk."

    st.caption(f"💡 **Context Intelligence**: {desc}")
    
    with st.expander("ℹ️ **MACRO PROTOCOL: How to Run (Click to Expand)**", expanded=False):
        st.markdown("""
        **Objective: Observe the 'Struggle' between Policy and Biology.**
        1.  **Set Strategy**: Define target growth and systemic stress.
        2.  **Observe**: The Gold Line (GHDP) will oscillate and try to recover (Policy Relief).
        3.  **Diagnosis**: Watch how 'Irreversible Drag' eventually pulls the system down despite corrections.
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

    # 4. 運算核心 (THE NEW ENGINE)
    # 核心思想：Sovereignty collapses from repeated tempo misalignment.
    
    years = np.arange(2025, 2036)
    n_years = len(years)
    
    # A. GDP 路径 (Base Velocity)
    gdp = [100 * ((1 + target_growth/100) ** i) for i in range(n_years)]
    
    # B. 节奏失配强度 (Misalignment Intensity 0-1)
    # 当压力 > 韧性，失配开始产生
    tempo_misalignment = max(0, (tempo_stress - human_resilience) / 100)
    
    ghdp = []
    
    # 用于存储中间变量以便调试或以后展示
    debug_oscillation = []
    debug_drag = []
    
    for i in range(n_years):
        # 1. 核心一：节奏震荡 (Tempo Oscillation)
        # 生物与制度的冲突，导致系统不稳。i/1.5 控制震荡频率
        oscillation = np.sin(i / 1.5) * tempo_misalignment * 0.08
        
        # 2. 核心二：修复幻觉 (Policy Relief Illusion)
        # 每4年一次的政策刺激或选举年，系统以为自己修好了
        if i > 0 and i % 4 == 0:
            policy_relief = 0.06 # 短暂的反弹
        else:
            policy_relief = 0
            
        # 3. 核心三：不可逆生物侵蚀 (Irreversible Drag)
        # 疲劳是非线性的 (i ** 1.4)，时间越久，拖累越重
        irreversible_drag = tempo_misalignment * 0.015 * (i ** 1.4)
        
        # 4. 最终合成
        # 基础调整系数 = 1 - 拖累 + 震荡 + 救市
        adjusted = 1 - irreversible_drag + oscillation + policy_relief
        adjusted = max(0, adjusted) # 主权不能为负
        
        ghdp.append(gdp[i] * adjusted)

    # 5. 繪製圖表
    st.subheader("3. The Tempo Misalignment Visualization")
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_alpha(0.0) 
    ax.set_facecolor('#0e1117') 
    
    ax.plot(years, gdp, color='#FF4B4B', linestyle='--', label='Systemic Velocity (GDP)', linewidth=2)
    # GHDP 线条
    ax.plot(years, ghdp, color='#C5A059', label='Biological Capacity (GHDP)', linewidth=3)
    
    ax.set_title("Forecast 2025-2035: The Struggle for Rhythm", color='gray', fontsize=12)
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
    m2.metric("2035 GHDP Projection", f"${int(ghdp[-1])}B", f"Gap: -{int(final_gap)}B", delta_color="inverse")
    
    # 动态点评
    if tempo_misalignment > 0.4:
        st.error(f"⚠️ **SYSTEM FAILURE**: Biology has collapsed under stress. Notice the sharp divergence after 2030.")
    elif tempo_misalignment > 0.1:
        st.warning("⚠️ **OSCILLATION DETECTED**: System is fighting to recover (see peaks), but drag is accumulating.")
    else:
        st.success("✅ **SYNCHRONIZED**: Tempo is aligned. Growth is sustainable.")
        
    st.caption("Note: The temporary uplifts in the Gold Line represent 'Policy Relief Illusions' — structural corrections that fail to address the root biological drag.")

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
        1.  **Audit Liabilities**: Adjust 'Decisions' and 'Fragmentation'.
        2.  **Assess Assets**: Input your sleep quality and deep work hours.
        3.  **Check the Horizon**: Look at the **30-Day Burnout Horizon** graph below.
        """)

    col_input, col_diag = st.columns([1, 1])
    
    with col_input:
        st.subheader("1. The Load (Liabilities)")
        decision_load = st.slider("High-Stakes Decisions / Day", 0, 10, 4)
        fragmentation = st.slider("Cognitive Fragmentation (1-10)", 1, 10, 7)
        st.markdown("---")
        st.subheader("2. The Fuel (Assets)")
        sleep_quality = st.slider("Restorative Depth (1-10)", 1, 10, 6)
        flow_state = st.slider("Deep Work / Flow State (Hours)", 0.0, 4.0, 1.0, 0.5)

    # Micro 算法
    biological_cost = (decision_load * 8) + (fragmentation * 5)
    biological_recovery = (sleep_quality * 6) + (flow_state * 15)
    net_tempo = biological_recovery - biological_cost
    sovereignty_score = max(0, min(100, 50 + net_tempo))

    with col_diag:
        st.subheader("🧠 Real-time Audit")
        
        if sovereignty_score > 75:
            score_color, status, msg = "normal", "SOVEREIGN STATE", "Operating with surplus energy. Legacy building mode."
        elif sovereignty_score > 40:
            score_color, status, msg = "off", "FUNCTIONAL DEBT", "Borrowing energy from tomorrow. Sustainable for weeks only."
        else:
            score_color, status, msg = "inverse", "SYSTEMIC INSOLVENCY", "CRITICAL: Judgment mathematically compromised."

        st.metric("Biological Sovereignty Score", f"{int(sovereignty_score)} / 100", status, delta_color=score_color)
        st.progress(int(sovereignty_score))
        st.info(f"💡 **Diagnosis**: {msg}")

        st.markdown("#### 📉 30-Day Burnout Horizon")
        days = np.arange(1, 31)
        daily_drift = net_tempo * 0.1 
        trajectory = [max(0, min(100, sovereignty_score + (daily_drift * d))) for d in days]
        
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
# FOOTER
# ==========================================
st.markdown("---")
with st.expander("⚖️ **Disclaimer & Research Philosophy**"):
    st.markdown("""
    **Foresight 88 Institute | Research Model (v2.2)**
    **Core Thesis**: Sovereignty collapses not from growth, but from repeated tempo misalignment.
    **Methodology**: This engine simulates the friction between systemic acceleration and biological limits, accounting for 'policy relief illusions' and irreversible fatigue.
    """)

st.markdown("### 🤝 **Initialize Strategic Dialogue**")
st.write("To deploy the GHDP™ framework, contact Foresight 88.")
c1, c2, c3 = st.columns([1, 1, 3])
with c1: st.link_button("📧 Email Us", "mailto:eunice.wong@foresight88.institute")
with c2: st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/eunice-wong-ba8399362/")
with c3: st.caption("© 2025 Foresight 88 Institute. All Rights Reserved.")
