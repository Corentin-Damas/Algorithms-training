
from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        choices = set(("A", "C", "G", "T"))
        bank = set(bank)
        queue = deque([(startGene, 0)])
        visited = {startGene}

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps

            for i, s, in enumerate(gene):
                for c in choices:
                    if s != c:
                        new_gene = gene[:i] + c + gene[i+1:]
                        if new_gene in bank and new_gene not in visited:
                            visited.add(new_gene)
                            queue.append((new_gene, steps + 1))
        return -1
