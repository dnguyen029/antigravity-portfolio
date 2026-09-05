"""
🤖 AI RECEPTIONIST AGENT TOPOLOGY (PORTFOLIO SHOWCASE)
Defines the routing architecture, specialist sub-agents, and Gemini model options
using the Google Agents SDK (ADK).
"""

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

# Initialize the Gemini model options
model = Gemini(
    model="gemini-3.1-flash-live",
    retry_options=types.HttpRetryOptions(attempts=3),
)

# 1. Lead Capture Specialist
lead_capture_agent = Agent(
    name="lead_capture_agent",
    model=model,
    description="Captures customer name, phone number, and email address to log callback requests.",
    instruction="Greet politely, capture name, phone, and email. Confirm details before logging.",
)

# 2. WISMO (Where Is My Order) Specialist
wismo_agent = Agent(
    name="wismo_agent",
    model=model,
    description="Helps callers track their shipping status and look up order details using PO numbers.",
    instruction="Ask for the Purchase Order (PO) number, query order status, and report details.",
)

# 3. FAQ Specialist
faq_agent = Agent(
    name="faq_agent",
    model=model,
    description="Answers general inquiries, returns policies, and product specifications using web search.",
    instruction="Search the knowledge base to answer questions about products, returns, and FAQs.",
)

# 4. Exit / Call Closer Specialist
exit_agent = Agent(
    name="exit_agent",
    model=model,
    description="Politely handles call closure, delivers final greetings, and terminates the session.",
    instruction="Provide a polite closing statement and end the call session.",
)

# 5. Core Router Agent (Main entrypoint)
router_agent = Agent(
    name="router_agent",
    model=model,
    description="Main entrypoint routing callers to specialized agents based on conversation intent.",
    instruction="Classify the user intent and route to the correct sub-agent.",
    sub_agents=[lead_capture_agent, wismo_agent, faq_agent, exit_agent],
)

# Application entrypoint wrapping the agent topology
app = App(
    root_agent=router_agent,
    name="ai_receptionist_app",
)
