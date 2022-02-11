# 최단경로문제: 각 간선의 가중치 합이 최소가 되는 두 정점(또는 노드) 사이의 경로를 찾는 문제

# 다익스트라 알고리즘: 항상 노드 주변을 BFS로 최단 경로만 택하는 대표적인 그리디 알고리즘.임의의 정점을 출발 집합에 더할 때
# 그 정점까지의 최단거리는 계산이 끝났다는 확신을 갖고 더하므로 만일 이후에 더 짧은 경로가 존재한다면 논리적 기반이 무너진다.
# 따라서 가중치가 음수인 경우 처리할 수 없고 모두 양수가 되도록 더하거나 벨만-포드 알고리즘 같은 다른 알고리즘을 사용해야함
# 같은 이유로 최장 거리를 구하는 데에는 다익스트라 알고리즘을 사용할 수 없음
