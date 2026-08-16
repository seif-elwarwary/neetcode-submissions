from functools import cache

class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)

        @cache
        def play(i: int, alice_turn: bool) -> tuple[int, int]:
            if i == n:
                return 0, 0

            outcomes = []
            taken = 0

            for count in range(1, 4):
                if i + count > n:
                    break

                taken += stoneValue[i + count - 1]
                alice, bob = play(i + count, not alice_turn)

                if alice_turn:
                    alice += taken
                else:
                    bob += taken

                outcomes.append((alice, bob))

            if alice_turn:
                return max(outcomes, key=lambda scores: scores[0])
            return max(outcomes, key=lambda scores: scores[1])

        alice, bob = play(0, True)

        if alice > bob:
            return "Alice"
        if alice < bob:
            return "Bob"
        return "Tie"