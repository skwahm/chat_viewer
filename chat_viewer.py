import json
import sys
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text

class JSONChatViewer:
    def __init__(self, theme: str = "monokai"):
        self.console = Console()
        self.theme = theme

    def load_json(self, file_path: str) -> list:
        with open(file_path, 'r') as f:
            return json.load(f)

    def json_to_markdown(self, data: list) -> str:
        markdown = ""
        for i, message in enumerate(data):
            role = message['role']
            content = message['content']

            if role == 'system':
                markdown += f"**System Message:**\n\n{content}\n\n---\n\n"
            else:
                markdown += f"### [{i}] {role.capitalize()}\n\n{content}\n\n"

        return markdown

    def view(self, file_path: str):
        data = self.load_json(file_path)
        markdown_content = self.json_to_markdown(data)
        markdown = Markdown(markdown_content, code_theme=self.theme)
        self.console.print(markdown)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_json_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    viewer = JSONChatViewer()
    viewer.view(file_path)

if __name__ == "__main__":
    main()