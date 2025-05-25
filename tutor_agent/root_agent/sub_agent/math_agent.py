from google.adk.agents import Agent
from ..tools.calculator import calculator_tool 
from google.adk.tools.agent_tool import AgentTool

math_agent = Agent(
    name="math_agent",
    model="gemini-2.0-flash",
    description="Specialist in mathematical problem solving",
    instruction="""
    You are an expert mathematician. Your tasks:
    1. Parse mathematical queries
    2. Use calculator_tool for computations
    3. Provide step-by-step solutions
    4. Verify answers with calculations
    
    Always:
    - Show working steps
    - Validate results with calculator_tool
    - Use LaTeX for equations: \sqrt{x^2 + y^2}
    
    If the user asks about anything else,
     then delegate to the tutor agent.
    """,
    tools=[
        calculator_tool
        ]
)
