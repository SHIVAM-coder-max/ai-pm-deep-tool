import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI PM Deep Tool", layout="wide")

st.title("🚀 AI Product Manager - Deep Version")

api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

if api_key:

    client = OpenAI(api_key=api_key)

    tool = st.sidebar.selectbox(
        "Choose PM Tool",
        [
            "Idea Validator",
            "Market Research",
            "Product Expansion",
            "Feature Prioritization (RICE)"
        ]
    )

    user_input = st.text_area("Enter Product / Feature Info")

    if tool == "Feature Prioritization (RICE)":
        reach = st.number_input("Reach", min_value=1)
        impact = st.number_input("Impact (1-5)", min_value=1, max_value=5)
        confidence = st.number_input("Confidence (0.1-1.0)", min_value=0.1, max_value=1.0)
        effort = st.number_input("Effort", min_value=1)

        if st.button("Calculate RICE Score"):
            score = (reach * impact * confidence) / effort
            st.success(f"RICE Score: {score}")

    else:

        if st.button("Generate Analysis"):

            if tool == "Idea Validator":
                prompt = f"""
                Act as Senior Product Manager.

                Analyze this idea deeply:
                {user_input}

                Give:
                - Target Users
                - Problem Statement
                - Market Opportunity
                - Risks
                - Suggestions
                """

            elif tool == "Market Research":
                prompt = f"""
                Conduct structured market research for:
                {user_input}

                Include:
                - Market Size Logic (TAM/SAM/SOM reasoning)
                - Competitors
                - User Pain Points
                - Trends (3-5 years)
                - Gaps in Market
                """

            elif tool == "Product Expansion":
                prompt = f"""
                Suggest new product or feature expansion ideas for:
                {user_input}

                Include:
                - Adjacent markets
                - Monetization models
                - AI opportunities
                - Revenue impact logic
                """

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            st.subheader("AI Output")
            st.write(response.choices[0].message.content)

else:
    st.warning("Enter OpenAI API Key to continue.")