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

### Day 8
- Interesting one! First time I built a visualizer to help debug an issue with part 1. Weirdly again part 2 was pretty straightforward. Perhaps that means I engineered part 1 well? :)
- Looping through a dict
- Passing functions as arguments

### Day 9
- I started using Co-pilot in the IDE for this one. I used it about 9 months ago and found my feelings haven't changed much in that time. For code suggestions, most of them were completely off or close-but-wrong. The only suggestions I actually took were trivial anyway. Meanwhile, the constant suggestions added quite a bit of extra cognitive load over time. Eventually I disabled them since I found them more costly than beneficial. I remember these suggestions being quite good for unit tests, but still not for code like this. I also like using the prompts to do things like complex refactors. Just not the auto suggestions.
- There's also an Ask function for Co-pilot. This functions similar to the web interface of Claude that I'm using, except it's in a side panel in the IDE. It's a cool idea, but I actually kind of prefer the web interface of Claude just so I can access my chats organized by Advent of Code day from anywhere. You can name chats in the IDE co-pilot too, but they seem tied to the project somehow rather than just accessible account-wide. I haven't looked too much into it, so some of these assertions might be wrong, but I found I just kept using the Claude web interface for this experiment. One exception is for really simple queries for say how to use an API I just can't remember.
- I haven't used the Agent versions of Co-pilot or Claude code. Advent of Code doesn't seem like a good test of these, so my plan is try these soon but not as part of this experiment.
- I had a very different implementation for part 1 and part 2. For part 1 I used a list to represent each block on disk, since that seemed like the simplest way to handle all the fragmenting. I could tell using a similar method for part 2 would cause excessive execution time, but defining blocks could allow for a few key optimizations. My idea seemed to work pretty well, and I think part 2 was actually faster execution than part 1.
- Iterators
- Classes
- Reverse ranges
- Range steps (e.g. 2)
- Filtering dicts
- Filtering lists of classes by parameter (i.e. min with lambda)
- The above doesn't work with empty lists
- Sort lists of classes by parameter (again, lambda)
- list.remove (how has this not come up before?)

### Day 10
- This one seemed much easier than Day 9. Maybe because I'm already familiar with grid traversal and recursion, but not tricks that would have helped yesterday? Either way, this one went pretty fast.
- Tuples (in Sets!)

### Day 11
- These ones are fun! It always makes me smile when part 1 is a bit long-running and then part 2 simply says "now do the same thing but many more times". Of course the naive algorithm isn't difficult, the trick is optimizing the solution enough to compute in a reasonable amount of time. I'll record my attempts:
  - I determined that I didn't need to manage the list at all (splitting/concating), I just needed a count. This sped things up quite a bit and for 25 iterations was sufficiently fast.
  - I attempted to only do string conversions after determining if it was necessary, via a check for number of digits that Claude taught me. This was only a marginal increase in speed, hardly noteworthy.
  - I used dynamic programming to attempt to remember already-computed counts. The sheer scope of possibilities of stone values and iteration numbers means you want to be a bit judicious with what you store. I started off with just storing counts for 0s since they seemed relatively common, but this didn't have much effect.
  - The evolution of the last point led to pre-computing counts for ALL iterations and storing them. Initially I did this for just 0, and it was still taking forever. I didn't have data, but my logic told me it must have had some effect.
  - The big insight came when I realized that numbers of lengths of powers of two would reduce to their component single digits in log2(n) iterations. This led me to expanding the pre-computed values to all digits instead of only 0. This was the big key, and the correct solution was computed very fast, maybe just over a second. Nice!
- writing/reading json
- didn't use, but Claude taught me a neat trick to determine if an integer is a power of two: `n > 0 and (n & (n - 1)) == 0`. It wasn't immediately clear to me why `n & (n - 1) == 0` would work, but Claude gave a great explanation.
