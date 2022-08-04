from collections import deque
import sys
# BFS 메서드 정의


def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


input = sys.stdin.readline
# 각 노드가 연결된 정보를 표현(2차원 리스트)
N, M, V = list(map(int, input().split()))
graph = [[0]]
for i in range(M):
    graph.append(list(map(int, input().split())))
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * N

# 정의된 BFS 함수 호출
bfs(graph, V, visited)
