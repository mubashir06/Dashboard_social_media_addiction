import streamlit as st
import plotly.express as px

from utils.load_data import load_data
from utils.sidebar import sidebar_filters


st.set_page_config(

    page_title="Teen Mental Health Dashboard",
    page_icon="📊",
    layout="wide"

)

COLORS = {

    "social":"#3B82F6",
    "mental":"#EF4444",
    "sleep":"#8B5CF6",
    "activity":"#10B981",
    "academic":"#F59E0B",
    "neutral":"#64748B"

}
# ======================
# LOAD DATA
# ======================

df=load_data()

df=sidebar_filters(df)


# ======================
# TITLE
# ======================

st.title(
    "Impact of Social Media Usage on Teen Mental Health and Lifestyle"
)

st.markdown(
"""
This dashboard explores patterns between social media behavior,
mental health, sleep patterns, physical activity,
and academic performance among teenagers aged 13–19.
"""
)

st.markdown("---")


# ======================
# KPI SECTION
# ======================

st.subheader(
    "Key Indicators"
)

c1,c2,c3,c4=st.columns(4)

with c1:

    st.metric(
        "Avg Social Media Hours",
        round(df['daily_social_media_hours'].mean(),2)
    )

with c2:

    avg_sleep=round(df['sleep_hours'].mean(),2)

    if avg_sleep >= 8:
        st.success(f"Sleep Hours: {avg_sleep}")

    else:
        st.warning(f"Sleep Hours: {avg_sleep}")

with c3:

    st.metric(
        "Mental Health Score",
        round(df['mental_health_score'].mean(),2)
    )

with c4:

    depression_rate=round(
        (
            len(df[df['depression_status']=="Depression Risk"])
            /len(df)
        )*100,
        2
    )

    if depression_rate < 20:

        st.success(
            f"Depression Risk: {depression_rate}%"
        )

    elif depression_rate < 40:

        st.warning(
            f"Depression Risk: {depression_rate}%"
        )

    else:

        st.error(
            f"Depression Risk: {depression_rate}%"
        )



st.markdown("---")


# ======================
# DEMOGRAPHICS
# ======================

st.subheader(
    "Teen Demographics"
)


c1,c2=st.columns(2)


with c1:

    fig=px.histogram(

        df,

        x='age',

        title='Age Distribution'

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


with c2:

    gender_counts = df['gender'].value_counts()

    fig = px.pie(

        values=gender_counts.values,

        names=gender_counts.index,

        hole=0.55,

        title="Gender Distribution"

    )

    fig.update_traces(

        textposition='inside',

        textinfo='percent+label',

        pull=[0.03]*len(gender_counts)

    )

    fig.update_layout(

        legend_title="Gender",

        title_x=0.25

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ======================
# SOCIAL MEDIA BEHAVIOR
# ======================

st.subheader(
    "Social Media Behavior"
)


c1,c2=st.columns(2)


with c1:

    platform=df[
    'platform_usage'
    ].value_counts()


    fig=px.bar(

        x=platform.values,

        y=platform.index,

        orientation='h',

        title='Most Used Platforms'

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


with c2:

    fig=px.histogram(

    df,

    x='daily_social_media_hours',

    nbins=20,

    color_discrete_sequence=[
        COLORS['social']
    ],

    title='Daily Social Media Usage'

)

    fig.add_vline(

        x=df['daily_social_media_hours'].mean(),

        line_color="red",

        annotation_text="Mean"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================
# USER TYPES
# ======================

st.subheader(
    "Teen User Categories"
)


category=df[
'user_category'
].value_counts()


fig=px.bar(

x=category.index,

y=category.values,

color=category.index,

title='User Categories'

)


st.plotly_chart(
fig,
use_container_width=True
)

st.subheader(
    "Mental Health Risk Distribution"
)

fig=px.histogram(

    df,

    x='mental_health_status',

    color='mental_health_status',

    title='Mental Health Status Distribution',

    color_discrete_map={

        "Low Risk":"green",

        "Moderate Risk":"orange",

        "High Risk":"red"

    }

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")


st.info(

"""
Dashboard Purpose:

Identify social media usage patterns and provide
a foundation for deeper hypothesis testing
in the Analysis section.

"""
)