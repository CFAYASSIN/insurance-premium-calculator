
import streamlit as st

st.set_page_config(
    page_title="Ngacha Insurance Calculator",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Ngacha Insurance")
st.subheader("Insurance Premium Calculator")

st.write(
    "Calculate total premiums collected "
    "and the balance after paying claims."
)

st.divider()

# Input details
number_of_customers = st.number_input(
    "Number of customers",
    min_value=0,
    value=50,
    step=1
)

premium_per_customer = st.number_input(
    "Premium per customer (TSh)",
    min_value=0,
    value=20000,
    step=1000
)

total_claim_paid = st.number_input(
    "Total claims paid (TSh)",
    min_value=0,
    value=600000,
    step=10000
)

# Calculate
if st.button("Calculate", type="primary"):

    total_premium_collected = (
        number_of_customers * premium_per_customer
    )

    balance_after_claims = (
        total_premium_collected - total_claim_paid
    )

    st.divider()
    st.subheader("Calculation Results")

    st.metric(
        "Total Premiums Collected",
        f"TSh {total_premium_collected:,.0f}"
    )

    st.metric(
        "Total Claims Paid",
        f"TSh {total_claim_paid:,.0f}"
    )

    st.metric(
        "Balance After Claims",
        f"TSh {balance_after_claims:,.0f}"
    )

    if balance_after_claims >= 0:
        st.success("Premiums collected cover the claims paid.")
    else:
        st.warning("Claims paid exceed premiums collected.")

st.caption(
    "Note: This is a basic calculation. "
    "Other expenses and insurance liabilities are excluded."
)
