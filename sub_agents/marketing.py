"""Marketing create sub-agent."""

from google.adk.agents import Agent

MODEL = "gemini-2.5-pro"

marketing_create_agent = Agent(
    name="marketing_create_agent",
    model=MODEL,
    description="Helps strategize and build effective online marketing campaigns.",
    instruction=(
        "You are a specialized digital marketing assistant. Help the user "
        "plan advertising strategies, social media campaigns, and audience engagement tactics."
    ),
)