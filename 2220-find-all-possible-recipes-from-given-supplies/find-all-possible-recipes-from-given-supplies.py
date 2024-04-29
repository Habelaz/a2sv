class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incoming = defaultdict(int)

        for i in range(len(ingredients)):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
                incoming[recipes[i]] += 1
        # print(graph)
        q = deque(supplies)
        ans = []

        while q:
            for i in range(len(q)):
                node = q.popleft()
                for nbr in graph[node]:
                    incoming[nbr] -= 1
                    if incoming[nbr] == 0:
                        q.append(nbr)
                        ans.append(nbr)

        return ans