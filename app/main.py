from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False

        Animal.alive.append(self)

    def __str__(self) -> str:
        return str(
            {"name": self.name, "health": self.health, "hidden": self.hidden}
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        if isinstance(target, Herbivore):
            if not target.hidden:
                target.health -= 50

                if target.health <= 0:
                    Animal.alive = [
                        animal
                        for animal
                        in Animal.alive
                        if animal.name != target.name
                    ]
