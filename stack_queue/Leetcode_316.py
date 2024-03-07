class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = {}
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        stack = []
        for c in s:
            if stack and stack[-1] > c and count[stack[-1]] > 1:
                copy_stack, copy_count = stack[::], {}
                for i, v in count.items():
                    copy_count[i] = v
                while (
                    copy_stack and copy_stack[-1] > c and copy_count[copy_stack[-1]] > 1
                ):
                    copy_count[copy_stack.pop()] -= 1
                if not copy_stack or copy_stack[-1] != c and c not in copy_stack:
                    copy_stack.append(c)
                    stack = copy_stack[::]
                    for i, v in copy_count.items():
                        count[i] = v
                else:
                    count[c] -= 1
            else:
                if stack and stack[-1] == c:
                    count[c] -= 1
                    pass
                else:
                    stack.append(c)

        result = []
        for c in stack:
            if count[c]:
                result.append(c)
            count[c] = False

        return "".join(result)


"""
제출하고 통과안된 케이스에 맞게 계속 수정.
그래서 그런지 스파게티 코드가 되버림.
처음부분에 stack에 동일한 것을 제외시키는 조건문만 추가하면 깔끔해짐.
"""
