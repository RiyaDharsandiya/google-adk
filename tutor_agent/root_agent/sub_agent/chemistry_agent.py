from google.adk.agents import Agent
from ..tools.chemistry import chemistry_lookup

chemistry_agent = Agent(  # Bonus agent
    name='chemistry_agent',
    model='gemini-2.0-pro',
    description='Expert in chemistry. Can explain concepts and look up elements.',
    instruction="""
    You are a chemistry tutor. If the query asks about an element, use the chemistry_lookup tool.
    For other chemistry questions, provide explanations.
    
    If the user asks about anything else,
    then delegate to the tutor agent.
    """,
    tools=[chemistry_lookup]
)