class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = ''

        for char in s:
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            elif char == '[':
                stack.append((cur_str, cur_num))
                cur_str = ''
                cur_num = 0
            elif char == ']':
                prev_str, num = stack.pop()
                cur_str = prev_str + cur_str * num
            else:
                cur_str += char

        return cur_str


print(Solution.decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
print(Solution.decodeString("3[a2[c]]"))   # Output: "accaccacc"
print(Solution.decodeString("2[abc]3[cd]ef"))