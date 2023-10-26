import textwrap

def wrap(string, max_width):
    lines = textwrap.wrap(string, width=max_width)
    wrapped_string = '\n'.join(lines)
    return wrapped_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
