"""Logo create sub-agent."""

from google.adk.agents import Agent

MODEL = "gemini-2.5-pro"

logo_create_agent = Agent(
    name="logo_create_agent",
    model=MODEL,
    description="Helps conceptualize and design a memorable logo for your brand.",
    instruction=(
        "You are a specialized logo design assistant. Guide the user "
        "through visual concepts, color schemes, style choices, and branding ideas "
        "to help them create a professional logo."
    ),
)