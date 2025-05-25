# AI Tutor System

## Project Description

The AI Tutor System is a sophisticated multi-agent application designed to provide intelligent and specialized tutoring assistance across various subjects. Unlike a monolithic AI, this system intelligently routes user queries to specialized "expert" agents, each equipped to handle specific domains like mathematics or physics. Furthermore, these specialist agents can leverage "tools" to provide accurate and detailed responses, mimicking a real-world tutoring experience.

**Core Components:**

* **Tutor Agent (Main Agent):** This serves as the primary interface for the student. It receives natural language queries (e.g., "What is Newton's second law?" or "Can you help me solve 2x + 5 = 11?") and, through intelligent intent recognition (using keyword matching or the Gemini API), delegates the query to the most appropriate specialist sub-agent.
* **Sub-Agents (Specialist Agents):**
    * **Math Agent:** Specialized in answering mathematics-related questions.
    * **Physics Agent:** Specialized in answering physics-related questions.
    Each sub-agent is capable of processing tasks/queries from the Tutor Agent and generating detailed responses using the Gemini API.
* **Tool Usage:**
    * **Calculator Tool (for Math Agent):** A simple arithmetic calculator integrated with the Math Agent, allowing it to perform basic operations (addition, subtraction, multiplication, division) for solving or verifying mathematical problems.
    * **Physics Constants Lookup Tool (for Physics Agent):** A function that allows the Physics Agent to retrieve common physical constants (e.g., speed of light, gravitational constant) from a predefined knowledge base, enhancing its ability to provide accurate answers.

**Agent Communication & Orchestration:**

The Tutor Agent acts as the orchestrator, intelligently routing queries to the chosen sub-agent. Once a sub-agent processes the query (potentially using its specific tools), its response is seamlessly relayed back through the Tutor Agent to the user, providing a unified and intelligent tutoring experience.

# AI Tutor System

## Project Description

The AI Tutor System is a sophisticated multi-agent application designed to provide intelligent and specialized tutoring assistance across various subjects. Unlike a monolithic AI, this system intelligently routes user queries to specialized "expert" agents, each equipped to handle specific domains like mathematics or physics. Furthermore, these specialist agents can leverage "tools" to provide accurate and detailed responses, mimicking a real-world tutoring experience.

**Core Components:**

* **Tutor Agent (Main Agent):** This serves as the primary interface for the student. It receives natural language queries (e.g., "What is Newton's second law?" or "Can you help me solve 2x + 5 = 11?") and, through intelligent intent recognition (using keyword matching or the Gemini API), delegates the query to the most appropriate specialist sub-agent.
* **Sub-Agents (Specialist Agents):**
    * **Math Agent:** Specialized in answering mathematics-related questions.
    * **Physics Agent:** Specialized in answering physics-related questions.
    Each sub-agent is capable of processing tasks/queries from the Tutor Agent and generating detailed responses using the Gemini API.
* **Tool Usage:**
    * **Calculator Tool (for Math Agent):** A simple arithmetic calculator integrated with the Math Agent, allowing it to perform basic operations (addition, subtraction, multiplication, division) for solving or verifying mathematical problems.
    * **Physics Constants Lookup Tool (for Physics Agent):** A function that allows the Physics Agent to retrieve common physical constants (e.g., speed of light, gravitational constant) from a predefined knowledge base, enhancing its ability to provide accurate answers.

**Agent Communication & Orchestration:**

The Tutor Agent acts as the orchestrator, intelligently routing queries to the chosen sub-agent. Once a sub-agent processes the query (potentially using its specific tools), its response is seamlessly relayed back through the Tutor Agent to the user, providing a unified and intelligent tutoring experience.


## Setup Instructions

Follow these steps to get the AI Tutor System running on your local machine.

### Prerequisites

* Python 3.9+ (Recommended)
* `pip` (Python package installer)
* Git

1.Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone [https://github.com/RiyaDharsandiya/google-adk.git](https://github.com/RiyaDharsandiya/google-adk.git)
cd google-adk/tutor_system

2. Create a Virtual Environment (Recommended)

python -m venv .venv
source .venv/bin/activate  # On Linux/macOS
# .venv\Scripts\activate   # On Windows

3.Install Dependencies
cd tutor_system

pip install -r requirements.txt

4.Configure Environment Variables
GEMINI_API_KEY=YOUR_GEMINI_API_KEY


How to Run Locally
1.Ensure Virtual Environment is Active:
source .venv/bin/activate  # On Linux/macOS
# .venv\Scripts\activate   # On Windows

2.Start the ADK Web Application:
cd tutor_system
adk web

3.Access the Application:
http://127.0.0.1:8000

###Live Deployed Application LINK


Agent Interaction and Tool Usage Explained
The system is designed for intelligent delegation and enhanced response generation:

* User Query to Tutor Agent: A student's query first arrives at the Tutor Agent.
* Intent Recognition & Delegation: The Tutor Agent analyzes the query. It might use simple keyword matching (e.g., "solve," "calculate" for math; "physics," "law" for physics) or a more advanced intent classification via the Gemini API to determine the subject. Based on this, it directs the query to the appropriate Sub-Agent (e.g., Math Agent or Physics Agent).
* Sub-Agent Processing: The chosen Sub-Agent receives the query. It then uses its specialized knowledge and the Gemini API to formulate a response.
* Tool Invocation (If Applicable):
If the Math Agent detects a numerical calculation (e.g., "2x + 5 = 11" or "What is 15 divided by 3?"), it will invoke its Calculator Tool to perform the arithmetic and incorporate the result into its explanation.
If the Physics Agent needs a constant (e.g., "What is the speed of light?"), it will query its Physics Constants Lookup Tool to retrieve the accurate value.
* Response Back to User: The Sub-Agent sends its generated answer back to the Tutor Agent, which then presents it to the user as a seamless response.
This modular approach ensures that each agent is focused and highly capable in its domain, while tools enhance their ability to provide precise and helpful information.

### Challenges Faced and Overcoming Them 
Challenge 1: Agent Orchestration and Routing Logic:
Description: Initially, implementing robust logic for the Tutor Agent to accurately determine the correct Sub-Agent for diverse queries proved tricky. Simple keyword matching could be brittle.
Overcoming: We explored using the Gemini API for more advanced intent classification, prompting it to categorize the query into subjects (Math, Physics, etc.). This significantly improved the routing accuracy compared to rigid keyword-based rules.
Challenge 2: Integrating Tools with Agents:
Description: Ensuring that agents knew when and how to call their respective tools effectively was a learning curve. For instance, making the Math Agent intelligently parse mathematical expressions from natural language for the calculator tool.
Overcoming: We implemented specific parsing logic within the agent's code to identify tool-triggering phrases or patterns. For the Gemini API, we experimented with prompt engineering, guiding the LLM to output a structured request that could then be parsed and executed by the tool.
Challenge 3: Environment Variable Management for Deployment:
Description: Properly handling sensitive API keys and other configurations for local development versus cloud deployment required careful attention to .env files and platform-specific environment settings.
Overcoming: Strictly adhering to .gitignore for .env files and then diligently setting environment variables in Vercel/Railway dashboards ensured that sensitive information was never exposed in the codebase.


Contributors:

Riya Dharsandiya