"""Runner script for my-agent."""

import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import asyncio
from google.adk.runners import InMemoryRunner
from google.genai import types
from agent import root_agent

async def main():
    print("=" * 60)
    print(f"Agent loaded successfully: {root_agent.name}")
    print("Initializing ADK Runner session...")
    
    # Initialize the ADK runner for your root agent
    runner = InMemoryRunner(
        agent=root_agent,
        app_name="marketing_agency_app"
    )
    
    # Create an async session for the conversation
    session = await runner.session_service.create_session(
        app_name="marketing_agency_app",
        user_id="yash_user"
    )
    
    print("Session created successfully!")
    print("Type your message below to start chatting (type 'exit' to quit).")
    print("=" * 60)

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            if not user_input.strip():
                continue

            print(f"\n[Processing with {root_agent.name}...]")
            
            # Package the user input into ADK Content format
            content = types.Content(
                role='user',
                parts=[types.Part.from_text(text=user_input)]
            )
            
            # Run the agent asynchronously and stream/print events
            async for event in runner.run_async(
                user_id="yash_user",
                session_id=session.id,
                new_message=content
            ):
                if event.content and event.content.parts:
                    for part in event.content.parts:
                        if hasattr(part, 'text') and part.text:
                            print(f"\nAgent: {part.text}")
                            
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break

if __name__ == "__main__":
    asyncio.run(main())