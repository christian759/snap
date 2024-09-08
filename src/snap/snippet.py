class Snippet:
    def __init__(self, name: str, category: str, content: str = ""):
        self.name: str = name
        self.category: str = category
        self.content: str = content

    def __str__(self):
        print(f"new class called {self.name} has been created")
        return f"{self.name} ({self.category})"

    def set_content(self, content: str) -> None:
        self.content = content

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "content": self.content
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["category"], data["content"])

