def search(pat, txt):
    M = len(pat)
    N = len(txt)
    for i in range(N - M + 1):
        j = 0
        while j < M:
            if txt[i + j] != pat[j]:
                break
            j += 1
        if j == M:
            print("Pattern found at index", i)

# Driver's Code
tn = int(input("Enter the number of texts: "))
txt = []
for i in range(tn):
    ele = str(input("Enter text element: "))
    txt.append(ele)

pn = int(input("Enter the number of patterns: "))
pat = []
for j in range(pn):
    el = str(input("Enter pattern element: "))
    pat.append(el)

# Function call
search(pat, txt)
