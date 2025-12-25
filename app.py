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
    st.markdown("**Tempo Economics™ Simulation Engine | v2.3 Dual-Volatility**")

st.markdown("---")
st.info("👆 **SYSTEM ARCHITECTURE**: This engine consists of two layers. Please switch tabs below to view **National Strategy** or **Personal Leadership**.")

# 建立分頁
tab1, tab2 = st.tabs(["🌍 National Sovereignty (Macro)", "🧠 Leader's Biological Tempo (Micro)"])

# ==========================================
# TAB 1: 國家宏觀模擬 (Macro - Tempo Misalignment)
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

    # 互动滑杆
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        target_growth = st.slider("Target GDP Growth (%)", 0.0, 10.0, default_growth)
    with col_b:
        tempo_stress = st.slider("Systemic Acceleration (Stress)", 0, 100, default_stress)
    with col_c:
        human_resilience = st.slider("Human Capital Resilience", 0, 100, default_resilience)

    # === MACRO 运算核心 ===
    years = np.arange(2025, 2036)
    n_years = len(years)
    
    gdp = [100 * ((1 + target_growth/100) ** i) for i in range(n_years)]
    tempo_misalignment = max(0, (tempo_stress - human_resilience) / 100)
    
    ghdp = []
    for i in range(n_years):
        # 1. 节奏震荡
        oscillation = np.sin(i / 1.5) * tempo_misalignment * 0.08
        # 2. 修复幻觉 (Policy Relief)
        if i > 0 and i % 4 == 0:
            policy_relief = 0.06 
        else:
            policy_relief = 0
        # 3. 不可逆侵蚀
        irreversible_drag = tempo_misalignment * 0.015 * (i ** 1.4)
        
        adjusted = 1 - irreversible_drag + oscillation + policy_relief
        adjusted = max(0, adjusted)
        ghdp.append(gdp[i] * adjusted)

    # 绘图
    st.subheader("3. The Tempo Misalignment Visualization")
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_alpha(0.0) 
    ax.set_facecolor('#0e1117') 
    
    ax.plot(years, gdp, color='#FF4B4B', linestyle='--', label='Systemic Velocity (GDP)', linewidth=2)
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

    # 诊断
    final_gap = gdp[-1] - ghdp[-1]
    m1, m2, m3 = st.columns(3)
    m1.metric("2035 GDP Projection", f"${int(gdp[-1])}B", "+Growth")
    m2.metric("2035 GHDP Projection", f"${int(ghdp[-1])}B", f"Gap: -{int(final_gap)}B", delta_color="inverse")
    
    if tempo_misalignment > 0.4:
        st.error(f"⚠️ **SYSTEM FAILURE**: Biology has collapsed under stress. Notice the sharp divergence after 2030.")
    elif tempo_misalignment > 0.1:
        st.warning("⚠️ **OSCILLATION DETECTED**: System is fighting to recover (see peaks), but drag is accumulating.")
    else:
        st.success("✅ **SYNCHRONIZED**: Tempo is aligned. Growth is sustainable.")
    st.caption("Note: The temporary uplifts in the Gold Line represent 'Policy Relief Illusions' — structural corrections that fail to address the root biological drag.")

# ==========================================
# TAB 2: 個人/領袖掃描 (Micro - Bio-Rhythm)
# ==========================================
with tab2:
    st.markdown("### 🧬 The Executive Biological Ledger")
    st.caption("*Current Mode: Subjective Perception Input.* *🚀 **Roadmap v2.0**: Integration with **Apple Health / Oura Ring API**.*")
    
    with st.expander("ℹ️ **EXECUTIVE PROTOCOL: How to Run (Click to Expand)**", expanded=True):
        st.markdown("""
        **Objective: Prevent 'The Adrenaline Cliff'.**
        1.  **Input Load**: High fragmentation creates 'Cognitive Volatility' (jagged lines).
        2.  **Input Fuel**: Sleep and Flow State provide the buffer.
        3.  **Forecast**: Observe if you are running on **True Energy** or **False Adrenaline**.
        """)

    col_input, col_diag = st.columns([1, 1])
    
    with col_input:
        st.subheader("1. The Load (Liabilities)")
        decision_load = st.slider("High-Stakes Decisions / Day", 0, 10, 4)
        # Fragmentation 现在直接关联到“波动率”
        fragmentation = st.slider("Cognitive Fragmentation (1-10)", 1, 10, 7)
        st.markdown("---")
        st.subheader("2. The Fuel (Assets)")
        sleep_quality = st.slider("Restorative Depth (1-10)", 1, 10, 6)
        flow_state = st.slider("Deep Work / Flow State (Hours)", 0.0, 4.0, 1.0, 0.5)

    # === MICRO 运算核心 (NEW) ===
    biological_cost = (decision_load * 8) + (fragmentation * 5)
    biological_recovery = (sleep_quality * 6) + (flow_state * 15)
    net_tempo = biological_recovery - biological_cost
    
    # 基础分数
    base_score = max(0, min(100, 50 + net_tempo))

    with col_diag:
        st.subheader("🧠 Real-time Audit")
        
        # 状态判断逻辑
        if base_score > 75:
            score_color, status, msg = "normal", "SOVEREIGN STATE", "Operating with surplus energy. Legacy building mode."
        elif base_score > 40:
            score_color, status, msg = "off", "FUNCTIONAL DEBT", "Running on adrenaline. Sustainable for weeks only."
        else:
            score_color, status, msg = "inverse", "SYSTEMIC INSOLVENCY", "CRITICAL: Judgment mathematically compromised."

        st.metric("Biological Sovereignty Score", f"{int(base_score)} / 100", status, delta_color=score_color)
        st.progress(int(base_score))
        st.info(f"💡 **Diagnosis**: {msg}")

        # === 30-Day Burnout Horizon (UPGRADED) ===
        st.markdown("#### 📉 30-Day Forecast: Adrenaline vs Reality")
        
        days = np.arange(1, 31)
        trajectory = []
        
        # 波动系数：碎片化越高，情绪/认知波动越大
        volatility_factor = fragmentation * 0.5 
        
        for d in days:
            # 1. 基础漂移 (Linear Drift)
            drift = net_tempo * 0.1 * d
            
            # 2. 认知波动 (Cognitive Volatility) - 模拟每天的状态起伏
            # 使用 sin 波模拟生理节律，fragmentation 决定波幅
            daily_fluctuation = np.sin(d) * volatility_factor
            
            # 3. 肾上腺素代偿 (Adrenaline Masking) - 所谓的 "False Second Wind"
            # 如果压力大 (net_tempo < 0)，前 7 天会有一个虚假的提升
            adrenaline_boost = 0
            if net_tempo < 0 and d < 8:
                adrenaline_boost = abs(net_tempo) * 0.5 * np.sin(d/8 * np.pi)
            
            # 合成
            val = base_score + drift + daily_fluctuation + adrenaline_boost
            trajectory.append(max(0, min(100, val)))
        
        fig_micro, ax_micro = plt.subplots(figsize=(6, 3))
        fig_micro.patch.set_alpha(0.0)
        ax_micro.set_facecolor('#0e1117')
        
        # 颜色逻辑：如果是负的 drift，用红色警示
        line_color = '#C5A059' if net_tempo >= 0 else '#FF4B4B'
        
        ax_micro.plot(days, trajectory, color=line_color, linewidth=2, label='Projected Capacity')
        
        # 绘制“崩溃阈值”线
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
        
        if net_tempo < 0:
            st.caption("⚠️ **Warning**: The peaks in the first week are 'Adrenaline Masking'. The crash follows shortly after.")

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
with st.expander("⚖️ **Disclaimer & Research Philosophy**"):
    st.markdown("""
    **Foresight 88 Institute | Research Model (v2.3)**
    **Core Thesis**: Sovereignty collapses not from growth, but from repeated tempo misalignment.
    **Methodology**: This engine simulates the friction between systemic acceleration and biological limits, accounting for 'policy relief illusions' (Macro) and 'adrenaline masking' (Micro).
    """)

st.markdown("### 🤝 **Initialize Strategic Dialogue**")
st.write("To deploy the GHDP™ framework, contact Foresight 88.")
c1, c2, c3 = st.columns([1, 1, 3])
with c1: st.link_button("📧 Email Us", "mailto:eunice.wong@foresight88.institute")
with c2: st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/eunice-wong-ba8399362/")
with c3: st.caption("© 2025 Foresight 88 Institute. All Rights Reserved.")
