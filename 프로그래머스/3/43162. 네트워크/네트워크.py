'''
각 노드로부터 연결된 노드들을 리스트 형태로 담은 딕셔너리를 만들고,
union-find 알고리즘으로 간접, 직접적으로 연결된 노드 중 최소값들을 찾는다.
최소노드들의 종류를 구하면 된다.
'''
def solution(n, computers):
    def find(node): # 최소 노드(부모 노드)를 찾는 함수
        if node != parents[node]:
            parents[node] = find(parents[node])
        return parents[node]
    def union(a,b): # 연결된 두 노드의 부모 노드를 합치는 함수
        a,b = find(a), find(b)
        if a > b: # 더 작은 부모 노드로 통일
            parents[a] = parents[b]
        elif a < b:
            parents[b] = parents[a]
    parents = [i for i in range(n)] # 부모 노드를 담을 리스트, 시작은 자기 자신
    # 간선을 하나씩 받으면서
    for sta_node in range(n):
        conn = computers[sta_node]
        for arr_node in range(n):
            if arr_node != sta_node and conn[arr_node] == 1:
                union(sta_node,arr_node)
    for node in range(n): # 미처 부모 노드를 갱신하지 못한 노드 갱신
        parents[node] = find(node)
    return len(set(parents))