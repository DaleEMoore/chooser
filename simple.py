# chooser or Choose-Number

# Set correct numbers 3 and 7.
# Ask user, what number am I thinking of.
# If it's 3 or 7, congratulate them.
# Let them try again.

__author__ = 'dalem'

# TODO; make thinking_of two values randomly assigned on each execution.
thinking_of = [3, 5, 7]

while True:
    guess = input("What number am I thinking of between 1 and 10? ")

    if guess in thinking_of:
        print("Congratulations I was thinking of " + ''.join(str(e) for e in thinking_of))
        break
    else:
        print("Nope, try again.")
