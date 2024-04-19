class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        freq = [(-cnt,word) for word,cnt in count.items()]
        heapify(freq)
        return [heappop(freq)[1] for i in range(k)]
        
