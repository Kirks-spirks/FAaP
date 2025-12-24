s = 0
for i in range(1,100):
    s = s+i
print(s)
from rich.console import Console
from rich.panel import Panel

console = Console()


console.print(Panel("Статус вашего заказа".center(75), border_style="white"))