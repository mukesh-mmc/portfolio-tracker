import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import backend

st.set_page_config(page_title="Portfolio Tracker", layout="wide")

st.title("📊 Mutual Fund Portfolio Tracker")

# ✅ NEW: Refresh NAV button
if st.button("🔄 Refresh NAV"):
    backend._nav_history_cache.clear()
    backend._nav_latest_cache.clear()
    st.success("NAV cache cleared. Please click 'Run Portfolio Update'")

uploaded_file = st.file_uploader("Upload your portfolio Excel file", type=["xlsx"])

if uploaded_file:
    with open("temp.xlsx", "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Run Portfolio Update"):
        with st.spinner("Processing..."):
            df = backend.run_portfolio("temp.xlsx")

        st.success("Portfolio Updated Successfully!")

        # -----------------------------
        # REMOVE TOTAL ROW FOR CHARTS
        # -----------------------------
        chart_df = df[df["Scheme Name"] != "TOTAL"]

        # -----------------------------
        # DISPLAY METRICS
        # -----------------------------
        if "TOTAL" in df["Scheme Name"].values:
            total_row = df[df["Scheme Name"] == "TOTAL"].iloc[0]

            st.header("📈 Key Portfolio Metrics")

            st.metric("Total Portfolio Value", f"₹{total_row['Current Value (₹)']:.2f}")
            st.metric("Daily Change", f"₹{total_row['Daily Change (₹)']:.2f}", 
                      delta=f"{total_row['Daily Change (%)']:.2f}%",
                      delta_color=("inverse" if total_row['Daily Change (₹)'] > 0 else "normal"))
            st.metric("Total Returns", f"₹{total_row['Total Return (₹)']:.2f}")
            if total_row["XIRR (%)"] is not None:
                st.metric("Portfolio XIRR", f"{total_row['XIRR (%)']:.2f}%")

        # -----------------------------
        # SHOW TABLE
        # -----------------------------
        st.subheader("📋 Portfolio Summary")
        st.dataframe(df, use_container_width=True)

        # -----------------------------
        # PIE CHART - ALLOCATION
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
        # BAR CHART - XIRR
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
        # DOWNLOAD BUTTON
        # -----------------------------
        st.download_button(
            label="📥 Download Updated File",
            data=open("temp.xlsx", "rb"),
            file_name="portfolio_updated.xlsx"
        )