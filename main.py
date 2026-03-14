from andrea.agent import AndreaAgent
from rich.console import Console
from rich.panel import Console

console = Console()

def main():
    console.print("[bold cyan]Andrea AI Agent System[/bold cyan]")
    
    # Initialize Agent
    agent = AndreaAgent()
    
    # Define Goal
    goal = "Create a market entry strategy for a new AI-powered SaaS tool."
    
    # Planning Phase
    agent.plan(goal)
    
    # Execution Phase
    console.print("\n[bold green]Starting Execution Phase:[/bold green]")
    while True:
        result = agent.execute_next()
        if not result:
            break
        console.print(f"[dim]-> {result}[/dim]")

    console.print("\n[bold gyan]All tasks completed successfully.[/bold cyan]")

if __name__ == "__main__":
    main()