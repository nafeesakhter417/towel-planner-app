import streamlit as st
import pandas as pd

# --- TOWEL LOGIC (Hidden Formulas) ---
def calculate_towel_weight(l, w, gsm, pile_ratio):
    # Area in square meters
    area = (l * 0.0254) * (w * 0.0254)
    total_weight = area * gsm
    # Pile vs Ground distribution
    pile = total_weight * (pile_ratio / (pile_ratio + 1))
    ground = total_weight - pile
    return round(total_weight, 2), round(pile, 2), round(ground, 2)

# --- WEB INTERFACE ---
st.set_page_config(page_title="Towel Planner Pro", layout="wide")
st.title("📊 Professional Towel Planning Dashboard")

# Sidebar for Input
with st.sidebar:
    st.header("🛠 Order Entry")
    po_no = st.text_input("PO Number", "PO-2026-001")
    towel_size_l = st.number_input("Length (Inches)", value=54)
    towel_size_w = st.number_input("Width (Inches)", value=27)
    target_gsm = st.number_input("Target GSM", value=500)
    p_ratio = st.slider("Pile Ratio (1:X)", 2.0, 10.0, 6.5)
    
    submit = st.button("Calculate & Plan")

# Calculation Execution
total, p_wt, g_wt = calculate_towel_weight(towel_size_l, towel_size_w, target_gsm, p_ratio)

# Main Dashboard Layout (Like your image)
col1, col2, col3, col4 = st.columns(4)
col1.metric("TOTAL WEIGHT", f"{total}g")
col2.metric("PILE YARN", f"{p_wt}g")
col3.metric("GROUND YARN", f"{g_wt}g")
col4.metric("STATUS", "Active")

st.markdown("---")

# Production Table
st.subheader(f"Loom Status - {po_no}")
df = pd.DataFrame({
    'Loom No': [101, 102, 105],
    'Size': [f"{towel_size_l}x{towel_size_w}"] * 3,
    'Total Pcs': [2000, 2000, 2000],
    'Weaved': [500, 1200, 0],
    'Balance': [1500, 800, 2000],
    'Finish Date': ['2026-04-15', '2026-04-10', '2026-04-25'],
    'Status': ['Running', 'Running', 'Late']
})

# Display Table with colors
st.table(df)
