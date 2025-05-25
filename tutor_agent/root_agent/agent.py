from google.adk.agents import Agent 
from google.adk.tools.agent_tool import AgentTool

# Sub-agents
from .sub_agent.math_agent import math_agent
from .sub_agent.physics_agent import physics_agent
from .sub_agent.chemistry_agent import chemistry_agent
from .sub_agent.general_agent import general_agent

# Tools
from .tools.calculator import calculator_tool
from .tools.constants import physics_constants_tool
from .tools.chemistry import chemistry_lookup

root_agent = Agent(
    name='root_agent',
    model='gemini-2.0-flash-001',
    description='Main Tutor Agent that routes queries to the appropriate specialist agent.',
    instruction="""
        You are a tutor agent responsible for overseeing the work of the other agents.

        You must always delegate the task to the appropriate agent or use a tool based on the query type.

        You are responsible for delegating tasks to the following agents: 
        - math_agent
        - physics_agent
        - chemistry_agent

        You also have access to the following tools:
        - google_search (for general knowledge, current events, or if no specific agent is appropriate)
        Rules:
        - If a query relates to math, send it to math_agent.
        - If a query relates to physics, send it to physics_agent.
        - If a query relates to chemistry, send it to chemistry_agent.
        - If the query is not related to any of the above (e.g., general knowledge, history, geography, how-to queries), ALWAYS use the google_search tool.
        - If you're unsure which agent or tool to use, default to google_search.

        Maintain conversation history for context.
        If the query is ambiguous or unclear, ask for clarification.
        """,
    tools=[
        AgentTool(general_agent),
        calculator_tool,
        physics_constants_tool,
        chemistry_lookup
        ], 
    sub_agents=[math_agent, physics_agent, chemistry_agent]
)
