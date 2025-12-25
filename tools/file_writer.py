from crewai.tools import tool
from pathlib import Path

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

@tool("File Writer Tool")
def write_report(filename: str, content: str) -> str:
    """
    Write content to a markdown file.
    """
    path = OUTPUT_DIR / filename
    path.write_text(content, encoding="utf-8")
    return f"Report saved to {path}"
