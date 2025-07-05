Repo for 2024 Advent of Code

I want to try learning Python using an AI agent and thought this would be a good way to do it. Planning on Claude and/or Co-pilot.

https://adventofcode.com/2024

## Lessons learned

### Day 1 pt 1
- Used Claude to teach me how to Python. Tried to read API docs too, but asking Claude was much faster. Learning this way leaves a lot of gaps but can fill many of them with general programming knowledge.
- Claude was too talkative sometimes. I just wanted to know how to get the length of an Array and got a whole writeup about it. Maybe a mix of both Claude and Co-pilot would be effective.
- Python fundamentals (modules, import/export, `if __name__ == "__main__"`, try/except, print, string format)
- File reads
- String methods (strip, split)
- Array methods (append, sort)
- Multiple returns
- Destructuring (called "unpacking")
- for in, for in range
- len, abs, int

### Day 1 pt 2
- Used Claude again. Still talkative. Interestingly I asked for something similar to JavaScript's reduce once, and after that it kept giving me examples comparing to JS. It's more than I needed/wanted, though I understand it could be useful to some.
- Dictionaries (maps)
- Ternary operator
- Inline map of a list
- Discovered get method of a dict, which was nice shorthand to safely get a value in an expression (could have used that on line 9, but I left line 9 as a ternary example)
- Not used: or/and, None is like null, truthy/falsey, reduce does exist but so does sum (!)

### Day 2
- Used Claude again. I was using ChatGPT earlier for something unrelated and realized how much slower Claude is. I finally noticed some bugs with code Claude gave me today. I guess it was inevitable, but maybe also more likely as I started asking more complicated questions.
- I had the dreaded moment in part 2 where my code passed the example input, but not the real input. My first approach was just ignoring the first level that made the report unsafe, but I switched to checking each permutation to account for a corner case I was neglecting. This was still pretty fast.
- I tried to make a common module for reading file input that I could import from anywhere in the project, and it was surprisingly difficult. I found a few different paths forward, but they seemed quite arcane and, sure enough, I couldn't get any of them working quickly. I'll look more into this later. This is where AI has some rough edges and real expertise would probably solve it quickly.
- reversed, any
- getting all permutations of an array with one element removed
- also something `itertools.combinations` that can do the above, but I didn't use and opted for manual inline notation