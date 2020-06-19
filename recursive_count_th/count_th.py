'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    """
    args: string
    returns: number of occurence of "th" in string
    """
    # TBC
    chrc = "th"
    # base case if string is empty 
    if len(word) == 0:
        return 0
    # check if first two words are chrc
    # and
    # traverse array two words at a time
    elif word[:2] == chrc:
        return count_th(word[2:]) + 1
    # or we go back and start traversing
    # from the first word 
    # to ensure all words are checked
    else:
        return count_th(word[1:])

