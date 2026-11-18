word1 = input()
word2 = input()

word1 = sorted(word1)
word2 = sorted(word2)

count = 0
if word1 == word2:
    count += 1

word1 == word1[::-1]
word2 == word2[::-1]

if word1 == word2:
    count += 1

if count >= 1:
    print("Yes")
else:
    print("No")