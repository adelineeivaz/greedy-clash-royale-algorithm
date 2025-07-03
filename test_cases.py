from _460_01project import choose_card_to_play, card_db

def run_test(test_num, hand, enemy_units, elixir, expected):
    result = choose_card_to_play(hand, elixir, enemy_units)
    actual = result.name if result else "None"
    passed = actual == expected
    print(f"Test {test_num}: {'PASSED' if passed else 'FAILED'}")
    print(f"  Hand: {hand}")
    print(f"  Enemy: {enemy_units}")
    print(f"  Elixir: {elixir}")
    print(f"  Expected: {expected}")
    print(f"  Actual: {actual}")
    print()

def run_all_tests():
    run_test(
        1,
        hand=["Fireball", "Ice Spirit", "Princess", "Skeleton Army"],
        enemy_units=["swarm"],
        elixir=6,
        expected="Fireball"
    )
    run_test(
        2,
        hand=["Mini P.E.K.K.A", "Zap", "Knight", "Archers"],
        enemy_units=["tank"],
        elixir=5,
        expected="Mini P.E.K.K.A"
    )
    run_test(
        3,
        hand=["Musketeer", "Valkyrie", "Skeleton Army", "Princess"],
        enemy_units=["air"],
        elixir=4,
        expected="Musketeer"
    )

if __name__ == "__main__":
    run_all_tests()
