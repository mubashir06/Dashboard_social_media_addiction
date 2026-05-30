import streamlit as st

from utils.load_data import load_data
from utils.sidebar import sidebar_filters


st.set_page_config(

    page_title="Recommendations",
    page_icon="🧠",
    layout="wide"

)


df=load_data()

df=sidebar_filters(df)


st.title(
"Recommendations"
)

st.markdown("""
Recommendations based on observed behavioral
patterns and hypothesis analysis.
""")

st.markdown("---")


# ======================
# High Risk Population
# ======================

st.subheader(
"High Risk Indicators"
)


c1,c2,c3=st.columns(3)


with c1:

    high_sleep=len(

        df[
        df[
        'sleep_deficit'
        ]>2
        ]

    )

    st.metric(
        "Sleep Deficit >2 hrs",
        high_sleep
    )


with c2:

    high_addiction=len(

        df[
        df[
        'addiction_level'
        ]>=7
        ]

    )

    st.metric(
        "High Addiction",

        high_addiction
    )


with c3:

    risk=len(

        df[
        df[
        'mental_health_status'
        ]
        ==
        'High Risk'
        ]
    )

    st.metric(
        "High Mental Risk",
        risk
    )


st.markdown("---")


st.subheader(
"Suggested Actions"
)


with st.expander(
"Sleep and Screen Exposure"
):

    st.write(
"""
• Encourage consistent sleep schedules

• Reduce screen time before sleep

• Limit late-night social media exposure
"""
)


with st.expander(
"Physical Activity"
):

    st.write(
"""
• Promote daily activity

• Encourage outdoor/social engagement

• Reduce prolonged sedentary behavior
"""
)


with st.expander(
"Mental Health Monitoring"
):

    st.write(
"""
• Monitor stress and anxiety indicators

• Identify heavy users early

• Support balanced digital habits
"""
)


st.markdown("---")


st.success(
"""
Expected Findings:

• Increased social media usage may reduce sleep

• Heavy users may show higher addiction

• Higher addiction may increase depression risk

• Balanced lifestyle habits may improve wellbeing
"""
)