"""Website create sub-agent."""

from google.adk.agents import Agent

MODEL = "gemini-2.5-pro"

website_create_agent = Agent(
    name="website_create_agent",
    model=MODEL,
    description="Helps design and build a professional website for your brand.",
    instruction=(
        "You are a specialized website development assistant. Help the user "
        "structure pages, plan layouts, write web copy, and establish their online platform."
    ),
)