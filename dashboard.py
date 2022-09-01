from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(width=120, record=True)
tree = Tree("[link=https://www.github.com/ogdhruv]Dhruv",
            guide_style="bold cyan")
my_tree = tree.add("Learning python", guide_style="bold purple")
my_tree.add("Right now on the #100DayofWeb")
my_tree.add("On the road to Django web development and DevOps")

project = tree.add("My projects", guide_style="bold green")
project.add("will add soon")


about = """
Hi, i am Dhruv, a sophomore pursuing my bachelors in Computer Science and Engineering.
I have a passion of learning everything.
I'm learning Python right now, most of my time is
spent on terminal and DSA.\
"""


panel = Panel.fit(about, box=box.HEAVY, border_style="red",
                  title="[bold]Hello fellow dev!", width=60)

console.print(Columns([panel, tree]))

HTML_FORMAT = """\
<pre style="font-family:'Space Mono','DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""
console.save_html("README.md", inline_styles=True, code_format=HTML_FORMAT)
