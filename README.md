# Outline:

(Description from UCSD's Combinatorics and Probability Coursera course)

- The game is very simple: two players pick a dice each from a given pool of dices with various numbers on their sides. Then each player throws his dice and the one with the greater number on his dice wins. The game looks very simple and it seems that it is very easy to play this game optimally once we know our pool of dices. Yet it turns out that this intuition is overwhelmingly wrong: the game turns out to be very counterintuitive. This program determines an optimal strategy to play the game.
- The essential crux of the game was to determine an optimum strategy to play the game: if there were a dice that yielded a better result than all of the other die, we would choose to play first and use that dice else if no dice was *ultimate* then we would let our opponents pick first and then pick the die that could best the dice picked by our opponent and yielded the greatest win percentage against our opponents die.
- The return type therefore was a dictionary which detailed our strategy:

    ```python
    {'choose_first': False, 0: 1, 2: 0, 1: 2}
    ```

    For example this outcome meant that no die was ultimate and beat all the others and if the opponent chose die 0, we were to choose 1, if they chose 2 we were to choose 0 and finally if they chose 1 we were to choose 2.
- A more detailed description lies below.

# Purpose:

- The program was a required portion of the Combinatorics & Probability Course by UCSD on Coursera and solving this puzzle helped me understand the nuances of linear random variables (discrete), Markov's inequality as well as fundamental combinatorics. These helped me understand the place for discrete math in a field such as Computer Science.

# Description:

- The program is rather easy to understand and user 2 key functions: one as a driver and the other to test all the outcomes between 2 die and return the victor as well as the percentage of game's won.
- Defaultdict is used in this program to create a dictionary of lists, can_lose which detail a dice and then all the other die it can lose too as well as the win percentage of the respective die, making it so that I can choose the best die for each scenario by sorting them via percentage.
- The dice_ref dictionary is used to store the dice using a quasi index, the reason for which is to account for any duplicate die otherwise simply the index of the die in the original list could have been used.
- The strategy dictionary houses what is to be returned and in case there is a die that can beat every other one, it is reflected and returned.
- While the itertools and defaultdict dependencies are not extremely necessary per se, they are used in order to aid readability and make the code more idiomatic.
