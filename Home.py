import streamlit as st
from utilities import test
from tools.utility import test2
from datetime import datetime


# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Meri Sehat Analytics",
    page_icon="🩺",
    
)

# --- HEADER ---
st.title("🩺 Meri Sehat – Analytics Platform")
st.markdown("### Empowering healthcare decisions through intelligent insights")

st.markdown("---")

# --- INTRO SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(
    """
    <div style="background-color:#f8f9fa; padding:20px 30px; border-radius:12px;">
        <h2 style="color:#004aad;">Welcome to Meri Sehat Analytics 📊</h2>
        <p>This platform empowers healthcare decision-making through real-time insights and data intelligence.</p>
    </div>
    """,
    unsafe_allow_html=True
)
    st.markdown(
        """


        #### 🎯 Purpose:
        - Track performance of **AI Health Scan**, **Online Consultations**, and **Field Activations**
        - Measure **Customer Engagement**, **Doctor Utilization**, and **Operational Efficiency**
        - Provide leadership with real-time insights for faster, data-driven decisions

        #### 💡 How to Use:
        - Use the **sidebar** to navigate between sections  
          → *Care-Connect, GLP-Campaign, Orders, Customers, Operations, Financials, and more*  
        - Each page is designed to highlight specific business KPIs  

        ---
        """
    )

with col2:
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/2966/2966480.png" width="250">
            <p style="font-size:14px; color:gray;">AI-driven Health Insights</p>
        </div>
        """,
        unsafe_allow_html=True
    )
# --- FOOTER ---
st.markdown(
    f"""
    #### 🕒 Last Updated: {datetime.now().strftime('%d %b %Y, %I:%M %p')}
    ---
    **Developed by:** Meri Sehat Data & Strategy Team  
    **Version:** 1.0.1
    """
) 

test()
test2()
