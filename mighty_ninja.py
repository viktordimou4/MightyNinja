#!/usr/bin/env python3
"""
MightyNinja - Heavy Ninja Action Game
A ninja combat simulator with intense action and special moves!
"""

import random
import time


class Ninja:
    """A mighty ninja warrior with heavy action capabilities."""
    
    def __init__(self, name, strength=50, agility=50, stealth=50):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.stealth = stealth
        self.health = 100
        self.energy = 100
        
    def __str__(self):
        return f"{self.name} - HP: {self.health} | Energy: {self.energy} | STR: {self.strength} | AGI: {self.agility} | STL: {self.stealth}"
    
    def heavy_strike(self, target):
        """Unleash a devastating heavy strike on the target."""
        if self.energy < 20:
            return f"{self.name} doesn't have enough energy for a heavy strike!"
        
        self.energy -= 20
        damage = int(self.strength * 1.5 + random.randint(-10, 10))
        target.health -= damage
        return f"💥 {self.name} delivers a HEAVY STRIKE to {target.name} for {damage} damage!"
    
    def shadow_assault(self, target):
        """A swift, stealthy attack combining agility and stealth."""
        if self.energy < 30:
            return f"{self.name} doesn't have enough energy for shadow assault!"
        
        self.energy -= 30
        # Stealth affects hit chance, agility affects damage
        hit_chance = min(95, self.stealth + self.agility // 2)
        
        if random.randint(1, 100) <= hit_chance:
            damage = int(self.agility * 1.2 + self.stealth * 0.8)
            target.health -= damage
            return f"🌙 {self.name} strikes from the shadows! Shadow Assault hits {target.name} for {damage} damage!"
        else:
            return f"⚡ {self.name}'s Shadow Assault missed! {target.name} detected the attack!"
    
    def berserker_fury(self, target):
        """Ultimate heavy attack - multiple devastating strikes!"""
        if self.energy < 50:
            return f"{self.name} doesn't have enough energy for Berserker Fury!"
        
        self.energy -= 50
        total_damage = 0
        strikes = 3
        results = [f"🔥 {self.name} unleashes BERSERKER FURY!"]
        
        for i in range(strikes):
            damage = int(self.strength * 0.8 + random.randint(5, 15))
            total_damage += damage
            target.health -= damage
            results.append(f"   Strike {i+1}: {damage} damage!")
        
        results.append(f"   Total damage: {total_damage}!")
        return "\n".join(results)
    
    def stealth_recovery(self):
        """Use stealth to meditate and recover energy."""
        recovery = int(self.stealth * 0.5 + random.randint(10, 20))
        self.energy = min(100, self.energy + recovery)
        return f"🧘 {self.name} meditates in stealth, recovering {recovery} energy!"
    
    def dodge(self):
        """Attempt to dodge incoming attacks."""
        dodge_chance = min(90, self.agility + random.randint(-10, 10))
        return random.randint(1, 100) <= dodge_chance
    
    def is_alive(self):
        """Check if the ninja is still standing."""
        return self.health > 0


class NinjaGang:
    """A gang of mighty ninjas ready for heavy action."""
    
    def __init__(self):
        self.ninjas = []
    
    def add_ninja(self, ninja):
        """Add a ninja to the gang."""
        self.ninjas.append(ninja)
        print(f"✅ {ninja.name} has joined the gang!")
    
    def show_gang(self):
        """Display all ninjas in the gang."""
        print("\n=== MIGHTY NINJA GANG ===")
        for ninja in self.ninjas:
            status = "💀 Defeated" if not ninja.is_alive() else "⚔️ Ready"
            print(f"{status} {ninja}")
        print("========================\n")


def heavy_battle(ninja1, ninja2):
    """Initiate a heavy ninja battle between two warriors."""
    print("\n" + "="*60)
    print(f"⚔️  HEAVY NINJA ACTION BATTLE ⚔️")
    print(f"{ninja1.name} VS {ninja2.name}")
    print("="*60 + "\n")
    
    round_num = 1
    
    while ninja1.is_alive() and ninja2.is_alive():
        print(f"\n--- Round {round_num} ---")
        print(f"{ninja1}")
        print(f"{ninja2}\n")
        
        # Ninja 1's turn
        action = random.choice(['heavy_strike', 'shadow_assault', 'berserker_fury', 'stealth_recovery'])
        
        if action == 'heavy_strike':
            result = ninja1.heavy_strike(ninja2)
        elif action == 'shadow_assault':
            result = ninja1.shadow_assault(ninja2)
        elif action == 'berserker_fury':
            result = ninja1.berserker_fury(ninja2)
        else:
            result = ninja1.stealth_recovery()
        
        print(result)
        time.sleep(0.5)
        
        if not ninja2.is_alive():
            break
        
        # Ninja 2's turn
        action = random.choice(['heavy_strike', 'shadow_assault', 'berserker_fury', 'stealth_recovery'])
        
        if action == 'heavy_strike':
            result = ninja2.heavy_strike(ninja1)
        elif action == 'shadow_assault':
            result = ninja2.shadow_assault(ninja1)
        elif action == 'berserker_fury':
            result = ninja2.berserker_fury(ninja1)
        else:
            result = ninja2.stealth_recovery()
        
        print(result)
        time.sleep(0.5)
        
        round_num += 1
    
    print("\n" + "="*60)
    winner = ninja1 if ninja1.is_alive() else ninja2
    print(f"🏆 VICTORY! {winner.name} wins the battle!")
    print("="*60 + "\n")


def main():
    """Main entry point for MightyNinja heavy action demo."""
    print("""
    ███╗   ███╗██╗ ██████╗ ██╗  ██╗████████╗██╗   ██╗
    ████╗ ████║██║██╔════╝ ██║  ██║╚══██╔══╝╚██╗ ██╔╝
    ██╔████╔██║██║██║  ███╗███████║   ██║    ╚████╔╝ 
    ██║╚██╔╝██║██║██║   ██║██╔══██║   ██║     ╚██╔╝  
    ██║ ╚═╝ ██║██║╚██████╔╝██║  ██║   ██║      ██║   
    ╚═╝     ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   
                                                      
    ███╗   ██╗██╗███╗   ██╗     ██╗ █████╗            
    ████╗  ██║██║████╗  ██║     ██║██╔══██╗           
    ██╔██╗ ██║██║██╔██╗ ██║     ██║███████║           
    ██║╚██╗██║██║██║╚██╗██║██   ██║██╔══██║           
    ██║ ╚████║██║██║ ╚████║╚█████╔╝██║  ██║           
    ╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚════╝ ╚═╝  ╚═╝           
    
    🥷 HEAVY NINJA ACTION - Gang Edition 🥷
    """)
    
    # Create a gang of mighty ninjas
    gang = NinjaGang()
    
    # Create ninjas with different specializations
    shadow_master = Ninja("Shadow Master", strength=60, agility=70, stealth=85)
    iron_fist = Ninja("Iron Fist", strength=90, agility=50, stealth=40)
    swift_blade = Ninja("Swift Blade", strength=55, agility=85, stealth=60)
    
    gang.add_ninja(shadow_master)
    gang.add_ninja(iron_fist)
    gang.add_ninja(swift_blade)
    
    gang.show_gang()
    
    # Heavy action battle demonstration
    print("🎬 Initiating heavy ninja action battle sequence...\n")
    time.sleep(1)
    
    heavy_battle(shadow_master, iron_fist)
    
    gang.show_gang()


if __name__ == "__main__":
    main()
