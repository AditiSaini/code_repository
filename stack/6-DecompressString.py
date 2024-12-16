def decompress(s: str) -> str:
    count = 0
    num = 0
    cur_str = ''
    stack = []
    while count<len(s):
        char = s[count]
        if char.isdigit():
            num = num*10+int(char)
        elif char =="[":
            stack.append((num, cur_str))
            num = 0
            cur_str = ''
        elif char == "]":
            multiplier, prev_str = stack.pop()
            cur_str = prev_str + cur_str*multiplier
        else:
            cur_str+=char
        count+=1
    return cur_str

compressed_string = "3[a]2[3[b]]c"
decompressed_string = decompress(compressed_string)
print(decompressed_string)  # Output: "abccabccabcc"


#C3.ai (OA on 15th Dec 2024)