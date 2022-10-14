from reptile import Reptile


class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def use_toungue_to_smell(self):
        return "If I can touch it, I can smell it as well"


smart_snake = Snake()
print(f"Method from Parent Class - {smart_snake.hunt()}")
print(f"Method from Current Class - {smart_snake.use_toungue_to_smell()}")
print(f"Method from Grand Parent Class - {smart_snake.breathe()}")
