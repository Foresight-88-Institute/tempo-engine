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
    .charter-text { font-family: 'Georgia', serif; color: #E0E0E0; }
</style>
""", unsafe_allow_html=True)

# 標題區
col1, col2 = st.columns([1, 4])
with col1: st.markdown("# ⏳") 
with col2:
    st.title("Foresight 88 Intelligence")
    st.markdown("**Tempo Economics™ Simulation Engine | v3.0 Causal Edition**")

st.markdown("---")
st.info("👆 **SYSTEM ARCHITECTURE**: This engine consists of two layers. Please switch tabs below to view **National Strategy** or **Personal Leadership**.")

# 建立分頁
tab1, tab2 = st.tabs(["🌍 National Sovereignty (Macro)", "🧠 Leader's Biological Tempo (Micro)"])

# ==========================================
# TAB 1: 國家宏觀模擬 (The Causal Macro Engine)
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
        **Objective: Minimize the 'Sovereignty Gap'.**
        *Note: In v3.0 Logic, higher Target Growth automatically degrades Effective Resilience.*
        1.  **Set Strategy**: Define target growth and systemic stress.
        2.  **Observe**: Watch how ambitious growth targets create automatic friction drag.
        3.  **Diagnosis**: The Gap represents the hidden cost of speed.
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
        human_resilience = st.slider("Human Capital Resilience (Base)", 0, 100, default_resilience)

    # === MACRO 运算核心 (v3.0 CAUSAL LOGIC) ===
    years = np.arange(2025, 2036)
    n_years = len(years)
    
    # 1. 基础 GDP 路径
    gdp = [100 * ((1 + target_growth/100) ** i) for i in range(n_years)]
    
    # 2. 因果关联：增长压力 (Growth Pressure)
    # 核心逻辑：你想要的增长越快，对系统的消耗越大。
    # 如果 Target Growth 是 10%，Resilience 会自动打折 50%
    growth_pressure = target_growth / 10 
    effective_resilience = human_resilience * (1 - growth_pressure * 0.5)
    
    # 3. 节奏失配 (使用 Effective Resilience 而不是 Base)
    tempo_misalignment = max(0, (tempo_stress - effective_resilience) / 100)
    
    ghdp = []
    for i in range(n_years):
        # A. 节奏震荡 (Oscillation)
        # 高 Misalignment 会导致剧烈波动
        oscillation = np.sin(i / 1.5) * tempo_misalignment * 0.12 # 放大了一点波动可见性
        
        # B. 修复幻觉 (Policy Relief)
        if i > 0 and i % 4 == 0:
            policy_relief = 0.08 # 救市力度
        else:
            policy_relief = 0
            
        # C. 不可逆侵蚀 (Irreversible Drag)
        # 这里的指数 i**1.5 更加严厉，模拟长期疲劳
        irreversible_drag = tempo_misalignment * 0.02 * (i ** 1.5)
        
        # 合成
        adjusted = 1 - irreversible_drag + oscillation + policy_relief
        adjusted = max(0, adjusted)
        ghdp.append(gdp[i] * adjusted)

    # 绘图
    st.subheader("3. The Sovereignty Gap Visualization")
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_alpha(0.0) 
    ax.set_facecolor('#0e1117') 
    
    ax.plot(years, gdp, color='#FF4B4B', linestyle='--', label='Systemic Velocity (GDP)', linewidth=2)
    ax.plot(years, ghdp, color='#C5A059', label='Biological Capacity (GHDP)', linewidth=3)
    
    ax.set_title("Forecast 2025-2035: The Cost of Acceleration", color='gray', fontsize=12)
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
        st.error(f"⚠️ **SYSTEM FAILURE**: Growth targets are cannibalizing resilience. Effective Resilience has dropped to {int(effective_resilience)}.")
    elif tempo_misalignment > 0.1:
        st.warning(f"⚠️ **DRAG DETECTED**: High growth ({target_growth}%) is creating structural friction.")
    else:
        st.success("✅ **SYNCHRONIZED**: Growth pace matches biological capacity.")
        
    st.caption(f"**Analyst Note**: At {target_growth}% Target Growth, the system suffers a -{int(growth_pressure*50)}% penalty on resilience. This reflects the biological cost of speed.")

# ==========================================
# TAB 2: 個人/領袖掃描 (Micro - Nonlinear Burnout)
# ==========================================
with tab2:
    st.markdown("### 🧬 The Executive Biological Ledger")
    st.caption("*Current Mode: Subjective Perception Input.* *🚀 **Roadmap v2.0**: Integration with **Apple Health / Oura Ring API**.*")
    
    with st.expander("ℹ️ **EXECUTIVE PROTOCOL: How to Run (Click to Expand)**", expanded=True):
        st.markdown("""
        **Objective: Avoid the 'Non-linear Crash'.**
        1.  **Input Load**: High fragmentation accelerates burnout exponentially.
        2.  **Input Fuel**: Sleep is the only hedge against decision fatigue.
        3.  **Forecast**: v3.0 logic applies a 'Fatigue Penalty' — burnout is not linear, it is catastrophic.
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

    # === MICRO 运算核心 (v3.0 NON-LINEAR LOGIC) ===
    biological_cost = (decision_load * 8) + (fragmentation * 5)
    biological_recovery = (sleep_quality * 6) + (flow_state * 15)
    net_tempo = biological_recovery - biological_cost
    
    # v3.0 Upgrade: Nonlinear Fatigue Penalty
    # 如果 net_tempo 是负的，惩罚会呈指数级增长
    if net_tempo < 0:
        fatigue_penalty = (abs(net_tempo) ** 1.3) * 0.5
    else:
        fatigue_penalty = 0
        
    base_score = max(0, min(100, 50 + net_tempo - fatigue_penalty))

    with col_diag:
        st.subheader("🧠 Real-time Audit")
        
        if base_score > 75:
            score_color, status, msg = "normal", "SOVEREIGN STATE", "Operating with surplus energy. Legacy building mode."
        elif base_score > 40:
            score_color, status, msg = "off", "FUNCTIONAL DEBT", "Adrenaline masking active. Crash risk rising."
        else:
            score_color, status, msg = "inverse", "SYSTEMIC INSOLVENCY", "CRITICAL: Non-linear collapse imminent. Stop."

        st.metric("Biological Sovereignty Score", f"{int(base_score)} / 100", status, delta_color=score_color)
        st.progress(int(base_score))
        st.info(f"💡 **Diagnosis**: {msg}")

        # === 30-Day Burnout Horizon ===
        st.markdown("#### 📉 30-Day Forecast: The Crash Curve")
        
        days = np.arange(1, 31)
        trajectory = []
        volatility_factor = fragmentation * 0.6 
        
        for d in days:
            # 基础漂移 (含非线性惩罚)
            drift = (net_tempo - fatigue_penalty) * 0.1 * d
            # 波动
            daily_fluctuation = np.sin(d) * volatility_factor
            # 肾上腺素代偿 (Adrenaline Masking)
            adrenaline_boost = 0
            if net_tempo < 0 and d < 9: # 延长一点代偿期，让后面的跌落更痛
                adrenaline_boost = abs(net_tempo) * 0.8 * np.sin(d/9 * np.pi)
            
            val = base_score + drift + daily_fluctuation + adrenaline_boost
            trajectory.append(max(0, min(100, val)))
        
        fig_micro, ax_micro = plt.subplots(figsize=(6, 3))
        fig_micro.patch.set_alpha(0.0)
        ax_micro.set_facecolor('#0e1117')
        
        line_color = '#C5A059' if base_score >= 50 else '#FF4B4B'
        
        ax_micro.plot(days, trajectory, color=line_color, linewidth=2, label='Projected Capacity')
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
            st.caption("⚠️ **v3.0 Logic**: Burnout is non-linear. The 'Adrenaline Masking' (first week peaks) will fail abruptly.")

# ==========================================
# FOOTER: Legal Boundary & Contact
# ==========================================
st.markdown("---")

# 簡化的 Legal Boundary
with st.expander("⚖️ **Legal Boundary**", expanded=False):
    st.caption("""
    This application presents a research simulation for conceptual and illustrative purposes only.
    It does not provide medical, financial, or policy advice.
    """)

# 戰略對話與聯繫方式
st.markdown("### 🤝 **Initialize Strategic Dialogue**")
st.write("To deploy the GHDP™ framework in your jurisdiction or organization, contact the Foresight 88 research team.")

c1, c2, c3 = st.columns([1, 1, 3])
with c1: 
    st.link_button("📧 Email Us", "mailto:eunice.wong@foresight88.institute")
with c2: 
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/eunice-wong-ba8399362/")
with c3: 
    st.caption("© 2025 Foresight 88 Institute. All Rights Reserved.")

# ==========================================
# HIDDEN CHARTER (For Logic Consistency)
# ==========================================
# 這裡放置 Charter 內容但預設折疊，確保版本號 v3.0 一致
with st.expander("📜 **Foresight 88 Research Charter (v3.0)**", expanded=False):
    st.markdown("""
    **Institution:** Foresight 88 Institute | **Model Status:** v3.0 Causal Edition
    > *Sovereignty collapses not from growth, but from repeated tempo misalignment.*
    """)
