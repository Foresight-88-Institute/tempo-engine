# ==========================================
# v3.2-RA Research Appendix Build
# Parameters Frozen | Reviewer-Safe
# Foresight 88 Institute | Tempo Intelligence
# ==========================================

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------
# 0. Page Config
# ------------------------------------------
st.set_page_config(
    page_title="Foresight 88 | Tempo Intelligence — Research Appendix",
    page_icon="⏳",
    layout="wide"
)

# ------------------------------------------
# 1. Styling (Static, Non-reactive)
# ------------------------------------------
st.markdown("""
<style>
h1 { color: #C5A059 !important; }
.stTabs [data-baseweb="tab-list"] { gap: 24px; }
.stTabs [aria-selected="true"] {
    border-bottom: 2px solid #C5A059;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------
# 2. Header
# ------------------------------------------
st.title("Foresight 88 | Tempo Intelligence")
st.markdown("**Research Appendix Edition — v3.2 (Parameters Frozen)**")
st.caption(
    "This appendix presents a deterministic simulation for structural reasoning only. "
    "No interactive tuning is permitted in this build."
)
st.markdown("---")

# ------------------------------------------
# 3. Scenario Registry (FROZEN)
# ------------------------------------------
SCENARIOS = {
    "Abu Dhabi — Vision 2030 (High Buffer)": {
        "growth": 5.5,
        "stress": 45,
        "resilience": 85,
        "desc": "High resource buffer with tempo-setting optionality."
    },
    "Singapore — Smart Nation (Optimization Ceiling)": {
        "growth": 3.5,
        "stress": 70,
        "resilience": 75,
        "desc": "Peak efficiency regime with limited recovery slack."
    },
    "Japan — Structural Stagnation": {
        "growth": 1.2,
        "stress": 65,
        "resilience": 40,
        "desc": "Low volatility equilibrium with embedded fatigue."
    },
    "South Korea — Acceleration Crisis": {
        "growth": 2.5,
        "stress": 90,
        "resilience": 30,
        "desc": "Tempo misalignment exceeds biological limits."
    }
}

# ------------------------------------------
# 4. Scenario Selection (Discrete Only)
# ------------------------------------------
scenario_name = st.selectbox(
    "Select Reference Jurisdiction (Discrete Scenario)",
    list(SCENARIOS.keys())
)

params = SCENARIOS[scenario_name]

st.info(f"**Context Note**: {params['desc']}")

# ------------------------------------------
# 5. Macro Engine (FROZEN LOGIC)
# ------------------------------------------
years = np.arange(2025, 2036)
n = len(years)

target_growth = params["growth"]
tempo_stress = params["stress"]
human_resilience = params["resilience"]

gdp = [100 * ((1 + target_growth / 100) ** i) for i in range(n)]

growth_pressure = target_growth / 10
effective_resilience = human_resilience * (1 - growth_pressure * 0.5)
tempo_misalignment = max(0, (tempo_stress - effective_resilience) / 100)

ghdp = []
for i in range(n):
    oscillation = np.sin(i / 1.5) * tempo_misalignment * 0.12
    policy_relief = 0.08 if i > 0 and i % 4 == 0 else 0
    irreversible_drag = tempo_misalignment * 0.02 * (i ** 1.5)

    adjusted = max(0, 1 - irreversible_drag + oscillation + policy_relief)
    ghdp.append(gdp[i] * adjusted)

capacity_ratio = np.array(ghdp) / np.array(gdp)

# ------------------------------------------
# 6. Visualization — Sovereignty Gap
# ------------------------------------------
st.subheader("I. Sovereignty Gap Trajectory (2025–2035)")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(years, gdp, linestyle="--", linewidth=2, label="Systemic Velocity (GDP)")
ax.plot(years, ghdp, linewidth=3, label="Biological Capacity (GHDP)")
ax.set_title("The Cost of Unsynchronized Acceleration", fontsize=11)
ax.legend()
ax.grid(alpha=0.3)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
st.pyplot(fig)

# ------------------------------------------
# 7. Synchronization Ratio
# ------------------------------------------
st.subheader("II. Biological Synchronization Ratio")

fig2, ax2 = plt.subplots(figsize=(10, 2.5))
ax2.plot(years, capacity_ratio, linewidth=2)
ax2.axhline(1, linestyle="--", alpha=0.5)
ax2.set_ylim(0, 1.1)
ax2.set_ylabel("GHDP / GDP")
ax2.grid(alpha=0.3)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
st.pyplot(fig2)

# ------------------------------------------
# 8. Diagnostic Summary (Static)
# ------------------------------------------
final_gap = gdp[-1] - ghdp[-1]

c1, c2, c3 = st.columns(3)
c1.metric("2035 GDP Index", f"{int(gdp[-1])}")
c2.metric("2035 GHDP Index", f"{int(ghdp[-1])}")
c3.metric("Sovereignty Gap", f"-{int(final_gap)}")

if tempo_misalignment > 0.4:
    st.error(
        "SYSTEM FAILURE: Growth targets cannibalize resilience. "
        "Acceleration exceeds biological absorption capacity."
    )
elif tempo_misalignment > 0.1:
    st.warning(
        "STRUCTURAL DRAG: Persistent friction emerges under sustained acceleration."
    )
else:
    st.success(
        "SYNCHRONIZED REGIME: Growth velocity remains metabolizable."
    )

# ------------------------------------------
# 9. Research Boundary Statement
# ------------------------------------------
st.markdown("---")
with st.expander("📎 Research Boundary & Reviewer Notes"):
    st.markdown("""
**Scope Statement**

This appendix presents a deterministic causal sandbox designed for:
- Structural reasoning
- Stress-testing assumptions
- Visualizing non-linear capacity erosion

It is **not**:
- A forecasting model
- An econometric estimator
- A policy prescription tool

Parameters are intentionally frozen to prevent overfitting and false precision.

**Core Question Only**  
*At what point does acceleration stop compounding — and start consuming sovereignty?*
""")

st.caption("© 2025 Foresight 88 Institute · Research Appendix Edition")
