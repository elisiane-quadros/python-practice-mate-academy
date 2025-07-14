from app.knights import Knight


def battle(knights_config: dict) -> dict:
    knights = {name: Knight(**stats) for name, stats in knights_config.items()}

    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    for knight1, knight2 in battles:
        if knight1 not in knights or knight2 not in knights:
            raise ValueError(
                f"Cavaleiros {knight1} ou {knight2} não encontrados!")

        knights[knight1].take_damage(
            knights[knight2].power - knights[knight1].protection)
        knights[knight2].take_damage(
            knights[knight1].power - knights[knight2].protection)

    return {
        knight.name: knight.hp for knight in knights.values()
    }
