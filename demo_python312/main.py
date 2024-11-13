from typing import override

class Base:
    def get_color(self) -> str:
        return "blue"

class GoodChild(Base):
    @override  # This decorator indicates this method overrides one in the parent class
    def get_color(self) -> str:
        return "yellow"

class BadChild(Base):
    @override  # Typing error will be flagged here due to misspelling 'color'
    def get_colour(self) -> str:
        return "red"

print(GoodChild().get_color())

print(BadChild().get_colour())