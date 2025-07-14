class Weapon:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    @classmethod
    def from_string_classmethod(cls, weapon_string: str):
        weapon_name, weapon_power = weapon_string.split()
        return cls(weapon_name, int(weapon_power))
    @staticmethod
    def from_string_staticmethod(weapon_string: str):
        weapon_name, weapon_power = weapon_string.split()
        return Weapon(weapon_name, int(weapon_power))

weapon = Weapon.from_string_classmethod(("weapon 100"))
print(weapon.__class__)
print(weapon.__dict__)

weapon= Weapon.from_string_staticmethod("weapon 100")
print(weapon.__class__)
print(weapon.__dict__)