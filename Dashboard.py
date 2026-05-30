import streamlit as st
import plotly.express as px

from utils.load_data import load_data
from utils.sidebar import sidebar_filters


st.set_page_config(

    page_title="Teen Mental Health Dashboard",
    page_icon="📊",
    layout="wide"

)


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

        "Average Social Media Hours",

        round(
            df[
            'daily_social_media_hours'
            ].mean(),
            2
        )

    )


with c2:

    st.metric(

        "Average Sleep Hours",

        round(
            df[
            'sleep_hours'
            ].mean(),
            2
        )

    )


with c3:

    st.metric(

        "Average Mental Health Score",

        round(
            df[
            'mental_health_score'
            ].mean(),
            2
        )

    )


with c4:

    depression_rate=round(

    (

    len(

    df[
    df[
    'depression_status'
    ]
    ==
    'Depression Risk'
    ]

    )

    /

    len(df)

    )*100

    ,

    2

    )


    st.metric(

        "Depression Risk %",

        f"{depression_rate}%"

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

    fig=px.pie(

        df,

        names='gender',

        hole=.5,

        title='Gender Distribution'

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

        title='Daily Social Media Usage'

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


st.markdown("---")


st.info(

"""
Dashboard Purpose:

Identify social media usage patterns and provide
a foundation for deeper hypothesis testing
in the Analysis section.

"""
)