# Real life challenge
A human can easily spot that there is an ordered list of items and subitems in the below example. The challenge is to make a computer figure out that the number of items is really just 3 with some items having subitems:

```
1. The planet earth is not flat
1. People have travelled around it following always just one direction, most recently on January 8.
2. Astronauts have sent realtime videos back to earth while in space, most recently on November 28.
3. The more zoom capability you have does not translate into seeing more in the horizon
4. Gravity and surface tension win most of the time resulting in rounded objects
2. Humans have visited the moon
3. Global warming is rising water levels and increasing year around temperatures around the world

```

The program that parses the above list must be aware of the possible existence of an inner list for any of the top list elements, otherwise will return 4, 8 or 24 to be the number of scientific claims when in reality there are only 3 of them in the list.

# Python problem
Given a list of integers where each number can have a nested list of numbers referring to it
Print the greatest of the consecutive numbers that is a top parent

# Python solution
Given that there is only one possible level of nested numbers
Then there is no need for recursion or tree based solution
Therefore three variables can take care of the problem. First one to be aware of whether we are at level zero (the parents) or level 1 (children of any parent). Second the current item number in the level 1. Third the current item number in the level 0 (current parent number).

# Tests
To test the solution we create a number of files with an integer per line. Test 3.txt is the one corresponding to the real life challenge described in this document.
```
python printLastParentNumber.py 1.txt && \
python printLastParentNumber.py 2.txt && \
python printLastParentNumber.py 3.txt && \
python printLastParentNumber.py 4.txt && \
python printLastParentNumber.py 5.txt
```
