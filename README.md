Repo for 2024 Advent of Code

I want to try learning Python using an AI agent and thought this would be a good way to do it. Planning on Claude and/or Co-pilot.

https://adventofcode.com/2024

## Usage

```
py -m day[n].main[1,2]
```

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

### Day 3
- Used combination of Claude and StackOverflow to finally get common modules working.
- Good old regular expression problem. Was able to get it working without too much trouble using Claude to teach me regexp in Python. I'm sure I could have inlined it a bit more.
- Regexp
- Getting local module path

### Day 4
- Only used Claude to learn a couple things
- Actually part 1 gave me more trouble than part 2. I misunderstood the problem at first and then had some logic issues. While part 2 I got straightaway on first execution.
- Convert string to list of chars
- Learned that closure is a thing, but ended up refactoring it out to simplify logic

### Day 5
- More Claude! I'll assume I keep using Claude unless stated otherwise
- This one seemed a bit trickier than previous days. There's probably an easier way to solve this, but I ended up with a naive solution. Still fast enough though!
- integer division operator `//` (used to find middle element of a list)
- sets
- rearranging elements in a list (pop, insert)

### Day 6
- My first long-running one. Part 2 took quite awhile to run, maybe 30-60 seconds. I thought one optimization would be to skip any cells that had no # in its row or column, but there were none of those in the input. If it was just a single loop you could probably look for how #s are relatively positioned, but for loops involving more than four #s, I decided to just go for the brute force approach. I did at least try to identify loops quickly and exit, which seemed to work.
- while
- grid initialization and hydration
- enums
- not used: value equality (==) vs reference equality (is)
- also == will do deep equality check

### Day 7
- Pretty straight-forward with recursion. My biggest concern was splitting three-ways in part 2, but it wasn't too bad. I rearranged things to have the fastest-growing branch first, since I exit a branch early if we've exceeded the target due to all operations being growing. The idea was I could more quickly cut out branches of the OR tree, but I'm not positive how effective it was since it is OR. Either way, it still only took around a second to execute.
- Splitting an expression to multiple lines
- Converting to string