from collections import deque


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    visit = [0 for i in range(len(words))]
    while q:
        word, count = q.popleft()
        if word == target:
            answer = count
            return answer
        for i in range(len(words)):
            stack = 0
            if not visit[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        stack += 1
                    else:
                        pass
                if stack == 1:
                    q.append([words[i], count+1])  # 하나의 글자만 틀리다면, q에 바뀔 글자와 카운트를 1 더해서 넣어줌.
                    visit[i] = 1  # 이 단어(words[i])와 카운트는 방문한 노드가 됨.

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))
