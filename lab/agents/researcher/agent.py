from google.adk.agents import Agent
from google.adk.tools.google_search_tool import google_search


MODEL = "gemini-3-flash-preview"

# The researcher should be an Agent that uses the google_search tool
# and follows the instructions to gather information.

# using Gemini 3, the search tool is automatically availale
# if < 3, you need to pass tools=[google_search] to the Agent constructor
researcher = Agent(
    name="Researcher",
    model=MODEL,
    description="Gathers information using the Google Search",
    instructions="""
    You are an expert researcher. Your goal is to find comprehensive and accurate information on the user's topic.
    Summarize your findings clearly.
    If you receive feedback that your research is insufficient, use the feedback to refine your next search.
    DO NOT output any function calls. Provide your research directly as text.
    """,
)

root_agent = researcher

