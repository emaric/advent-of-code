def countDownAndUp(number):
    print(number)

    if number == 0:
        # BASE CASE
        print("Reached the base case.")
        return
    else:
        # RECURSIVE CASE
        countDownAndUp(number - 1)

        # After recursive call
        print(number, "returning")
        return


countDownAndUp(3)

# head-tail:
# head = first element, tail = everything after first
"""
    What is the base case? 
        An empty array, which has the sum of 0.
    What argument is passed to the recursive function call? 
        The tail of the original number array, which has one less number than the original array argument.
    How does this argument become closer to the base case? 
        The array argument shrinks by one element for each recursive call until it becomes a zero-length, or empty, array.
"""


def sum(numbers):
    if len(numbers) == 0:  # BASE CASE
        return 0
    else:  # RECURSIVE CASE
        head = numbers[0]
        tail = numbers[1:]
        return head + sum(tail)


"""
for a maze:
    
    What is the base case? 
        Reaching a dead end or the exit of the maze.
    What argument is passed to the recursive function call? 
        The x, y coordinates, along with the maze data and list of already visited x, y coordinates.
    How does this argument become closer to the base case? 
       the x, y coordinates keep moving to neighboring coordinates until they eventually reach dead ends or the final exit.

"""


"""
permutations:
    What is the base case? 
        An argument of a single character string or empty string, which returns an array of just that string.
    What argument is passed to the recursive function call? 
        The string argument missing one character. A separate recursive call is made for each character missing.
    How does this argument become closer to the base case? 
        The size of the string shrinks and eventually becomes a single-character string.
"""


def getPerms(chars, indent=0):
    print("." * indent + 'Start of getPerms("' + chars + '")')
    if len(chars) == 1:
        # BASE CASE
        print("." * indent + 'When chars = "' + chars + '" base case returns', chars)
        return [chars]

    # RECURSIVE CASE
    permutations = []
    head = chars[0]
    tail = chars[1:]
    tailPermutations = getPerms(tail, indent + 1)
    for tailPerm in tailPermutations:
        print(
            "." * indent + "When chars =",
            chars,
            "putting head",
            head,
            "in all places in",
            tailPerm,
        )
        for i in range(len(tailPerm) + 1):
            newPerm = tailPerm[0:i] + head + tailPerm[i:]
            print("." * indent + "New permutation:", newPerm)
            permutations.append(newPerm)
    print("." * indent + "When chars =", chars, "results are", permutations)
    return permutations


print('Permutations of "ABC":')
print("Results:", ",".join(getPerms("ABC")))
