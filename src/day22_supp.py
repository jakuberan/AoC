def eval_deck(deck):
    """
    Evaluates a deck
    """
    return sum([deck[i] * (len(deck) - i) for i in range(len(deck))])


def deck_to_string(deck):
    """
    Converts a deck to string
    """
    out = ""
    for d in deck:
        if d < 10:
            out += "0"
        out += str(d)
    return out


def play_game(deck1, deck2):
    """
    Plays the game
    """

    # Memories of already used decks
    deck_memory = []

    # Run the game
    while len(deck1) * len(deck2) > 0:

        # Avoid infinite loops, represent decks more 'efficiently'
        deck1_string = deck_to_string(deck1)
        deck2_string = deck_to_string(deck2)
        if [deck1_string, deck2_string] in deck_memory:
            return True, []
        else:
            deck_memory.append([deck1_string, deck2_string])

        # Draw cards
        p1n = deck1.pop(0)
        p2n = deck2.pop(0)

        # Play subgame
        if p1n <= len(deck1) and p2n <= len(deck2):
            result = play_game(deck1.copy()[:p1n], deck2.copy()[:p2n])[0]
        # Play regular game
        else:
            result = p1n > p2n

        # Evaluate game
        if result:
            deck1.append(p1n)
            deck1.append(p2n)
        else:
            deck2.append(p2n)
            deck2.append(p1n)

    # Return winning array and append all appeared combinations
    if len(deck1) > 0:
        return True, deck1
    else:
        return False, deck2
