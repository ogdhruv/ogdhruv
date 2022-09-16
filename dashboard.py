from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(width=120, record=True)
tree = Tree("[bold]😎️[link=https://www.github.com/ogdhruv]Dhruv[/bold]",
            guide_style="bold cyan")
my_tree = tree.add("[bold]🐍️Learning python[/bold]", guide_style="bold purple")
my_tree.add("📈️#100DayofWeb")
my_tree.add("Django")
my_tree.add("👨‍💻️DevOps")
project = tree.add("[bold]💻️My projects[/bold]", guide_style="bold green")
project.add("🌟️[link=https://github.com/ogdhruv/faster-kid]fasterKid")
project.add("🗓️soon will add more")


about = """
Hi, i am Dhruv, a sophomore pursuing my bachelors in Computer Science and Engineering.
I have a passion of learning everything.
I'm learning Python right now, most of my time
is spent on terminal and DSA.
"""

additional_add_touch = """
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/https://www.linkedin.com/in/dhruv-r-a87564183/) [![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?logo=Twitter&logoColor=white)](https://twitter.com/OGdhruv) 
"""

panel = Panel.fit(about, box=box.HEAVY, border_style="white",
                  title="[bold]Hello fellow dev!✌️", width=50)

console.print(Columns([panel, tree]))

HTML_FORMAT = """\
<pre style="font-family:'Space Mono','DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""
console.save_html("README.md", inline_styles=True, code_format=HTML_FORMAT)
