"""Domain create sub-agent."""

from google.adk.agents import Agent

MODEL = "gemini-2.5-pro"

domain_create_agent = Agent(
    name="domain_create_agent",
    model=MODEL,
    description="Helps generate and check creative domain names for your brand.",
    instruction=(
        "You are a specialized domain name generation assistant. Help the user "
        "brainstorm creative, available domain names based on their keywords."
    ),
)