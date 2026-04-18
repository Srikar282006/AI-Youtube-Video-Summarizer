import streamlit as st
from youtube import build_youtube_agent

st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout="centered"
)

st.title("📽️ AI Youtube Video Analyzer")

def get_agent():
    return build_youtube_agent()

agent = get_agent()

# Input
video_url = st.text_input("Enter your Youtube Video URL")

button = st.button("Analyze Video")

if video_url and button:
    with st.spinner("Analyzing video..."):
        try:
            response = agent.run(
                f"Analyze this video: {video_url}"
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")

    st.markdown("Analysis Report of Video")
    st.markdown(response.content)