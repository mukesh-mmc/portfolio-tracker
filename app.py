import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import backend

st.set_page_config(page_title="Portfolio Tracker", layout="wide")

st.title("📊 Mutual Fund Portfolio Tracker")

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "df" not in st.session_state:
    st.session_state.df = None

if "file_data" not in st.session_state:
    st.session_state.file_data = None

# -----------------------------
# REFRESH NAV BUTTON
# -----------------------------
if st.button("🔄 Refresh NAV"):
    backend._nav_history_cache.clear()
    backend._nav_latest_cache.clear()
    st.success("NAV cache cleared. Please click 'Run Portfolio Update'")

# -----------------------------
# FILE UPLOAD
# -----------------------------
uploaded_file = st.file_uploader("Upload your portfolio Excel file", type=["xlsx"])

if uploaded_file:
    # Save uploaded file temporarily
    with open("temp.xlsx", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # -----------------------------
    # RUN PORTFOLIO BUTTON
    # -----------------------------
    if st.button("Run Portfolio Update"):
        with st.spinner("Processing..."):
            df = backend.run_portfolio("temp.xlsx")

        # Save to session state
        st.session_state.df = df

        # Save file bytes for download
        with open("temp.xlsx", "rb") as f:
            st.session_state.file_data = f.read()

        st.success("Portfolio Updated Successfully!")

# -----------------------------
# DISPLAY RESULTS (PERSISTENT)
# -----------------------------
if st.session_state.df is not None:
    df = st.session_state.df

    # Remove TOTAL row for charts
    chart_df = df[df["Scheme Name"] != "TOTAL"]

    # -----------------------------
    # METRICS
    # -----------------------------
    if "TOTAL" in df["Scheme Name"].values:
        total_row = df[df["Scheme Name"] == "TOTAL"].iloc[0]

        st.header("📈 Key Portfolio Metrics")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Portfolio Value", f"₹{total_row['Current Value (₹)']:.2f}")

        col2.metric(
            "Daily Change",
            f"₹{total_row['Daily Change (₹)']:.2f}",
            delta=f"{total_row['Daily Change (%)']:.2f}%",
            delta_color=("inverse" if total_row['Daily Change (₹)'] > 0 else "normal")
        )

        col3.metric("Total Returns", f"₹{total_row['Total Return (₹)']:.2f}")

        if total_row["XIRR (%)"] is not None:
            col4.metric("Portfolio XIRR", f"{total_row['XIRR (%)']:.2f}%")

    # -----------------------------
    # TABLE
    # -----------------------------
    st.subheader("📋 Portfolio Summary")
    st.dataframe(df, use_container_width=True)

    # -----------------------------
    # PIE CHART
    # -----------------------------
    st.subheader("🥧 Portfolio Allocation")

    fig1, ax1 = plt.subplots()
    ax1.pie(
        chart_df["Current Value (₹)"],
        labels=chart_df["Scheme Name"],
        autopct="%1.1f%%"
    )
    ax1.set_title("Allocation by Scheme")

    st.pyplot(fig1)

    # -----------------------------
    # BAR CHART
    # -----------------------------
    st.subheader("📊 Scheme-wise XIRR (%)")

    fig2, ax2 = plt.subplots()
    ax2.bar(
        chart_df["Scheme Name"],
        chart_df["XIRR (%)"]
    )
    ax2.set_ylabel("XIRR (%)")
    ax2.set_title("Returns by Scheme")

    plt.xticks(rotation=45, ha="right")

    st.pyplot(fig2)

    # -----------------------------
    # DOWNLOAD BUTTON (FIXED)
    # -----------------------------
    if st.session_state.file_data is not None:
        st.download_button(
            label="📥 Download Updated File",
            data=st.session_state.file_data,
            file_name="portfolio_updated.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
