# TODO: Add code here
class Todo:

    def __int__(self, code_id: int, title: str, description: str, completed: bool, tags: list[str]):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: False = completed
        self.tags: list[str] = tags
