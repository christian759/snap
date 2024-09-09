class Snippet:
    """
        A class to represent a code snippet.

        Attributes
        ----------
        name : str
            The name of the snippet.
        category : str
            The category of the snippet.
        content : str
            The content of the snippet.

        Methods
        -------
        __init__(self, name: str, category: str, content: str = "")
            Initializes a new Snippet object.

        __str__(self) -> str
            Returns a string representation of the Snippet object.

        set_content(self, content: str) -> None
            Sets the content of the snippet.

        to_dict(self) -> dict
            Returns a dictionary representation of the Snippet object.

        from_dict(cls, data: dict) -> Snippet
            Creates a new Snippet object from a dictionary.
    """

    def __init__(self, name: str, category: str, content: str = ""):
        self.name: str = name
        self.category: str = category
        self.content: str = content

    def __str__(self):
        print(f"new class called {self.name} under the {self.category} category has been created")
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
