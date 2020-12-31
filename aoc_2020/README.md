# Advent of Code 2020

## Day 1

- 2sum: hash table

- 3sum: two pointers

## Day 2

- strings

## Day 3

- arrays

## Day 4

- strings. ```string.hexdigits``` and ```string.digits``` came in handy.

## Day 5

- Binary search

## Day 6

- set operation: union (```|```) and intersection (```&```)

## Day 7

- Graph

- part 1 is easy, writing a DFS in iterative fashion

- part 2 (I think) can be done with level-based BFS (written in an iterative fashion), so that we can multiply the number of bags over. I ended up writing the recursion though.

## Day 8

- set

## Day 9

- dp maybe? sliding window?

## Day 10

- Tried using backtracking but took forever on the actual input

- Learnt from [this YouTube Video](https://www.youtube.com/watch?v=cE88K2kFZn0) and rewrote the thing in DP

## Day 11

- array

## Day 12

- coordinate system

- geometry?

## Day 13

- made a mistake on [operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)

- naive iteration won't solve part 2 in time...

- something about prime numbers and remainder theorem, learnt from [this YouTube Video](https://www.youtube.com/watch?v=x40aLK9KjYQ)

- Okay it's something I came across a long long time ago. Shame on myself.

- There's a section titled "Chinese remainder theorem" on competitive programming handbook

## Day 14

- strings

- arrays

- enumeration

## Day 15

- hash table

## Day 16

- Intersting one. Part 2 feels like solving linear equation systems, i.e. after LU-Factorization, we will end up with equations with 1, 2, 3, ..., n variables and then we can tackle them one by one.

## Day 17

- Multi-dimensional array. Feels like one problem from last year.

## Day 18

- parser? Maybe I can write a stack and evaluate them in order?

- [George Hotz's solution](https://www.youtube.com/watch?v=OxDp11u-GUo) was really cool, blew my mind

    - try this "abusive Python solution" first

    - [eval function](https://docs.python.org/3/library/functions.html#eval)

    - implement two dunder methods

    - use [regex](https://docs.python.org/3/library/re.html#re.sub) to insert the cutsom class

- [Anthonywritescode's solution](https://www.youtube.com/watch?v=2Xyg6Zjv2PM) using regular expression to handle the nested parenthesis is very cool as well

## Day 19

- Regular expression / context free grammar?

- I tried use Python's re module but somehow my implementation is too slow

- Watched [GeoHots' stream](https://www.youtube.com/watch?v=OxDp11u-GUo) to learn part 2

## Day 20

- part 1 might be really simple? I only need to find tiles whose boarders appear (1, 1, 2, 2) times. These will be the corner tiles

    - yeah it is that simple. I overthought

## Day 22

- normal array operation

- I got stuck on part 2 for probably 2, 3 hours. I was able to get the correct answer for the example case quickly but got "guess too large" on the actual input.

## Day 23

- Linked list. I implememnted using array and the run time is crazy. Still feeling very stupid on this one.

- Checked Youtube video [1](https://www.youtube.com/watch?v=Um2LI6EgfjA) and [2](https://www.youtube.com/watch?v=iD4R7wSNrdw) and their corresponding git repos. Re-factored the code a bit. And got the final answer correct.

## Day 24

- Modleing the envrionment with a coordinate system

- Learnt from [twitch stream of anthonywritescode](https://www.twitch.tv/videos/848239372) on how to handle this type of "infinitely expanding problem"


