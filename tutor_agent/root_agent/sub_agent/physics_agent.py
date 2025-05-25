from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from ..tools.constants import physics_constants_tool  # Adjust import path as needed

physics_agent = Agent(
    model='gemini-2.0-flash-001',
    name='physics_agent',
    description='An expert assistant for physics questions, able to use physical constants for calculations.',
    instruction="""
    You are a physics specialist. Your tasks:
    - Answer user questions about physics concepts, problems, and formulas.
    - When a calculation involves a physical constant (such as speed of light, Planck constant, gravitational constant, etc.), use the physics_constants_tool to retrieve its value.
    - Show all calculation steps clearly.
    - If a constant is not found, politely inform the user.
    
     If the user asks about anything else,
     then delegate to the tutor agent.
    """,
    tools=[
        physics_constants_tool
    ]
)
