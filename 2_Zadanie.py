from math import comb

print((comb(10,7)*comb(14,3) + comb(10,8)*comb(14,2) + comb(10,9) * comb(14,1) + comb(10,10)*comb(14,0))/ comb(24,10) * 100)
