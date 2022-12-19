from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(width=120, record=True)
tree = Tree(
    "[bold]😎️[link=https://www.linkedin.com/in/dhruv-r-a87564183/]Dhruv[/bold]", guide_style="bold cyan"
)
my_tree = tree.add("[bold]🐍️Learning Python[/bold]", guide_style="bold purple")
my_tree.add("Django")
my_tree.add("DevOps")
my_tree.add("ML")
project = tree.add("[bold]💻️My projects[/bold]", guide_style="bold green")
project.add("🌟️[link=https://github.com/ogdhruv/hirethemv2]Hire Them")
project.add(
    "🌟️[link=https://github.com/ogdhruv/duptwt]DuplexTwT (API)"
)
project.add("🌟️[link=https://github.com/ogdhruv/faster-kid]FasterKid")

about = """
Hi, i am Dhruv, a final year student pursuing my bachelors in Computer Science.
I have a passion of learning and .
I'm learning Django right now, most of my time
is spent on understanding microservices and learning new Technologies.
"""

additional_add_touch = """
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/https://www.linkedin.com/in/dhruv-r-a87564183/) [![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?logo=Twitter&logoColor=white)](https://twitter.com/OGdhruv) 
"""

panel = Panel.fit(
    about,
    box=box.HEAVY,
    border_style="white",
    title="[bold]Hello fellow dev!✌️",
    width=50,
)

console.print(
    Columns(
        [panel, tree],
    )
)

HTML_FORMAT = """\
<pre style="font-family:'Space Mono','DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""
console.save_html("README.md", inline_styles=True, code_format=HTML_FORMAT)
