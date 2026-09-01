"""Marketing_coordinator Agent assists in creating effective online content."""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

import prompt
from sub_agents.domain_create import domain_create_agent
from sub_agents.logo_create import logo_create_agent
from sub_agents.marketing import marketing_create_agent
from sub_agents.website import website_create_agent

MODEL = "gemini-2.5-pro"

marketing_coordinator = Agent(
    name="marketing_coordinator",
    model=MODEL,
    description=(
        "Establish a powerful online presence and connect with your audience "
        "effectively. Guide you through defining your digital identity, from "
        "choosing the perfect domain name and crafting a professional "
        "website, to strategizing online marketing campaigns, "
        "designing a memorable logo, and creating engaging short videos"
    ),
    instruction=prompt.MARKETING_COORDINATOR_PROMPT,
    tools=[
        AgentTool(agent=domain_create_agent),
        AgentTool(agent=website_create_agent),
        AgentTool(agent=marketing_create_agent),
        AgentTool(agent=logo_create_agent),
    ],
)

root_agent = marketing_coordinator