import random
import time

# defines a card with its name, elixir cost, role, and what it counters
class Card:
    def __init__(self, name, cost, role, counters):
        self.name = name
        self.cost = cost
        self.role = role
        self.counters = counters

    def __repr__(self):
        return f"{self.name} (Cost: {self.cost}, Role: {self.role})"

# real cards with simple tags for how they behave
card_db = {
    "Musketeer": Card("Musketeer", 4, "air_defense", ["air", "support"]),
    "Valkyrie": Card("Valkyrie", 4, "splash", ["swarm", "melee"]),
    "Mini P.E.K.K.A": Card("Mini P.E.K.K.A", 4, "dps", ["tank"]),
    "Fireball": Card("Fireball", 4, "spell", ["swarm", "support"]),
    "Zap": Card("Zap", 2, "spell", ["swarm", "reset"]),
    "Log": Card("Log", 2, "spell", ["swarm", "ground"]),
    "Goblin Barrel": Card("Goblin Barrel", 3, "bait", []),
    "Knight": Card("Knight", 3, "melee", []),
    "Ice Spirit": Card("Ice Spirit", 1, "cycle", []),
    "Inferno Tower": Card("Inferno Tower", 5, "building", ["tank"]),
    "Princess": Card("Princess", 3, "support", ["swarm", "air"]),
    "Golem": Card("Golem", 8, "tank", []),
    "Archers": Card("Archers", 3, "air_defense", ["air"]),
    "Balloon": Card("Balloon", 5, "wincon", ["tower"]),
    "Lava Hound": Card("Lava Hound", 7, "air_tank", []),
    "Mega Minion": Card("Mega Minion", 3, "air_defense", ["air"]),
    "Guards": Card("Guards", 3, "swarm", ["melee"]),
    "Skeleton Army": Card("Skeleton Army", 3, "swarm", ["tank", "melee"]),
    "Inferno Dragon": Card("Inferno Dragon", 4, "air_dps", ["tank"]),
    "Tombstone": Card("Tombstone", 3, "building", ["melee"]),
}

# one example deck
deck = [
    "Goblin Barrel", "Knight", "Princess", "Inferno Tower",
    "Log", "Ice Spirit", "Fireball", "Skeleton Army"
]

# chooses the best card to play based on current elixir and enemy units
def choose_card_to_play(hand, elixir, enemy_units):
    best_card = None
    best_score = float('-inf')

    for name in hand:
        if name not in card_db:
            continue
        card = card_db[name]
        if card.cost > elixir:
            continue  # skip cards we can't afford

        score = 0

        # +3 for each enemy type the card counters
        for enemy in enemy_units:
            if enemy in card.counters:
                score += 3

        # bonus for playing strong cards when at full elixir
        if elixir == 10 and card.cost >= 5:
            score += 2

        # penalty for expensive cards (so we don't overcommit)
        score -= card.cost * 0.2

        if score > best_score:
            best_score = score
            best_card = card

    return best_card

# runs the match simulation
def simulate_match(deck, match_time=30):
    print("Clash Royale Greedy Match Start")

    # shuffle the deck and draw the first 4 cards
    full_deck = deck[:]
    random.shuffle(full_deck)
    cycle_queue = full_deck[:]
    hand = cycle_queue[:4]
    cycle_queue = cycle_queue[4:]

    elixir = 5.0  # starting elixir
    time_step = 1
    regen_rate = 0.36  # elixir regenerated each second
    timer = 0
    next_enemy_turn = random.randint(5, 10)
    enemy_units = []

    while timer < match_time:
        print()
        print(f"Time: {timer}s")
        elixir = min(10, elixir + regen_rate)  # regenerate elixir
        print(f"Elixir: {round(elixir, 1)}")

        # spawn new enemy units every few seconds
        if timer == next_enemy_turn:
            enemy_units = random.choice([
                ["swarm"],
                ["air"],
                ["tank"],
                ["swarm", "air"],
                ["melee"]
            ])
            print(f"Enemy units appeared: {enemy_units}")
            next_enemy_turn += random.randint(5, 10)

        print(f"Your hand: {hand}")
        chosen = choose_card_to_play(hand, int(elixir), enemy_units)

        if chosen:
            print(f"Played: {chosen.name} for {chosen.cost} elixir")
            elixir -= chosen.cost
            hand.remove(chosen.name)

            # draw a new card to replace the one played
            if cycle_queue:
                new_card = cycle_queue.pop(0)
                hand.append(new_card)
                cycle_queue.append(chosen.name)  # cycle the used card to the back
        else:
            print("No good card to play or not enough elixir")

        time.sleep(0.5)  # slows down the simulation output a bit
        timer += time_step

    print()
    print("Match Over")

# run it
if __name__ == "__main__":
    simulate_match(deck, match_time=30)

