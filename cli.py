import json
from rich import print
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel
import script  #

console = Console()

with open("config.json") as f:
    styles_config = json.load(f)

style = Style.from_dict(styles_config["prompt_toolkit"])

def render_mixed_text(text: str):
    lines = text.splitlines()
    inside_code = False
    code_lines = []

    for line in lines:
        if line.strip().startswith("```") and not inside_code:
            inside_code = True
            lang = line.strip()[3:].strip() or "code"
            code_lines = []
        elif line.strip().startswith("```") and inside_code:
            inside_code = False
            code_content = "\n".join(code_lines)
            syntax = Syntax(
                code_content,
                lang,
                theme=styles_config["rich"]["syntax_theme"],
                line_numbers=True,
            )
            panel = Panel(syntax, border_style=styles_config["rich"]["panel_border_style"])
            console.print(panel)
        elif inside_code:
            code_lines.append(line)
        else:
            console.print(line)


if __name__ == "__main__":
    while True:
        try:
            content = prompt([('class:prompt', '> ')], style=style)
            render_mixed_text(script.get_response(content))
        except KeyboardInterrupt:
            break
