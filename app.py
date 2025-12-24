import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 0. 頁面配置 (Foresight 88 品牌設定) ---
st.set_page_config(
    page_title="Foresight 88 | Tempo Intelligence",
    page_icon="⏳",
    layout="wide"
)

# 自定義 CSS 讓介面更有質感 (隱藏預設選單，加入品牌色)
st.markdown("""
<style>
    .reportview-container {
        background: #0e1117;
    }
    .main .block-container {
        padding-top: 2rem;
    }
    h1 {
        color: #C5A059; /* Foresight Gold */
    }
    h3 {
        color: #E0E0E0;
    }
    .stSlider [data-baseweb="slider"] {
        color: #C5A059;
    }
</style>
""", unsafe_allow_html=True)

# 標題區
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("# ⏳") # 這裡可以之後換成妳的 Logo 圖片
with col2:
    st.title("Foresight 88 Intelligence")
    st.markdown("**Tempo Economics™ Simulation Engine | v1.0 Alpha**")

st.markdown("---")

# 建立分頁
tab1, tab2 = st.tabs(["🌍 National Sovereignty (Macro)", "🧠 Leader's Biological Tempo (Micro)"])

# ==========================================
# TAB 1: 國家宏觀模擬 (The Macro Simulator)
# ==========================================
with tab1:
    st.sidebar.header("🎛️ Macro Controls")
    
    # 1. 選擇情境
    scenario = st.sidebar.selectbox(
        "Select Jurisdiction Context",
        ["Abu Dhabi (Vision 2030) 🇦🇪", "Singapore (Smart Nation) 🇸🇬", "Japan (Stagnation) 🇯🇵", "South Korea (Crisis) 🇰🇷"]
    )
    
    st.sidebar.markdown("---")
    
    # 2. 預設參數 (根據不同國家載入不同數值)
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

    st.subheader(f"Scenario Analysis: {scenario}")
    st.info(desc)

    # 3. 互動滑桿 (讓客戶自己玩)
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        target_growth = st.slider("Target GDP Growth (%)", 0.0, 10.0, default_growth)
    with col_b:
        tempo_stress = st.slider("Systemic Acceleration (Stress)", 0, 100, default_stress)
    with col_c:
        human_resilience = st.slider("Human Capital Resilience", 0, 100, default_resilience)

    # 4. 運算核心 (GHDP Algorithm)
    years = np.arange(2025, 2036)
    n_years = len(years)
    
    # GDP (指數增長幻覺)
    gdp = [100 * ((1 + target_growth/100) ** i) for i in range(n_years)]
    
    # GHDP (考慮人類磨損的真實產出)
    # 邏輯：當 壓力 > 韌性，人類資產開始「折舊」
    friction_gap = max(0, (tempo_stress - human_resilience))
    decay_rate = friction_gap * 0.005 # 係數
    
    ghdp = []
    current_val = 100
    for i in range(n_years):
        # 隨著時間推移，疲勞是累積的 (Compound Fatigue)
        cumulative_drag = (decay_rate * i * i) 
        val = gdp[i] * (1 - cumulative_drag)
        ghdp.append(val)

    # 5. 繪製圖表 (Matplotlib)
    fig, ax = plt.subplots(figsize=(10, 4))
    # 設定背景色以符合 Foresight 風格
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')
    
    ax.plot(years, gdp, color='#FF4B4B', linestyle='--', label='Traditional GDP (Nominal)', linewidth=2)
    ax.plot(years, ghdp, color='#C5A059', label='Real GHDP (Human-Adjusted)', linewidth=3)
    
    # 圖表美化
    ax.set_title("The Sovereignty Gap (2025-2035)", color='white', fontsize=12)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.legend(facecolor='#0e1117', labelcolor='white')
    ax.grid(color='#444444', linestyle=':', linewidth=0.5)
    
    # 移除邊框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')

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
# TAB 2: 個人/領袖掃描 (The Micro Scan)
# ==========================================
with tab2:
    st.markdown("### 🧬 The Executive Tempo Audit")
    st.write("Calculates the biological runway of high-stakes decision makers.")
    
    c1, c2 = st.columns(2)
    with c1:
        sleep = st.slider("Average Sleep (Hours)", 4.0, 9.0, 6.0)
        deep_work = st.slider("Uninterrupted Deep Work (Hours/Day)", 0.0, 6.0, 2.0)
    with c2:
        meetings = st.slider("High-Stakes Decisions (Count/Day)", 0, 15, 5)
        digital_noise = st.slider("Screen Time & Notifications (High/Med/Low)", 1, 10, 8)

    st.markdown("---")
    
    # 簡易個人算法
    # 能量輸入 = 睡眠 + 深層工作(心流)
    energy_in = (sleep * 10) + (deep_work * 5)
    # 能量消耗 = 決策疲勞 + 數位噪音
    energy_out = (meetings * 8) + (digital_noise * 5)
    
    balance = energy_in - energy_out
    
    # 視覺化儀表板
    col_res1, col_res2 = st.columns([2, 1])
    
    with col_res1:
        st.write("#### Your Biological Tempo Score")
        # 進度條模擬
        score = 50 + balance
        score = max(0, min(100, score)) # 限制在 0-100
        
        bar_color = "red" if score < 40 else "gold" if score < 80 else "green"
        st.progress(int(score))
        st.caption(f"Score: {int(score)}/100")
        
        if score < 40:
            st.error("**CRITICAL BURNOUT RISK**: Cognitive functions are degrading. Judgment error probability: HIGH.")
        elif score < 70:
            st.warning("**SUB-OPTIMAL**: You are running on adrenaline, not energy. Sustainability: < 12 months.")
        else:
            st.success("**PEAK PERFORMANCE**: You are operating in a sovereign rhythm.")

    with col_res2:
        st.write("#### Prescription")
        if score < 60:
            st.markdown("- 📉 **Cut Decisions by 30%**")
            st.markdown("- 🛌 **Sleep +1 Hour**")
            st.markdown("- 📵 **Digital Detox Protocol**")
        else:
            st.markdown("- ✨ **Maintain Rhythm**")
            st.markdown("- 🚀 **Scale Intensity**")
