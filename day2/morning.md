## Dictionaries and Sets

Today we're going to get comfortable with dictionaries and sets.

### Part 1: Write some functions

In `src/dict_exercise.py` you will find some function stubs. You should fill in the functions according to the docstrings.

1. Fill out the functions in `src/dict_exercise.py`.

    *Focus on getting a working solution before attempting to modify your solutions to be one liners.*

    Test each function by running `nosetests src/test_dict.py`.

### Part 2: Efficiency

In this exercise, we're going to be taking a look at some code that's already working and figuring out how to improve it using dictionaries/sets.

The code is written in an inefficient way. We'll start by timing how long it takes with the current implementation, then doing your improvement and timing it again.

Take a look at the example code in `src/efficiency.py`. We'll start with the first question.

1. Run the first example using `%time` in `ipython`. Here is the code to run it:

    ```python
    from src import efficiency
    with open('data/wordlist.txt') as f:
        words = [line.lower().strip() for line in f]
    %time invalid = efficiency.invalid_words(words, 'data/frankenstein_small.txt')
    ```

    This should give you output of how long this took to run. **Write this value down.** (You can try running it on the full Frankenstein file, but you probably don't want to wait for that).

    this is what I got
    CPU times: user 8.73 s, sys: 20 ms, total: 8.75 s
    Wall time: 8.92 s

    Note: The best way to copy this into `ipython` is to copy it normally and then type `%paste` in `ipython`.

2. Make your improvements to the `invalid_words` function. You will need to run `reload(efficiency)` in `ipython` to get the updated version.

    Make sure you didn't change the functionality of the functions by running `nosetests src/test_efficiency.py`.

    Time timing it again. Is it faster?

    changed it to a set and then...
    CPU times: user 32 ms, sys: 4 ms, total: 36 ms
    Wall time: 36.9 ms
    holy fucking set

3. Repeat the above process for the second function, `common_characters`.

    This code will create a long string that you can use to run your function on.

    ```python
    import string
    import random

    mystring = "".join(random.choice(string.lowercase) for i in xrange(100000))
    ```
    from src import efficiency
    %time common = efficiency.common_characters(mystring, 2)
    CPU times: user 11.1 s, sys: 16 ms, total: 11.1 s
    Wall time: 11.2 s




    For the second parameter in the function, choose a number that makes sense. If it's too small, probably all the letters will appear more than that number of times. The expected number of times a letter would appear is 100000/26 = 3846, so choose something around there.

    **Since you are creating a random string for this, you should make sure you are using the same random string both times you run your function.

4. Repeat the same process once more with the `sum_to_zero` function.

    Use the following code to create a large list of integers:

    ```python.
    import random
    mylist = [random.randrange(-1,100000) for i in xrange(100000)]
    from src import efficiency
    %time zerosum = efficiency.sum_to_zero(mylist)
    ```
    %time common = efficiency.sum_to_zero(mylist)
    CPU times: user 3min 37s, sys: 516 ms, total: 3min 37s
    Wall time: 3min 38s


    Again, time how long it takes to run on this list before you change anything. Then make your changes and run again on the same list!

### Extra: Improve your algorithm from yesterday!

Yesterday you implemented a `substring` function. Today you're going to redo that function using a dictionary.

Look at the divisors example from lecture for inspiration.

1. Fill out the function in `substring.py`. Put in both your old and your new version so that you can compare them.

2. Run `nosetests test_substring.py` to make sure that both versions work properly.

3. Use `%time` to see if it's improved in efficiency! Figure out an example input that's sufficiency large that you'll be able to test the difference.

4. How would you change if instead you wanted for each substring, the list of words it was in?

    *Hint: Use a `defaultdict`*.
