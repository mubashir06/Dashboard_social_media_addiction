import streamlit as st


def sidebar_filters(df):


    st.sidebar.title(
        "Filters"
    )

    st.sidebar.markdown("---")


    gender=st.sidebar.multiselect(

        "Gender",

        options=df[
            'gender'
        ].unique(),

        default=df[
            'gender'
        ].unique()

    )


    age=st.sidebar.slider(

        "Age Range",

        min_value=int(
            df['age'].min()
        ),

        max_value=int(
            df['age'].max()
        ),

        value=(

            int(
                df['age'].min()
            ),

            int(
                df['age'].max()
            )

        )

    )


    user_category=st.sidebar.multiselect(

        "User Category",

        options=df[
            'user_category'
        ].unique(),

        default=df[
            'user_category'
        ].unique()

    )


    mental=st.sidebar.multiselect(

        "Mental Status",

        options=df[
            'mental_health_status'
        ].unique(),

        default=df[
            'mental_health_status'
        ].unique()

    )


    filtered_df=df[

        (df['gender'].isin(gender))

        &

        (df['age'].between(

            age[0],
            age[1]

        ))

        &

        (df['user_category'].isin(
            user_category
        ))

        &

        (df['mental_health_status'].isin(
            mental
        ))

    ]


    st.sidebar.markdown("---")

 

    return filtered_df