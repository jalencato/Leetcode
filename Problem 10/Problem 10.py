pattern = "a*"
string = "aa"


def isMatch(context, pattern):
    if not pattern:
        return not context
    if context:
        match_iter = pattern[0] in {context[0], '.'}
    else:
        match_iter = False

    # once for kleen star we can pop the character in the context one by one
    # at this time we keep the pattern unchanged for we still need the first characte
    if len(pattern) >= 2 and pattern[1] in {'*'}:
        return (isMatch(context, pattern[2:]) or
                match_iter and isMatch(context[1:], pattern))
    else:
        return match_iter and isMatch(context[1:], pattern[1:])


if __name__ == '__main__':
    print(isMatch(string, pattern))
