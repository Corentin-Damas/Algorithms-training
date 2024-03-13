from typing import List


class Solution:
    def fullJustify(words: List[str], maxWidth: int) -> List[str]:

        res = []
        ligne = []
        lenLigne = 0
        idx = 0
        while len(words) > idx:
            # len current words in the the line + simple spaces between words + new words > maxWidth
            if lenLigne + len(ligne) + len(words[idx]) > maxWidth:
                extra_space = maxWidth-lenLigne
                repartition = extra_space // max(1, len(ligne) - 1)
                remainder = extra_space % max(1, len(ligne) - 1)

                for s in range(max(1, len(ligne) - 1)):
                    ligne[s] += " " * repartition
                    if remainder:
                        ligne[s] += " "
                        remainder -= 1

                res.append("".join(ligne))
                ligne = []
                lenLigne = 0

            ligne.append(words[idx])
            lenLigne += len(words[idx])
            idx += 1

        last_line = " ".join(ligne)
        final_space = maxWidth - len(last_line)
        res.append(last_line + " " * final_space)

        return res


case01 = ["This", "is", "an", "example", "of", "text", "justification."]
print(Solution.fullJustify(case01, 16))
# [
#   "This    is    an",
#   "example  of text",
#   "justification.  "
# ]
