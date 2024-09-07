class Snippet:
    def __init__(self, name: str, category: str):
        self.name: str = name
        self.category: str = category
        self.content: str | None = None

    def __str__(self):
        print(f"new class called {self.name} has been created")
        return f"{self.name} ({self.category})"

    def set_content(self, content: str) -> None:
        self.content = content



