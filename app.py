# v3.2 Release Candidate — Parameters frozen for research testing
# Foresight 88 Institute | Tempo Intelligence Framework

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
    st.markdown("**Tempo Economics™ Simulation Engine | v3.2 Release Candidate**")

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
    
    # 預設參數 (Frozen for Research)
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

    # === MACRO 运算核心 (FROZEN) ===
    years = np.arange(2025, 2036)
    n_years = len(years)
    
    gdp = [100 * ((1 + target_growth/100) ** i) for i in range(n_years)]
    growth_pressure = target_growth / 10 
    effective_resilience = human_resilience * (1 - growth_pressure * 0.5)
    tempo_misalignment = max(0, (tempo_stress - effective_resilience) / 100)
    
    ghdp = []
    for i in range(n_years):
        oscillation = np.sin(i / 1.5) * tempo_misalignment * 0.12
        if i > 0 and i % 4 == 0:
            policy_relief = 0.08 
        else:
            policy_relief = 0
        irreversible_drag = tempo_misalignment * 0.02 * (i ** 1.5)
        
        adjusted = 1 - irreversible_drag + oscillation + policy_relief
        adjusted = max(0, adjusted)
        ghdp.append(gdp[i] * adjusted)

    # === RATIO CALCULATION ===
    capacity_ratio = np.array(ghdp) / np.array(gdp)

    # 绘图 1: 主图
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

    # 绘图 2: Ratio Chart
    st.markdown("#### 📉 Synchronization Ratio (Bio-Efficiency)")
    fig_ratio, ax_ratio = plt.subplots(figsize=(10, 2))
    fig_ratio.patch.set_alpha(0.0)
    ax_ratio.set_facecolor('#0e1117')
    ax_ratio.plot(years, capacity_ratio, color='#C5A059', linewidth=2, label='Bio/System Ratio')
    ax_ratio.axhline(1, color='gray', linestyle='--', alpha=0.5, linewidth=1)
    ax_ratio.set_ylim(0, 1.1)
    ax_ratio.tick_params(axis='x', colors='gray')
    ax_ratio.tick_params(axis='y', colors='gray')
    ax_ratio.grid(color='#444444', linestyle=':', linewidth=0.5)
    ax_ratio.spines['top'].set_visible(False)
    ax_ratio.spines['right'].set_visible(False)
    ax_ratio.spines['bottom'].set_color('gray')
    ax_ratio.spines['left'].set_color('gray')
    st.pyplot(fig_ratio)
    
    # 🛡️ DEFENSE PATCH 2: Policy Relief Explanation
    st.caption("**Metric Analysis**: This ratio represents biological synchronization. *Note: Policy relief cycles (the temporary peaks) are stylized placeholders representing systemic intervention.*")

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
        
    # 🛡️ DEFENSE PATCH 1: Magnitude Disclaimer
    st.caption(f"**Analyst Note**: At {target_growth}% Target Growth, the system suffers a -{int(growth_pressure*50)}% penalty on resilience. *The penalty coefficients are directional stress amplifiers, used to preserve causal monotonicity.*")

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
        3.  **Forecast**: v3.0 logic applies a 'Fatigue Penalty'. **This module models decision fatigue as a governance risk, not a health condition.**
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

    # === MICRO 运算核心 (FROZEN) ===
    biological_cost = (decision_load * 8) + (fragmentation * 5)
    biological_recovery = (sleep_quality * 6) + (flow_state * 15)
    net_tempo = biological_recovery - biological_cost
    
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
            drift = (net_tempo - fatigue_penalty) * 0.1 * d
            daily_fluctuation = np.sin(d) * volatility_factor
            adrenaline_boost = 0
            if net_tempo < 0 and d < 9:
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
# FOOTER: Legal, Contact & Expert Review
# ==========================================
st.markdown("---")

# 1. 🛡️ DEFENSE PATCH 3: Legal Boundary (Governance Risk)
with st.expander("⚖️ **Legal Boundary**", expanded=False):
    st.caption("""
    This application presents a research simulation for conceptual and illustrative purposes only.
    It does not provide medical, financial, or policy advice.
    **The Micro module models decision fatigue as a governance risk, not a health condition.**
    """)

# 2. 戰略對話與聯繫方式
st.markdown("### 🤝 **Initialize Strategic Dialogue**")
st.write("To deploy the GHDP™ framework in your jurisdiction or organization, contact the Foresight 88 research team.")

c1, c2, c3 = st.columns([1, 1, 3])
with c1: 
    st.link_button("📧 Email Us", "mailto:eunice.wong@foresight88.institute")
with c2: 
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/eunice-wong-ba8399362/")
with c3: 
    st.caption("© 2025 Foresight 88 Institute. All Rights Reserved.")

# 3. EXPERT REVIEW Q&A (Full Documentation)
st.markdown("---")
with st.expander("🛡️ **Expert Review — Anticipated Challenges & Research Boundaries**", expanded=False):
    st.markdown("""
    ### **Foresight 88 | Tempo Intelligence (v3.2 Release Candidate)**
    #### **Anticipated Challenges & Research Boundaries**

    ---

    **Q1. “Isn’t this just GDP with a subjective adjustment?”**
    > **Short Answer:** No. GDP measures velocity. This framework examines capacity synchronization.
    * **Extended Clarification:** GDP assumes that higher output velocity is universally absorbable. The Tempo Intelligence framework introduces biological and institutional limits as independent constraints, not moral overlays.
    * *GDP answers how fast the system moves. GHDP asks whether the system can still metabolize that speed.*

    **Q2. “Where is the empirical calibration? These parameters seem arbitrary.”**
    > **Short Answer:** They are intentionally non-calibrated.
    * **Extended Clarification:** This model does not aim for predictive accuracy or historical fit. Its purpose is structural reasoning, not econometric forecasting.
    * Parameters are designed to be: **Directionally monotonic**, **Causally interpretable**, and **Stress-testable by the user**.
    * Calibration would imply false precision. *This is a causal sandbox, not a regression engine.*

    **Q3. “Why assume higher growth degrades resilience?”**
    > **Short Answer:** Growth builds capacity only when tempo is metabolizable.
    * **Extended Clarification:** v3.0 introduces a growth-pressure mechanism: Higher target growth compresses institutional recovery cycles and decision latency.
    * *Growth is not dangerous. Unsynchronized acceleration is.*

    **Q4. “Isn’t the ‘Leader’s Biological Tempo’ dangerously close to pseudoscience?”**
    > **Short Answer:** Only if interpreted as diagnosis — which it explicitly is not.
    * **Extended Clarification:** The Micro layer is a self-reflective stress instrument. **No health data is collected.**
    * The intent is to visualize non-linear fatigue dynamics as a **governance risk**. *This module provokes awareness, not verdicts.*

    ---
    #### **Closing Boundary Statement**
    **It asks one question only: At what point does speed stop compounding — and start consuming — sovereignty?**

    🔒 **Version Notice**
    This Q&A applies to v3.2 Release Candidate.
    Model parameters are intentionally frozen for expert review.
    """)
