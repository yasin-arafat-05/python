def process_typing(keys):
    typed_string = []
    for key in keys:
        if key == 'b':
            if typed_string and typed_string[-1].islower():
                typed_string.pop()
        elif key == 'B':
            if typed_string and typed_string[-1].isupper():
                typed_string.pop()
        else:
            typed_string.append(key)
    return ''.join(typed_string) 

# Input number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    keys = input().strip()
    result = process_typing(keys)
    
    # Output the result for each test case
    print(result)
