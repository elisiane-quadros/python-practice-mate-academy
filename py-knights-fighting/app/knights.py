from typing import List, Optional, Dict


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: List[Dict],
        weapon: Dict,
        potion: Optional[Dict] = None
    ) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.apply_modifiers()

    def apply_modifiers(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)
        self.power = self.base_power + self.weapon["power"]

        if self.potion:
            self.hp += self.potion["effect"].get("hp", 0)
            self.power += self.potion["effect"].get("power", 0)
            self.protection += self.potion["effect"].get("protection", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= max(0, damage)
        if self.hp < 0:
            self.hp = 0
