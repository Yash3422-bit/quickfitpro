"""Expanded local multi-agent runner using Ollama with sequential steps."""

from openai import OpenAI

# Initialize client pointing to local Ollama server
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Local placeholder
)

MODEL_NAME = "llama3"

def query_ollama(system_prompt: str, user_message: str) -> str:
    """Sends a request to the local Ollama model."""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error communicating with local Ollama server: {e}"

def run_logo_subagent(brand_name: str) -> str:
    """Sub-agent specialized in generating local text-based logo design descriptions."""
    system_prompt = (
        "You are a specialized logo design sub-agent. Given a brand name and niche, "
        "provide a detailed visual description, color palette, and typography style "
        "for a clean, modern minimalist logo that can be used for a free web app."
    )
    user_prompt = f"Design a striking, motivational logo concept for our quick fitness app named: {brand_name}"
    return query_ollama(system_prompt, user_prompt)

def run_marketing_subagent(brand_name: str) -> str:
    """Sub-agent specialized in creating launch marketing copy."""
    system_prompt = (
        "You are a specialized marketing copywriter sub-agent. Create punchy, high-converting "
        "social media launch copy and a short hero section tagline tailored for busy professionals."
    )
    user_prompt = f"Write launch marketing copy and a landing page tagline for our free fitness app: {brand_name}"
    return query_ollama(system_prompt, user_prompt)

def main():
    print("=" * 60)
    print("Local Multi-Agent Marketing System (Powered by Ollama)")
    print("Type 'exit' or 'quit' to stop.")
    print("=" * 60)

    coordinator_prompt = (
        "You are an expert marketing coordinator agent. Your goal is to help users "
        "establish a powerful online presence using free subdomains (like Vercel or Netlify). "
        "Guide them through defining their digital identity and finalizing their free project name."
    )

    # Simple state machine to manage workflow stages
    stage = "chat"
    chosen_brand_name = "QuickFitPro"  # Default or captured from user

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            if not user_input.strip():
                continue

            if stage == "chat":
                print("\n[Coordinator Processing locally...]")
                response = query_ollama(coordinator_prompt, user_input)
                print(f"\nCoordinator:\n{response}")
                
                # Check if user is ready to move to sub-agents
                print("\n---")
                proceed = input("Would you like to automatically trigger the Logo & Marketing Sub-agents for your app? (yes/no): ").strip().lower()
                if proceed in ["yes", "y"]:
                    stage = "subagents"
                    print(f"\n[Triggering Logo Sub-agent for '{chosen_brand_name}'-...]")
                    logo_output = run_logo_subagent(chosen_brand_name)
                    print(f"\n🎨 [Logo Sub-agent Output]:\n{logo_output}")
                    
                    print(f"\n[Triggering Marketing Copy Sub-agent for '{chosen_brand_name}'...]")
                    marketing_output = run_marketing_subagent(chosen_brand_name)
                    print(f"\n📢 [Marketing Sub-agent Output]:\n{marketing_output}")
                    
                    print("\n=" * 60)
                    print("Pipeline complete! All assets generated locally and privately.")
                    print("=" * 60)
                    break
            
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()