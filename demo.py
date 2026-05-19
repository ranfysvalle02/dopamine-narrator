import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

SCENARIO = {
    "raw_task": "Clean the kitchen",
    "interest": "That one drawer — the junk drawer — what's actually in there? Archaeology mode.",
    "novelty": "Put on a podcast you've been saving. The kitchen is just the excuse to listen.",
    "challenge": "Timer: 10 minutes. Whatever isn't done doesn't exist. Speed run.",
    "urgency": "Company coming tomorrow. This is the last easy win before it gets weird.",
}


def main():
    s = SCENARIO

    console.print(f"\n[bold cyan]DOPAMINE NARRATOR[/bold cyan]  [dim]Interest-Based Activation[/dim]\n")

    # Identify the dead task
    console.print(f"[dim]Raw task:[/dim] [strike]{s['raw_task']}[/strike]")
    console.print(f"[bold magenta]Shame override:[/bold magenta] You're not failing. The task structure has zero fuel.\n")

    # Inject INCU vectors
    console.print("[bold]Reframing with salience vectors:[/bold]\n")
    console.print(f"  [bold]Interest[/bold]   {s['interest']}")
    console.print(f"  [bold]Novelty[/bold]    {s['novelty']}")
    console.print(f"  [bold]Challenge[/bold]  {s['challenge']}")
    console.print(f"  [bold]Urgency[/bold]    {s['urgency']}")

    # Flight plan
    console.print()
    plan = Text()
    plan.append("Entry rule: ", style="bold")
    plan.append("Don't face the macro-mountain.\n")
    plan.append("Spend 180 seconds initializing the Interest layer only.\n")
    plan.append("Don't work to finish. Work to pass the gate.", style="italic cyan")

    console.print(Panel(plan, title="Flight Plan", border_style="cyan"))
    console.print("[bold green]Turn the key. Go.[/bold green]\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n")
        sys.exit(0)
