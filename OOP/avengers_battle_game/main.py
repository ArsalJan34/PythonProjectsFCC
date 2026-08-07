"""
AVENGERS: ASSEMBLE — a pure Object-Oriented Python game.

Pick a hero from your roster and battle waves of villains to save the city!

OOP concepts demonstrated:
  - Abstraction    -> Hero and Villain are abstract base classes
  - Inheritance    -> each hero/villain extends a common base
  - Polymorphism   -> attack() / special_ability() behave differently per class
  - Encapsulation  -> HP/energy are private, changed only through methods
"""

from __future__ import annotations
from abc import ABC, abstractmethod
import random


# --------------------------------------------------------------------------
# BASE CLASSES
# --------------------------------------------------------------------------

class Combatant(ABC):
    """Abstract base for any character that can fight."""

    def __init__(self, name: str, max_hp: int):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def is_alive(self) -> bool:
        return self._hp > 0

    def take_damage(self, amount: int) -> None:
        self._hp = max(0, self._hp - amount)

    def heal(self, amount: int) -> None:
        self._hp = min(self._max_hp, self._hp + amount)

    @abstractmethod
    def attack(self, target: "Combatant") -> None:
        raise NotImplementedError

    @abstractmethod
    def special_ability(self, target: "Combatant") -> None:
        raise NotImplementedError

    def hp_bar(self, width: int = 20) -> str:
        filled = int(width * self._hp / self._max_hp)
        return f"[{'█' * filled}{'-' * (width - filled)}] {self._hp}/{self._max_hp} HP"

    def __str__(self) -> str:
        return f"{self._name} - {self.hp_bar()}"


class Hero(Combatant):
    """Base class for all playable heroes."""

    def __init__(self, name: str, max_hp: int, max_energy: int):
        super().__init__(name, max_hp)
        self._max_energy = max_energy
        self._energy = max_energy

    @property
    def energy(self) -> int:
        return self._energy

    def _spend_energy(self, amount: int) -> bool:
        if self._energy < amount:
            return False
        self._energy -= amount
        return True

    def regen_energy(self, amount: int = 10) -> None:
        self._energy = min(self._max_energy, self._energy + amount)

    def __str__(self) -> str:
        return (f"{self._name} - {self.hp_bar()} | "
                f"Energy: {self._energy}/{self._max_energy}")


class Villain(Combatant):
    """Base class for all enemy villains."""

    def __init__(self, name: str, max_hp: int, threat_reward: int):
        super().__init__(name, max_hp)
        self._threat_reward = threat_reward

    @property
    def threat_reward(self) -> int:
        return self._threat_reward

    def choose_action(self, target: Combatant) -> None:
        if random.random() < 0.3:
            self.special_ability(target)
        else:
            self.attack(target)


# --------------------------------------------------------------------------
# HEROES
# --------------------------------------------------------------------------

class ArmoredInventor(Hero):
    """A genius in a powered suit of armor."""

    def __init__(self):
        super().__init__("Iron Suit", max_hp=90, max_energy=40)

    def attack(self, target: Combatant) -> None:
        dmg = random.randint(10, 16)
        target.take_damage(dmg)
        print(f"{self._name} fires repulsor blasts at {target.name} for {dmg} damage!")

    def special_ability(self, target: Combatant) -> None:
        cost = 15
        if not self._spend_energy(cost):
            print(f"{self._name} is out of energy! Attacking instead.")
            self.attack(target)
            return
        dmg = random.randint(25, 35)
        target.take_damage(dmg)
        print(f"💥 {self._name} unleashes a UNIBEAM for {dmg} damage! (-{cost} energy)")


class SuperSoldier(Hero):
    """A shield-wielding tactician."""

    def __init__(self):
        super().__init__("Shield Bearer", max_hp=110, max_energy=30)

    def attack(self, target: Combatant) -> None:
        dmg = random.randint(8, 14)
        target.take_damage(dmg)
        print(f"{self._name} bashes {target.name} with their shield for {dmg} damage!")

    def special_ability(self, target: Combatant) -> None:
        cost = 12
        if not self._spend_energy(cost):
            print(f"{self._name} is out of energy! Attacking instead.")
            self.attack(target)
            return
        dmg = random.randint(18, 24)
        target.take_damage(dmg)
        print(f"🛡️  {self._name} throws a RICOCHET SHIELD STRIKE for {dmg} damage! (-{cost} energy)")


class ThunderGod(Hero):
    """A god of thunder wielding an enchanted hammer."""

    def __init__(self):
        super().__init__("Storm Bringer", max_hp=130, max_energy=35)

    def attack(self, target: Combatant) -> None:
        dmg = random.randint(12, 18)
        target.take_damage(dmg)
        print(f"{self._name} swings their hammer at {target.name} for {dmg} damage!")

    def special_ability(self, target: Combatant) -> None:
        cost = 18
        if not self._spend_energy(cost):
            print(f"{self._name} is out of energy! Attacking instead.")
            self.attack(target)
            return
        dmg = random.randint(30, 40)
        target.take_damage(dmg)
        print(f"⚡ {self._name} calls down LIGHTNING for {dmg} damage! (-{cost} energy)")


class MysticSorcerer(Hero):
    """A master of the mystic arts."""

    def __init__(self):
        super().__init__("Mystic Mage", max_hp=80, max_energy=50)

    def attack(self, target: Combatant) -> None:
        dmg = random.randint(9, 15)
        target.take_damage(dmg)
        print(f"{self._name} strikes {target.name} with a bolt of magic for {dmg} damage!")

    def special_ability(self, target: Combatant) -> None:
        cost = 20
        if not self._spend_energy(cost):
            print(f"{self._name} is out of energy! Attacking instead.")
            self.attack(target)
            return
        dmg = random.randint(28, 38)
        target.take_damage(dmg)
        print(f"🔮 {self._name} opens a PORTAL BARRAGE for {dmg} damage! (-{cost} energy)")


HERO_ROSTER = {
    "1": ArmoredInventor,
    "2": SuperSoldier,
    "3": ThunderGod,
    "4": MysticSorcerer,
}


# --------------------------------------------------------------------------
# VILLAINS
# --------------------------------------------------------------------------

class RogueRobot(Villain):
    def __init__(self):
        super().__init__("Rogue Sentinel Bot", max_hp=50, threat_reward=15)

    def attack(self, target: Combatant) -> None:
        dmg = random.randint(6, 12)
        target.take_damage(dmg)
        print(f"{self._name} fires a laser at {target.name} for {dmg} damage!")

    def special_ability(self, target: Combatant) -> None:
        dmg = random.randint(14, 20)
        target.take_damage(dmg)
        print(f"⚠️  {self._name} overcharges its cannon for {dmg} damage!")


class MercenaryDuo(Villain):
    def __init__(self):
        super().__init__("Masked Mercenaries", max_hp=65, threat_reward=20)

    def attack(self, target: Combatant) -> None:
        dmg = random.randint(8, 14)
        target.take_damage(dmg)
        print(f"{self._name} strike {target.name} for {dmg} damage!")

    def special_ability(self, target: Combatant) -> None:
        dmg = random.randint(16, 24)
        target.take_damage(dmg)
        print(f"⚠️  {self._name} launch a coordinated ambush for {dmg} damage!")


class RivalGenius(Villain):
    def __init__(self):
        super().__init__("Rival Genius", max_hp=70, threat_reward=25)

    def attack(self, target: Combatant) -> None:
        dmg = random.randint(9, 15)
        target.take_damage(dmg)
        print(f"{self._name} blasts {target.name} with an energy device for {dmg} damage!")

    def special_ability(self, target: Combatant) -> None:
        dmg = random.randint(18, 26)
        target.take_damage(dmg)
        print(f"⚠️  {self._name} deploys a swarm of drones for {dmg} damage!")


class CosmicWarlord(Villain):
    """Final boss."""

    def __init__(self):
        super().__init__("Cosmic Warlord", max_hp=150, threat_reward=100)

    def attack(self, target: Combatant) -> None:
        dmg = random.randint(14, 20)
        target.take_damage(dmg)
        print(f"{self._name} smashes {target.name} for {dmg} damage!")

    def special_ability(self, target: Combatant) -> None:
        dmg = random.randint(30, 45)
        target.take_damage(dmg)
        print(f"🌌 {self._name} channels COSMIC POWER for {dmg} damage!")


VILLAIN_SEQUENCE = [RogueRobot, MercenaryDuo, RivalGenius, CosmicWarlord]


# --------------------------------------------------------------------------
# BATTLE ENGINE
# --------------------------------------------------------------------------

class Battle:
    """Coordinates turns between a Hero and a Villain."""

    def __init__(self, hero: Hero, villain: Villain):
        self._hero = hero
        self._villain = villain

    def _hero_turn(self) -> None:
        print(f"\n{self._hero}")
        print(f"{self._villain}")
        print("\nChoose an action:")
        print("  1. Attack")
        print("  2. Special Ability")
        print("  3. Regroup (heal a little, restore energy)")
        choice = input("> ").strip()

        if choice == "1":
            self._hero.attack(self._villain)
        elif choice == "2":
            self._hero.special_ability(self._villain)
        elif choice == "3":
            self._hero.heal(10)
            self._hero.regen_energy(12)
            print(f"{self._hero.name} regroups, recovering HP and energy.")
        else:
            print("Invalid choice, you hesitate and lose your turn!")

    def _villain_turn(self) -> None:
        if self._villain.is_alive:
            self._villain.choose_action(self._hero)

    def run(self) -> bool:
        print(f"\n🚨 {self._villain.name} threatens the city! 🚨")
        while self._hero.is_alive and self._villain.is_alive:
            self._hero_turn()
            self._villain_turn()

        if self._hero.is_alive:
            print(f"\n🏆 {self._hero.name} defeated {self._villain.name}!")
            return True
        else:
            print(f"\n💀 {self._hero.name} was defeated by {self._villain.name}...")
            return False


# --------------------------------------------------------------------------
# GAME (top-level controller)
# --------------------------------------------------------------------------

class Game:
    """Top-level controller: hero selection, progression through villains."""

    def __init__(self):
        self._hero: Hero | None = None
        self._threat_score = 0

    def _select_hero(self) -> None:
        print("=" * 55)
        print("            AVENGERS: ASSEMBLE — HERO SELECT")
        print("=" * 55)
        print("Choose your hero:")
        print("  1. Iron Suit      (armored inventor, tech-based blasts)")
        print("  2. Shield Bearer  (super soldier, tactical shield strikes)")
        print("  3. Storm Bringer  (thunder god, devastating lightning)")
        print("  4. Mystic Mage    (sorcerer, powerful magic barrages)")
        choice = input("> ").strip()
        hero_cls = HERO_ROSTER.get(choice, ArmoredInventor)
        self._hero = hero_cls()
        print(f"\n{self._hero.name} assembles, ready for battle!")

    def run(self) -> None:
        self._select_hero()

        for villain_cls in VILLAIN_SEQUENCE:
            if not self._hero.is_alive:
                break
            villain = villain_cls()
            battle = Battle(self._hero, villain)
            won = battle.run()
            if not won:
                print(f"\nFinal Threat Score: {self._threat_score}")
                print("GAME OVER. Thanks for playing!")
                return
            self._threat_score += villain.threat_reward
            print(f"Threat Score: {self._threat_score}")
            input("\nPress Enter to face the next threat...")

        if self._hero.is_alive:
            print("\n" + "=" * 55)
            print(f"🎉 {self._hero.name} has saved the city! FINAL SCORE: "
                  f"{self._threat_score} 🎉")
            print("=" * 55)


if __name__ == "__main__":
    Game().run()
