from textwrap import dedent
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.youtube import YouTubeTools
from agno.models.groq import Groq

load_dotenv()

def build_youtube_agent():

    return Agent(
    name="YouTube Agent",
    model=Groq(id="Enter your model"),
    tools=[YouTubeTools()],
    instructions=dedent("""\
You are a YouTube video analyst.

IMPORTANT RULES:
- You MUST use the YouTube tool to fetch video data first
- Always pass ONLY a valid YouTube URL
- Do NOT modify the URL format
- Do NOT call functions manually

Workflow:
1. Use YouTube tool to fetch video content
2. Analyze returned transcript
3. Summarize into structured sections

Output format:
- Overview
- Timestamped sections
- Key takeaways

Keep output concise.
"""),
    markdown=True,

)

# Example usage with different types of videos
# youtube_agent.print_response(
#     "Analyze this video: https://www.youtube.com/watch?v=zjkBMFhNj_g",
#     stream=True,
# )
