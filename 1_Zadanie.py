A = [1, 2, 3, 4, 6, 7, 9, 10, 11, 13, 14, 17, 24, 26, 28, 29, 31, 32, 34, 35, 37, 38, 39]
B = [1, 2, 4, 10, 12, 13, 15, 17, 18, 19, 25, 30, 33, 34, 35, 36, 37]
C = [2, 7, 9, 14, 16, 21, 23, 25, 27, 28, 29, 32, 34, 35, 36, 37, 38]
D = [1, 3, 5, 6, 9, 10, 14, 15, 19, 21, 23, 28, 29, 31, 34, 35, 36, 37]

def sim_raz(ar1,ar2):
    res = []
    for i in ar1:
        if i not in ar2:
            res.append(i)
    for i in ar2:
        if i not in ar1:
            res.append(i)
    return sorted(res)

def raz(ar1,ar2):
    res = []
    for i in ar1:
        if i not in ar2:
            res.append(i)
    return res

def unite(ar1,ar2):
    return sorted(set(ar1+ar2))

def cross(ar1,ar2):
    res = []
    for i in ar1:
        if i in ar2:
            res.append(i)
    return res
  
#1. ((D ∆ C) ∩ (B \ A) ∩ C) ∆ ((B ∪ D) ∩ (D ∆ A))
#2. (D ∪ B) ∩ ((C ∪ D) \ (B ∩ A)) ∩ ((D \ (C ∩ A)) ∪ (B ∆ A))

print(sim_raz(cross(cross(sim_raz(D,C),raz(B,A)),C),cross(unite(B,D),sim_raz(D,A))))
print(cross(unite(D,B),cross(raz(unite(C,D),cross(B,A)),unite(raz(D,cross(C,A)),sim_raz(B,A)))))
