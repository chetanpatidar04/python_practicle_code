# wtp to check valid paranthesis
def valid_para(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '[','>':'<'}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack

# Example usage:
example_str = "(<>(({})))"
if valid_para(example_str):
    print(f"{example_str} is a valid expression.")
else:
    print(f"{example_str} is not a valid expression.")
    