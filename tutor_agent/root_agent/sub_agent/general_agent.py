from google.adk.agents import Agent
from google.adk.tools import google_search

general_agent = Agent(
    model='gemini-2.0-flash-001',
    name='general_agent',
    description='A helpful assistant for user questions.',
    instruction=(
        "Answer user questions to the best of your knowledge. "
        "For general questions, use the tool google_search to find accurate and up-to-date information."
    ),
    tools=[google_search],  # Assuming the API allows specifying tools
)
