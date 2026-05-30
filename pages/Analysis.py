import streamlit as st
import plotly.express as px
from scipy.stats import pearsonr
import pandas as pd

from utils.load_data import load_data
from utils.sidebar import sidebar_filters


st.set_page_config(

    page_title="Analysis",
    page_icon="📈",
    layout="wide"

)


# ======================
# LOAD DATA
# ======================

df=load_data()

df=sidebar_filters(df)


st.title(
    "Hypothesis Analysis (H1–H5)"
)

st.markdown("""
This section investigates relationships between
social media usage and teen wellbeing using
descriptive and diagnostic analytics.
""")

st.markdown("---")


# ===================================
# H1
# Social media → sleep
# ===================================

st.subheader(
"📈 H1: Social media usage vs sleep duration"
)

r,p=pearsonr(

df['daily_social_media_hours'],
df['sleep_hours']

)


fig=px.scatter(

df,

x='daily_social_media_hours',

y='sleep_hours',

trendline='ols',

title='Daily Social Media Hours vs Sleep Hours'

)

st.plotly_chart(
fig,
use_container_width=True
)

c1,c2=st.columns(2)

with c1:

    st.metric(
        "Correlation (r)",
        round(r,3)
    )


with c2:

    st.metric(
        "P-value",
        round(p,5)
    )


st.warning(
"""
Finding:

A very weak negative relationship was observed between social media usage
and sleep duration (r = -0.009, p = 0.743).

Although the relationship follows the expected direction,
the effect size is extremely small and statistically insignificant.

This suggests that social media usage alone does not appear to meaningfully
explain changes in sleep duration among teenagers in this dataset.

Conclusion:

❌ Hypothesis H1 is not supported.
"""
)

st.markdown("---")



# ===================================
# H2
# Social media → stress
# ===================================

st.subheader(
"📈 H2: Social media usage vs stress"
)

r,p=pearsonr(

df['daily_social_media_hours'],
df['stress_level']

)


fig=px.scatter(

df,

x='daily_social_media_hours',

y='stress_level',

trendline='ols',

title='Daily Social Media Hours vs Stress Level'

)

st.plotly_chart(
fig,
use_container_width=True
)

c1,c2=st.columns(2)

with c1:

    st.metric(
        "Correlation (r)",
        round(r,3)
    )


with c2:

    st.metric(
        "P-value",
        round(p,5)
    )


st.warning(
"""
Finding:

A very weak positive relationship was observed between social media usage
and stress level (r = 0.031, p = 0.288).

The relationship is not statistically significant.

Results suggest insufficient evidence that increased social media usage
directly influences stress levels in this dataset.

Conclusion:

❌ Hypothesis H2 is not supported.
"""
)

st.markdown("---")



# ===================================
# H3
# Addiction → depression
# ===================================

st.subheader(
"📈 H3: Addiction level vs depression risk"
)


depression_group=df.groupby(
'addiction_level'
)['depression_label'].mean().reset_index()


fig=px.bar(

depression_group,

x='addiction_level',

y='depression_label',

title='Depression Probability by Addiction Level'

)

st.plotly_chart(
fig,
use_container_width=True
)


st.info(
"""
Finding:

Depression probability shows a tendency to increase at
higher addiction levels, although the pattern is not
completely consistent across all groups.

Teenagers with stronger addiction tendencies appear more likely
to demonstrate elevated depression risk.

Conclusion:

🟡 Hypothesis H3 is partially supported.
"""
)

st.markdown("---")



# ===================================
# H4
# User category → academics
# ===================================

st.subheader(
"📈 H4: User category vs academic performance"
)


fig=px.box(

df,

x='user_category',

y='academic_performance',

title='Academic Performance by User Category'

)

st.plotly_chart(
fig,
use_container_width=True
)


st.warning(
"""
Finding:

Academic performance distributions appear very similar
across heavy, moderate, and low user groups.

Considerable overlap exists between categories,
and no strong decline in academic performance
is visible among heavy users.

Conclusion:

❌ Hypothesis H4 is not supported.
"""
)

st.markdown("---")



# ===================================
# H5
# Activity + screen exposure
# ===================================

st.subheader(
"📈 H5: Activity and screen exposure vs mental health"
)


fig=px.scatter(

df,

x='physical_activity',

y='screen_time_before_sleep',

size='mental_health_score',

color='mental_health_score',

title='Physical Activity and Screen Exposure'

)

st.plotly_chart(
fig,
use_container_width=True
)


st.warning(
"""
Finding:

No strong visual pattern was observed between
physical activity, screen exposure, and mental wellbeing.

The observations appear widely dispersed,
suggesting additional variables may contribute
to mental health outcomes.

Conclusion:

🟡 Hypothesis H5 receives limited support.
"""
)

st.markdown("---")



# ===================================
# HYPOTHESIS SUMMARY
# ===================================

st.subheader(
"Hypothesis Summary"
)


summary=pd.DataFrame({

"Hypothesis":[
"H1",
"H2",
"H3",
"H4",
"H5"
],

"Decision":[
"Not Supported",
"Not Supported",
"Partially Supported",
"Not Supported",
"Limited Support"
]

})


st.dataframe(

summary,

use_container_width=True

)